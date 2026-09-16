<!-- Generated from README.tpl.md by scripts/render_readme.py.
     Edits here are overwritten on the next scheduled run. -->
<p align="center">
  <img src="https://raw.githubusercontent.com/WAHIB-EL-KHADIRI/WAHIB-EL-KHADIRI/main/assets/terminal.svg" alt="Terminal: whoami -- AI engineer and systems developer from Morocco, building agent infrastructure in Rust" width="820">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white" alt="PHP">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
  &nbsp;·&nbsp;
  <a href="https://wahib-portfolio.netlify.app/"><img src="https://img.shields.io/badge/Portfolio-2E7D32?style=flat-square&logo=googlechrome&logoColor=white" alt="Portfolio"></a>
  <a href="https://dev.to/wahib_el_khadiri_0"><img src="https://img.shields.io/badge/dev.to-0A0A0A?style=flat-square&logo=devdotto&logoColor=white" alt="dev.to"></a>
  <a href="https://www.linkedin.com/in/wahib-el-khadiri-a54134283"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:wahibelkhadiri06@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
</p>

<p align="center">
  <a href="https://github.com/WAHIB-EL-KHADIRI/AgentOS"><img src="https://img.shields.io/github/stars/WAHIB-EL-KHADIRI/AgentOS?style=for-the-badge&logo=github&label=Star%20AgentOS&color=CD7F32&labelColor=0D1117" alt="Star AgentOS on GitHub"></a>
  <a href="https://github.com/WAHIB-EL-KHADIRI?tab=followers"><img src="https://img.shields.io/github/followers/WAHIB-EL-KHADIRI?style=for-the-badge&logo=github&label=Follow&color=2E7D32&labelColor=0D1117" alt="Follow WAHIB-EL-KHADIRI on GitHub"></a>
</p>

---

## 💼 What I build

**Correctness in developer tooling**, mostly in other people's repositories. Two
strands, and the evidence for both is below rather than asserted here:

- **Auto-fixers that corrupt the code they fix.** Linters are trusted to rewrite
  whole repositories unattended. I round-trip a project's own test corpus
  through its `--fix` and check the output still parses — which found data-loss
  bugs in a 9.8k-star SQL linter, and found nothing at all in ruff, which is
  reported just as plainly.
- **Release pipelines that execute their own inputs.** `${{ ... }}` is
  substituted as text before the shell parses the line, so a tag name stops
  being data — usually in the one job holding the publishing credentials.

You can run the first one against your own repository right now. No install,
about a minute, nothing left behind:

```bash
uvx --from "autofix-safety[ruff] @ git+https://github.com/WAHIB-EL-KHADIRI/autofix-safety" autofix-safety-ruff . findings.json
```

It will almost certainly come back clean — that is the common result, and
`findings.json` records the tool version, corpus and flags so a clean run is
checkable rather than just reassuring.

