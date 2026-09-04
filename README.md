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

## 💼 Available for work

Open to remote and contract work in DevSecOps, software supply-chain security,
and AI-agent infrastructure. Based in Morocco, across EMEA and US-morning hours.

[wahibelkhadiri06@gmail.com](mailto:wahibelkhadiri06@gmail.com)
· [LinkedIn](https://www.linkedin.com/in/wahib-el-khadiri-a54134283)

## 🔒 Work in other people's repositories

**14 merged pull requests into 11 repositories I don't own**, reviewed and
accepted by their maintainers. The through-line is release-pipeline security:
`${{ ... }}` is pasted into a shell as text before bash parses it, so a tag name
or dispatch input stops being data and becomes part of the program — almost
always in the one job holding the publishing credentials.

**Release-pipeline hardening**

- **[PrefectHQ/prefect](https://github.com/PrefectHQ/prefect)** — ✅ merged: the release ref was expanded into two shell bodies in the jobs that publish to PyPI, one of them holding `id-token: write` for Trusted Publishing ([#22882](https://github.com/PrefectHQ/prefect/pull/22882))
- **[thingctx/thingctx](https://github.com/thingctx/thingctx)** — ✅ merged: pinned every third-party GitHub Action to a commit SHA across CI and release workflows ([#127](https://github.com/thingctx/thingctx/pull/127))
- **[dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)** — the workflow that publishes to GitHub, PyPI and Docker: dispatch inputs expanded unquoted into an `echo` and into a command substitution ([#15994](https://github.com/dbt-labs/dbt-core/pull/15994))
- **[sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff)** — release workflow: the version input reached a command substitution and a step carrying `GITHUB_TOKEN` ([#8375](https://github.com/sqlfluff/sqlfluff/pull/8375))
- **[sktime/pytorch-forecasting](https://github.com/sktime/pytorch-forecasting)** — PyPI release workflow: tag name expanded into the tag check that gates the build, plus a least-privilege `permissions:` block the file had never declared ([#2385](https://github.com/sktime/pytorch-forecasting/pull/2385))

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
- **[every-app/open-seo](https://github.com/every-app/open-seo)** — agent-readiness audits: AI crawler directives, `llms.txt`, Markdown alternates ([#122](https://github.com/every-app/open-seo/pull/122))

## 🛠 My own projects

| Project | Stack |
|---|---|
| **[AgentOS](https://github.com/WAHIB-EL-KHADIRI/AgentOS)** — runtime for AI agents: supervised lifecycle, gRPC bus, secrets vault, deterministic trace replay. | <sub>Rust · 10-crate workspace · MIT/Apache-2.0</sub><br>[![CI](https://github.com/WAHIB-EL-KHADIRI/AgentOS/actions/workflows/ci.yml/badge.svg)](https://github.com/WAHIB-EL-KHADIRI/AgentOS/actions/workflows/ci.yml) [![Release](https://img.shields.io/github/v/release/WAHIB-EL-KHADIRI/AgentOS?include_prereleases&style=flat-square&label=release&color=CD7F32)](https://github.com/WAHIB-EL-KHADIRI/AgentOS/releases) |
| **[AI Content OS](https://github.com/WAHIB-EL-KHADIRI/ai_content_factory)** — 8 specialized agents, a visual workflow engine, and a router that picks the right model per task. | <sub>Python · FastAPI + React</sub><br>[![CI](https://github.com/WAHIB-EL-KHADIRI/ai_content_factory/actions/workflows/ci.yml/badge.svg)](https://github.com/WAHIB-EL-KHADIRI/ai_content_factory/actions/workflows/ci.yml) |
| **[TaskFlow Pro](https://github.com/WAHIB-EL-KHADIRI/taskflow-pro)** — task management on a custom MVC; the domain layer stays free of framework and persistence concerns. | <sub>PHP 8.1 · PSR-12 · PHPStan 5</sub><br>[![CI](https://github.com/WAHIB-EL-KHADIRI/taskflow-pro/actions/workflows/ci.yml/badge.svg)](https://github.com/WAHIB-EL-KHADIRI/taskflow-pro/actions/workflows/ci.yml) |

## ✍️ Writing

- [I Shipped My First Rust Release, and CI Turned Red Twice in 20 Minutes](https://dev.to/wahib_el_khadiri_0/i-shipped-my-first-rust-release-and-ci-turned-red-twice-in-20-minutes-31hp)
- [I Taught an Open-Source SEO Tool to Check Whether Your Site Is Readable by AI Agents](https://dev.to/wahib_el_khadiri_0/i-taught-an-open-source-seo-tool-to-check-whether-your-site-is-readable-by-ai-agents-15i3)

## 🧩 Contribute

AgentOS is open to contributors: issues labelled
[`good first issue`](https://github.com/WAHIB-EL-KHADIRI/AgentOS/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
and [`help wanted`](https://github.com/WAHIB-EL-KHADIRI/AgentOS/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
cover Rust internals, CLI ergonomics and docs. Design questions live in
[Discussions](https://github.com/WAHIB-EL-KHADIRI/AgentOS/discussions).

---

<p align="center">
  <b>217</b> commits · <b>110</b> pull requests · <b>12</b> issues ·
  <b>7</b> stars across <b>4</b> projects · <b>0 days</b> streak
</p>

<p align="center">
  <sub>Public contributions, counted 2026-09-04 by
  <a href="https://github.com/WAHIB-EL-KHADIRI/WAHIB-EL-KHADIRI/actions/workflows/readme.yml">a daily Action</a>
  · joined GitHub this year · contributor to 25 repos I don't own</sub>
</p>
