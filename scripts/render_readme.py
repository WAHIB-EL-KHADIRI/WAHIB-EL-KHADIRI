#!/usr/bin/env python3
"""Render README.md from README.tpl.md, filling in live GitHub stats.

Reads the template, queries the GitHub GraphQL API for lifetime contribution
counts and the contribution calendar, and writes the result to README.md.

Standard library only, so the workflow needs no dependency install step.

Environment:
    GITHUB_TOKEN   required; needs no scopes for public data, but a classic
                   PAT with read:user also counts private contributions.
    GITHUB_LOGIN   optional; defaults to WAHIB-EL-KHADIRI.

Exits non-zero on any API failure so a broken run fails the workflow loudly
instead of committing a README full of placeholders.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

API = "https://api.github.com/graphql"
ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "README.tpl.md"
OUTPUT = ROOT / "README.md"

DEFAULT_LOGIN = "WAHIB-EL-KHADIRI"


class GitHubError(RuntimeError):
    """The API returned an error, or kept failing after retries."""


def graphql(token: str, query: str, variables: dict) -> dict:
    """POST a GraphQL query, retrying the transient failures worth retrying."""
    payload = json.dumps({"query": query, "variables": variables}).encode()
    request = urllib.request.Request(
        API,
        data=payload,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "profile-readme-renderer",
        },
    )

    last_error = ""
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                body = json.loads(response.read())
            if "errors" in body:
                # Query errors are deterministic; retrying them just wastes time.
                raise GitHubError(f"GraphQL: {body['errors']}")
            return body["data"]
        except urllib.error.HTTPError as exc:
            # 502/503 and secondary rate limits are worth another attempt.
            if exc.code not in (429, 500, 502, 503):
                raise GitHubError(f"HTTP {exc.code}: {exc.read()[:300]!r}") from exc
            last_error = f"HTTP {exc.code}"
        except urllib.error.URLError as exc:
            last_error = str(exc.reason)

        time.sleep(2**attempt)

    raise GitHubError(f"gave up after 4 attempts: {last_error}")


PROFILE_QUERY = """
query($login: String!) {
  user(login: $login) {
    createdAt
    repositories(ownerAffiliations: OWNER, privacy: PUBLIC, isFork: false) {
      totalCount
    }
    repositoriesContributedTo(
      privacy: PUBLIC
      contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, REPOSITORY]
    ) {
      totalCount
    }
  }
}
"""

STARS_QUERY = """
query($login: String!, $cursor: String) {
  user(login: $login) {
    repositories(
      first: 100
      after: $cursor
      ownerAffiliations: OWNER
      privacy: PUBLIC
      isFork: false
    ) {
      pageInfo { hasNextPage endCursor }
      nodes { stargazerCount }
    }
  }
}
"""

CONTRIB_QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      totalCommitContributions
      totalIssueContributions
      totalPullRequestContributions
      contributionCalendar {
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


def fetch_stars(token: str, login: str) -> int:
    """Sum stargazers across every non-fork public repo the user owns."""
    total = 0
    cursor = None
    while True:
        repos = graphql(token, STARS_QUERY, {"login": login, "cursor": cursor})
        repos = repos["user"]["repositories"]
        total += sum(node["stargazerCount"] for node in repos["nodes"])
        if not repos["pageInfo"]["hasNextPage"]:
            return total
        cursor = repos["pageInfo"]["endCursor"]


def fetch_contributions(token: str, login: str, joined: dt.datetime) -> tuple[dict, dict]:
    """Walk year by year, since contributionsCollection spans at most a year.

    Returns lifetime totals and a date -> contribution count calendar.
    """
    totals = {"commits": 0, "issues": 0, "prs": 0}
    calendar: dict[str, int] = {}
    now = dt.datetime.now(dt.timezone.utc)

    for year in range(joined.year, now.year + 1):
        start = max(joined, dt.datetime(year, 1, 1, tzinfo=dt.timezone.utc))
        end = min(now, dt.datetime(year, 12, 31, 23, 59, 59, tzinfo=dt.timezone.utc))
        if start >= end:
            continue

        collection = graphql(
            token,
            CONTRIB_QUERY,
            {
                "login": login,
                "from": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "to": end.strftime("%Y-%m-%dT%H:%M:%SZ"),
            },
        )["user"]["contributionsCollection"]

        totals["commits"] += collection["totalCommitContributions"]
        totals["issues"] += collection["totalIssueContributions"]
        totals["prs"] += collection["totalPullRequestContributions"]

        for week in collection["contributionCalendar"]["weeks"]:
            for day in week["contributionDays"]:
                calendar[day["date"]] = day["contributionCount"]

    return totals, calendar


def current_streak(calendar: dict[str, int]) -> int:
    """Count consecutive contributing days ending today.

    A quiet today does not break the streak -- the day is not over yet -- so
    counting starts at yesterday in that case.
    """
    if not calendar:
        return 0

    day = dt.datetime.now(dt.timezone.utc).date()
    if calendar.get(day.isoformat(), 0) == 0:
        day -= dt.timedelta(days=1)

    streak = 0
    while calendar.get(day.isoformat(), 0) > 0:
        streak += 1
        day -= dt.timedelta(days=1)
    return streak


def plural(count: int, noun: str) -> str:
    return f"{count:,} {noun}" + ("" if count == 1 else "s")


def joined_phrase(joined: dt.datetime) -> str:
    """'3 years ago', 'a year ago', or 'this year' -- reads as prose."""
    days = (dt.datetime.now(dt.timezone.utc) - joined).days
    years = days // 365
    if years < 1:
        return "this year"
    if years == 1:
        return "a year ago"
    return f"{years} years ago"


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        print("error: GITHUB_TOKEN is not set", file=sys.stderr)
        return 1

    login = os.environ.get("GITHUB_LOGIN", "").strip() or DEFAULT_LOGIN

    if not TEMPLATE.is_file():
        print(f"error: template not found: {TEMPLATE}", file=sys.stderr)
        return 1
    template = TEMPLATE.read_text(encoding="utf-8")

    try:
        profile = graphql(token, PROFILE_QUERY, {"login": login})["user"]
        joined = dt.datetime.strptime(profile["createdAt"], "%Y-%m-%dT%H:%M:%SZ")
        joined = joined.replace(tzinfo=dt.timezone.utc)

        totals, calendar = fetch_contributions(token, login, joined)
        stars = fetch_stars(token, login)
    except GitHubError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    values = {
        "YEARS": joined_phrase(joined),
        "COMMITS": f"{totals['commits']:,}",
        "ISSUES": f"{totals['issues']:,}",
        "PRS": f"{totals['prs']:,}",
        "STARS": f"{stars:,}",
        "REPOS": f"{profile['repositories']['totalCount']:,}",
        "CONTRIBUTED": f"{profile['repositoriesContributedTo']['totalCount']:,}",
        "STREAK": plural(current_streak(calendar), "day"),
        "UPDATED": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"),
    }

    # The template opens with a note aimed at whoever edits it. That note is
    # wrong once copied into the output, so swap it for one aimed at readers.
    template = re.sub(r"\A<!--.*?-->\n", "", template, count=1, flags=re.DOTALL)
    banner = (
        "<!-- Generated from README.tpl.md by scripts/render_readme.py.\n"
        "     Edits here are overwritten on the next scheduled run. -->\n"
    )

    rendered = banner + template
    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", value)

    leftover = [key for key in values if "{{" + key + "}}" in rendered]
    if leftover:  # a placeholder the replace loop somehow missed
        print(f"error: unfilled placeholders: {leftover}", file=sys.stderr)
        return 1

    OUTPUT.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT.name} for {login}")
    for key, value in values.items():
        print(f"  {key:<12} {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