Also Rust systems work: [AgentOS](https://github.com/WAHIB-EL-KHADIRI/AgentOS),
a runtime for supervising long-lived agents and replaying their runs offline.

Web and business systems too — multi-tenant Postgres, RBAC, offline-first
frontends, bilingual FR/AR interfaces with real RTL — but those repositories are
private, so treat this paragraph as context rather than as evidence.

Based in Morocco, working across EMEA and US-morning hours. Open to product
engineering, contract work and consulting.

[wahibelkhadiri06@gmail.com](mailto:wahibelkhadiri06@gmail.com)
· [LinkedIn](https://www.linkedin.com/in/wahib-el-khadiri-a54134283)

## 🔒 Work in other people's repositories

**15 merged pull requests into 12 repositories I don't own**, reviewed and
accepted by their maintainers. The through-line is release-pipeline security:
`${{ ... }}` is pasted into a shell as text before bash parses it, so a tag name
or dispatch input stops being data and becomes part of the program — almost
always in the one job holding the publishing credentials.

**Release-pipeline hardening**

- **[PrefectHQ/prefect](https://github.com/PrefectHQ/prefect)** — ✅ merged: the release ref was expanded into two shell bodies in the jobs that publish to PyPI, one of them holding `id-token: write` for Trusted Publishing ([#22882](https://github.com/PrefectHQ/prefect/pull/22882))
- **[thingctx/thingctx](https://github.com/thingctx/thingctx)** — ✅ merged: pinned every third-party GitHub Action to a commit SHA across CI and release workflows ([#127](https://github.com/thingctx/thingctx/pull/127))
- **[dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)** — the workflow that publishes to GitHub, PyPI and Docker: dispatch inputs expanded unquoted into an `echo` and into a command substitution ([#15994](https://github.com/dbt-labs/dbt-core/pull/15994))
- **[sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff)** — ✅ merged: release workflow: the version input reached a command substitution and a step carrying `GITHUB_TOKEN` ([#8375](https://github.com/sqlfluff/sqlfluff/pull/8375))
- **[sktime/pytorch-forecasting](https://github.com/sktime/pytorch-forecasting)** — PyPI release workflow: tag name expanded into the tag check that gates the build, plus a least-privilege `permissions:` block the file had never declared ([#2385](https://github.com/sktime/pytorch-forecasting/pull/2385))

**Bugs found by tooling I wrote**

Found with [`autofix-safety`](https://github.com/WAHIB-EL-KHADIRI/autofix-safety),
a scanner I wrote: two adapters, one invariant, and results recorded so they can
be checked rather than believed — tool version, corpus commit, command,
environment, limitations. The runs that found **nothing** are recorded
the same way (ruff, across 1,607 of its own fixtures and 1,805 CPython stdlib
files, clean), and so is the finding that stopped reproducing once upstream
fixed it. The issues below are the part you can verify without taking my word
for any of it.


A linter's core promise is that fixing valid input leaves valid input. Almost no
project tests that across its whole corpus — fixtures are tested for *parsing*,
and rules are tested for *their* fix, but not for the two composed. So I wrote a
scanner that asserts it, and pointed it at a 9k-star SQL linter.

I also pointed it at [ruff](https://github.com/astral-sh/ruff) — 1,607 fixtures,
`--select ALL --fix --unsafe-fixes`, with CPython's own `ast.parse` as the judge
rather than the tool under test. **It found nothing.** Reporting that too, because
a method that only publishes its hits is a sales pitch.

- **[sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff)** — `fix` silently
  welds adjacent tokens together, so the file it writes lexes differently from
  the one it read. Still reproducing on `main`: `8 | ~ ~ ~4` → `8 | ~~~4`, and in
  Oracle two *keywords* — `MULTISET EXCEPT` → `MULTISETEXCEPT` — welded by
  `LT02`, a rule whose only job is indentation. Upstream has since patched one
  instance of this class in its own rule ([#8395]); the argument in my PR is that
  guarding once, where fixes are applied, ends the class instead of meeting it
  again in the next layout rule. Fix plus cross-dialect regression tests, each
  validated to fail without it
  ([#8415](https://github.com/sqlfluff/sqlfluff/pull/8415))

[#8395]: https://github.com/sqlfluff/sqlfluff/pull/8395
- **[sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff)** — `RF06` unquotes
  both halves of a MySQL/MariaDB `'user'@'host'` account specification, which is
  syntax rather than a quoted identifier. `CREATE USER`, `GRANT`, `DROP USER` and
  `DEFINER =` all come back unparsable, on the default rule set
  ([#8462](https://github.com/sqlfluff/sqlfluff/issues/8462))
- **[sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff)** — lint-result
  caching for files that came back clean, so a pre-commit run stops re-parsing
  files nothing touched ([#8418](https://github.com/sqlfluff/sqlfluff/pull/8418))

**Correctness, performance and dead code**

- **[sktime/sktime](https://github.com/sktime/sktime)** — ✅ merged: removed mutable default arguments (B006) from the ConvTimeNet backbones ([#10730](https://github.com/sktime/sktime/pull/10730))
- **[vprusso/toqito](https://github.com/vprusso/toqito)** — ✅ merged: vectorized the depolarizing-channel Kraus-operator construction (dropped the `d²` nested-loop allocations), verified identical output across dims/parameters ([#1921](https://github.com/vprusso/toqito/pull/1921))
- **[Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre)** — ✅ merged: fixed a CLI config-precedence bug so `OPENSRE_INTERACTIVE` and `config.yml` are honored when no `--interactive` flag is given, with a regression test ([#4387](https://github.com/Tracer-Cloud/opensre/pull/4387))
- **[RonaldHensbergen/composable-data-stack](https://github.com/RonaldHensbergen/composable-data-stack)** — ✅ merged: removed an unreachable default-credential security branch (dead code / false coverage) with regression tests ([#344](https://github.com/RonaldHensbergen/composable-data-stack/pull/344), [#345](https://github.com/RonaldHensbergen/composable-data-stack/pull/345))
- **[vedaant00/opendot](https://github.com/vedaant00/opendot)** — ✅ merged: `grep` no longer crashes on paths outside the workspace; `list_files` honors the shared ignore set ([#73](https://github.com/vedaant00/opendot/pull/73), [#61](https://github.com/vedaant00/opendot/pull/61))
- **[masumi-network/Citadel](https://github.com/masumi-network/Citadel)** — ✅ merged: dropped a dead `session_trace` re-export facade, then covered the notification gateways and logging utils ([#130](https://github.com/masumi-network/Citadel/pull/130), [#131](https://github.com/masumi-network/Citadel/pull/131))
- **[skodaconnect/myskoda](https://github.com/skodaconnect/myskoda)** — ✅ merged: added the missing `SoftwareStatus` enum members so updates in progress stop failing to parse ([#641](https://github.com/skodaconnect/myskoda/pull/641))
- **[abduznik/instrumation](https://github.com/abduznik/instrumation)** — ✅ merged: the duplicate-address scanner no longer breaks on empty or `None` input ([#137](https://github.com/abduznik/instrumation/pull/137))
- **[mldsveda/PyScrappy](https://github.com/mldsveda/PyScrappy)** — ✅ merged: aligned the GitHub scraper's default result count with the MCP tool ([#82](https://github.com/mldsveda/PyScrappy/pull/82))
- **[every-app/open-seo](https://github.com/every-app/open-seo)** — a self-hosted container can silently serve a stale client build: the entrypoint fingerprints a hardcoded env list that has to mirror `vite.config.ts`'s `envPrefix`, and only a comment keeps them in sync ([#316](https://github.com/every-app/open-seo/issues/316))

## 🛠 My own projects

| Project | Stack |
|---|---|
| **[autofix-safety](https://github.com/WAHIB-EL-KHADIRI/autofix-safety)** — round-trips a linter's own test corpus through its `--fix` and checks the output still parses. Found data-loss bugs in sqlfluff; found nothing in ruff, and publishes that too. | <sub>Python · `pip install` from git · MIT</sub><br>[![CI](https://github.com/WAHIB-EL-KHADIRI/autofix-safety/actions/workflows/ci.yml/badge.svg)](https://github.com/WAHIB-EL-KHADIRI/autofix-safety/actions/workflows/ci.yml) [![Release](https://img.shields.io/github/v/release/WAHIB-EL-KHADIRI/autofix-safety?style=flat-square&label=release&color=CD7F32)](https://github.com/WAHIB-EL-KHADIRI/autofix-safety/releases) |
| **[AgentOS](https://github.com/WAHIB-EL-KHADIRI/AgentOS)** — runtime for AI agents: supervised lifecycle, gRPC bus, secrets vault, deterministic trace replay. | <sub>Rust · 10-crate workspace · Apache-2.0</sub><br>[![CI](https://github.com/WAHIB-EL-KHADIRI/AgentOS/actions/workflows/ci.yml/badge.svg)](https://github.com/WAHIB-EL-KHADIRI/AgentOS/actions/workflows/ci.yml) [![Release](https://img.shields.io/github/v/release/WAHIB-EL-KHADIRI/AgentOS?include_prereleases&style=flat-square&label=release&color=CD7F32)](https://github.com/WAHIB-EL-KHADIRI/AgentOS/releases) |
| **[AI Content OS](https://github.com/WAHIB-EL-KHADIRI/ai_content_factory)** — 8 specialized agents, a visual workflow engine, and a router that picks the right model per task. | <sub>Python · FastAPI + React</sub><br>[![CI](https://github.com/WAHIB-EL-KHADIRI/ai_content_factory/actions/workflows/ci.yml/badge.svg)](https://github.com/WAHIB-EL-KHADIRI/ai_content_factory/actions/workflows/ci.yml) |
| **[TaskFlow Pro](https://github.com/WAHIB-EL-KHADIRI/taskflow-pro)** — task management on a custom MVC; the domain layer stays free of framework and persistence concerns. | <sub>PHP 8.1 · PSR-12 · PHPStan level 5</sub><br>[![CI](https://github.com/WAHIB-EL-KHADIRI/taskflow-pro/actions/workflows/ci.yml/badge.svg)](https://github.com/WAHIB-EL-KHADIRI/taskflow-pro/actions/workflows/ci.yml) |

## ✍️ Writing

- [I Round-Tripped 2,249 Test Fixtures Through sqlfluff's Auto-Fixer. Eight Came Back Unparsable.](https://dev.to/wahib_el_khadiri_0/i-round-tripped-2249-test-fixtures-through-sqlfluffs-auto-fixer-eight-came-back-unparsable-45le)
  — the method, including the check that found nothing and the finding that stopped reproducing once upstream fixed it.
- [A GitHub Actions tag is a promise, not a fact: pinning by SHA the right way](https://dev.to/wahib_el_khadiri_0/a-github-actions-tag-is-a-promise-not-a-fact-pinning-by-sha-the-right-way-3np)
- [I Read 25 Release Pipelines Looking for One Bug. Four Had It.](https://dev.to/wahib_el_khadiri_0/i-read-25-release-pipelines-looking-for-one-bug-four-had-it-3n9e)
  — the twenty-one that were clean are the point.

## 🧩 Contribute

AgentOS is open to contributors: issues labelled
[`good first issue`](https://github.com/WAHIB-EL-KHADIRI/AgentOS/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
and [`help wanted`](https://github.com/WAHIB-EL-KHADIRI/AgentOS/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
cover Rust internals, CLI ergonomics and docs. Design questions live in
[Discussions](https://github.com/WAHIB-EL-KHADIRI/AgentOS/discussions).

---

<p align="center">
  <b>278</b> commits · <b>165</b> pull requests · <b>21</b> issues ·
  <b>10</b> stars across <b>5</b> projects · <b>4 days</b> streak
</p>

<p align="center">
  <sub>Public contributions, counted 2026-09-16 by
  <a href="https://github.com/WAHIB-EL-KHADIRI/WAHIB-EL-KHADIRI/actions/workflows/readme.yml">a daily Action</a>
  · joined GitHub this year · contributor to 26 repos I don't own</sub>
</p>
