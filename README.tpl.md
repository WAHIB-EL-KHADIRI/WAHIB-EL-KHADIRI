<!--
  This file is the SOURCE. README.md is generated from it.

  Edit this file, never README.md -- the daily workflow in
  .github/workflows/readme.yml overwrites README.md on every run.

  Placeholders are filled by scripts/render_readme.py:
    {{YEARS}} {{COMMITS}} {{ISSUES}} {{PRS}} {{STARS}} {{REPOS}}
    {{CONTRIBUTED}} {{STREAK}} {{UPDATED}}
-->
<p align="center">
  <img src="https://raw.githubusercontent.com/WAHIB-EL-KHADIRI/WAHIB-EL-KHADIRI/main/assets/terminal.svg" alt="Terminal: whoami -- AI engineer and systems developer from Morocco, building agent infrastructure in Rust" width="820">
</p>

<p align="center">
  <a href="https://wahib-portfolio.netlify.app/"><img src="https://img.shields.io/badge/Portfolio-2E7D32?style=flat-square&logo=googlechrome&logoColor=white" alt="Portfolio"></a>
  <a href="https://dev.to/wahib_el_khadiri_0"><img src="https://img.shields.io/badge/dev.to-0A0A0A?style=flat-square&logo=devdotto&logoColor=white" alt="dev.to"></a>
  <a href="https://www.linkedin.com/in/wahib-el-khadiri-a54134283"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:wahibelkhadiri06@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
</p>

<p align="center">
  <a href="https://github.com/WAHIB-EL-KHADIRI/AgentOS"><img src="https://img.shields.io/github/stars/WAHIB-EL-KHADIRI/AgentOS?style=for-the-badge&logo=github&label=Star%20AgentOS&color=CD7F32&labelColor=0D1117" alt="Star AgentOS on GitHub"></a>
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

## 🧰 Tech stack & ecosystem

Grouped by **evidence, not aspiration**: the first group appears in my current
repositories and their CI; the second shipped in at least one project; the
third is what I'm learning and don't claim yet. Much of the web work lives in
private client repositories, so not every badge links to public code.

### Technologies I use

<p><b>Languages & Core Technologies</b><br>
  <a href="https://www.rust-lang.org"><img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust"></a>
  <a href="https://www.typescriptlang.org"><img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://developer.mozilla.org/docs/Web/JavaScript"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript"></a>
  <a href="https://www.php.net"><img src="https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white" alt="PHP"></a>
  <a href="https://www.postgresql.org/docs/current/sql.html"><img src="https://img.shields.io/badge/SQL-336791?style=flat-square&logo=postgresql&logoColor=white" alt="SQL"></a>
  <a href="https://www.gnu.org/software/bash/"><img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Bash"></a>
  <a href="https://learn.microsoft.com/powershell/"><img src="https://img.shields.io/badge/PowerShell-5391FE?style=flat-square" alt="PowerShell"></a>
  <a href="https://developer.mozilla.org/docs/Web/HTML"><img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=black" alt="HTML5"></a>
  <a href="https://developer.mozilla.org/docs/Web/CSS"><img src="https://img.shields.io/badge/CSS3-663399?style=flat-square&logo=css&logoColor=white" alt="CSS3"></a>
</p>
<p><b>Frontend Engineering</b><br>
  <a href="https://react.dev"><img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React"></a>
  <a href="https://nextjs.org"><img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js"></a>
  <a href="https://vite.dev"><img src="https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white" alt="Vite"></a>
  <a href="https://tailwindcss.com"><img src="https://img.shields.io/badge/Tailwind%20CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=black" alt="Tailwind CSS"></a>
  <a href="https://tanstack.com/query"><img src="https://img.shields.io/badge/TanStack%20Query-FF4154?style=flat-square&logo=reactquery&logoColor=white" alt="TanStack Query"></a>
  <a href="https://zustand.docs.pmnd.rs"><img src="https://img.shields.io/badge/Zustand-443E38?style=flat-square" alt="Zustand"></a>
  <a href="https://zod.dev"><img src="https://img.shields.io/badge/Zod-408AFF?style=flat-square&logo=zod&logoColor=white" alt="Zod"></a>
  <a href="https://motion.dev"><img src="https://img.shields.io/badge/Framer%20Motion-0055FF?style=flat-square&logo=framer&logoColor=white" alt="Framer Motion"></a>
</p>
<p><b>Backend & Distributed Systems</b><br>
  <a href="https://nodejs.org"><img src="https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js"></a>
  <a href="https://fastapi.tiangolo.com"><img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"></a>
  <a href="https://laravel.com"><img src="https://img.shields.io/badge/Laravel-FF2D20?style=flat-square&logo=laravel&logoColor=white" alt="Laravel"></a>
  <a href="https://tokio.rs"><img src="https://img.shields.io/badge/Tokio-000000?style=flat-square&logo=tokio&logoColor=white" alt="Tokio"></a>
  <a href="https://grpc.io"><img src="https://img.shields.io/badge/gRPC-244C5A?style=flat-square" alt="gRPC"></a>
  <a href="https://www.openapis.org"><img src="https://img.shields.io/badge/REST%20APIs-6BA539?style=flat-square&logo=openapiinitiative&logoColor=white" alt="REST APIs"></a>
</p>
<p><b>Databases & Data Engineering</b><br>
  <a href="https://www.postgresql.org"><img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"></a>
  <a href="https://www.sqlite.org"><img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite"></a>
  <a href="https://redis.io"><img src="https://img.shields.io/badge/Redis-FF4438?style=flat-square&logo=redis&logoColor=white" alt="Redis"></a>
  <a href="https://www.prisma.io"><img src="https://img.shields.io/badge/Prisma-2D3748?style=flat-square&logo=prisma&logoColor=white" alt="Prisma"></a>
</p>
<p><b>Cloud, Infrastructure & DevOps</b><br>
  <a href="https://www.docker.com"><img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"></a>
  <a href="https://docs.docker.com/compose/"><img src="https://img.shields.io/badge/Docker%20Compose-1D63ED?style=flat-square&logo=docker&logoColor=white" alt="Docker Compose"></a>
  <a href="https://kernel.org"><img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux"></a>
  <a href="https://nginx.org"><img src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white" alt="Nginx"></a>
  <a href="https://www.netlify.com"><img src="https://img.shields.io/badge/Netlify-00C7B7?style=flat-square&logo=netlify&logoColor=white" alt="Netlify"></a>
  <a href="https://git-scm.com"><img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git"></a>
  <a href="https://github.com/features/actions"><img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions"></a>
  <a href="https://docs.github.com/code-security/dependabot"><img src="https://img.shields.io/badge/Dependabot-025E8C?style=flat-square&logo=dependabot&logoColor=white" alt="Dependabot"></a>
  <a href="https://pre-commit.com"><img src="https://img.shields.io/badge/pre--commit-FAB040?style=flat-square&logo=precommit&logoColor=black" alt="pre-commit"></a>
</p>
<p><b>Application Security & Supply Chain Security</b><br>
  <a href="https://codeql.github.com"><img src="https://img.shields.io/badge/CodeQL-181717?style=flat-square&logo=github&logoColor=white" alt="CodeQL"></a>
  <a href="https://docs.zizmor.sh"><img src="https://img.shields.io/badge/zizmor-2B2B2B?style=flat-square" alt="zizmor"></a>
  <a href="https://github.com/gitleaks/gitleaks"><img src="https://img.shields.io/badge/Gitleaks-C2185B?style=flat-square" alt="Gitleaks"></a>
  <a href="https://scorecard.dev"><img src="https://img.shields.io/badge/OpenSSF%20Scorecard-0A3D5C?style=flat-square" alt="OpenSSF Scorecard"></a>
  <a href="https://docs.github.com/actions/security-for-github-actions/using-artifact-attestations"><img src="https://img.shields.io/badge/Build%20Provenance%20%28Sigstore%29-2E5C99?style=flat-square" alt="Build Provenance (Sigstore)"></a>
  <a href="https://docs.docker.com/build/metadata/attestations/sbom/"><img src="https://img.shields.io/badge/SBOM-4B5563?style=flat-square" alt="SBOM"></a>
  <a href="https://rustsec.org"><img src="https://img.shields.io/badge/cargo--audit-B7410E?style=flat-square&logo=rust&logoColor=white" alt="cargo-audit"></a>
  <a href="https://embarkstudios.github.io/cargo-deny/"><img src="https://img.shields.io/badge/cargo--deny-8B5E3C?style=flat-square&logo=rust&logoColor=white" alt="cargo-deny"></a>
  <a href="https://sarifweb.azurewebsites.net"><img src="https://img.shields.io/badge/SARIF-374151?style=flat-square" alt="SARIF"></a>
</p>
<p><b>AI Engineering & Autonomous Systems</b><br>
  <a href="https://github.com/WAHIB-EL-KHADIRI/AgentOS"><img src="https://img.shields.io/badge/AI%20Agents-6E40C9?style=flat-square" alt="AI Agents"></a>
  <a href="https://docs.anthropic.com"><img src="https://img.shields.io/badge/Anthropic%20API-191919?style=flat-square&logo=anthropic&logoColor=white" alt="Anthropic API"></a>
  <a href="https://platform.openai.com/docs"><img src="https://img.shields.io/badge/OpenAI%20API-412991?style=flat-square" alt="OpenAI API"></a>
</p>
<p><b>Testing, Reliability & Code Quality</b><br>
  <a href="https://pytest.org"><img src="https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white" alt="Pytest"></a>
  <a href="https://vitest.dev"><img src="https://img.shields.io/badge/Vitest-6E9F18?style=flat-square&logo=vitest&logoColor=white" alt="Vitest"></a>
  <a href="https://playwright.dev"><img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square" alt="Playwright"></a>
  <a href="https://phpunit.de"><img src="https://img.shields.io/badge/PHPUnit-3C9CD7?style=flat-square" alt="PHPUnit"></a>
  <a href="https://doc.rust-lang.org/cargo/commands/cargo-test.html"><img src="https://img.shields.io/badge/cargo%20test-000000?style=flat-square&logo=rust&logoColor=white" alt="cargo test"></a>
  <a href="https://docs.astral.sh/ruff/"><img src="https://img.shields.io/badge/Ruff-D7FF64?style=flat-square&logo=ruff&logoColor=black" alt="Ruff"></a>
  <a href="https://mypy-lang.org"><img src="https://img.shields.io/badge/mypy-2A6DB2?style=flat-square&logo=python&logoColor=white" alt="mypy"></a>
  <a href="https://phpstan.org"><img src="https://img.shields.io/badge/PHPStan-4F5B93?style=flat-square" alt="PHPStan"></a>
  <a href="https://eslint.org"><img src="https://img.shields.io/badge/ESLint-4B32C3?style=flat-square&logo=eslint&logoColor=white" alt="ESLint"></a>
  <a href="https://prettier.io"><img src="https://img.shields.io/badge/Prettier-1A2C34?style=flat-square&logo=prettier&logoColor=white" alt="Prettier"></a>
</p>
<p><b>Developer Tools & Workflow</b><br>
  <a href="https://code.visualstudio.com"><img src="https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square" alt="VS Code"></a>
  <a href="https://github.com"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="https://docs.anthropic.com/claude-code"><img src="https://img.shields.io/badge/Claude%20Code-D97757?style=flat-square&logo=claude&logoColor=white" alt="Claude Code"></a>
  <a href="https://docs.astral.sh/uv/"><img src="https://img.shields.io/badge/uv-DE5FE9?style=flat-square&logo=uv&logoColor=white" alt="uv"></a>
  <a href="https://commonmark.org"><img src="https://img.shields.io/badge/Markdown-000000?style=flat-square&logo=markdown&logoColor=white" alt="Markdown"></a>
</p>

### Technologies I have worked with

<p><b>Languages & Frameworks</b><br>
  <a href="https://expressjs.com"><img src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white" alt="Express"></a>
  <a href="https://fastify.dev"><img src="https://img.shields.io/badge/Fastify-000000?style=flat-square&logo=fastify&logoColor=white" alt="Fastify"></a>
  <a href="https://developer.mozilla.org/docs/Web/API/WebSockets_API"><img src="https://img.shields.io/badge/WebSockets-010101?style=flat-square" alt="WebSockets"></a>
  <a href="https://jwt.io"><img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" alt="JWT"></a>
  <a href="https://www.electronjs.org"><img src="https://img.shields.io/badge/Electron-47848F?style=flat-square&logo=electron&logoColor=white" alt="Electron"></a>
  <a href="https://doc.qt.io/qtforpython-6/"><img src="https://img.shields.io/badge/Qt%20%28PySide6%29-41CD52?style=flat-square&logo=qt&logoColor=white" alt="Qt (PySide6)"></a>
  <a href="https://webassembly.org"><img src="https://img.shields.io/badge/WebAssembly-654FF0?style=flat-square&logo=webassembly&logoColor=white" alt="WebAssembly"></a>
</p>
<p><b>Data & Persistence</b><br>
  <a href="https://www.sqlalchemy.org"><img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy"></a>
  <a href="https://docs.pydantic.dev"><img src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white" alt="Pydantic"></a>
  <a href="https://www.mongodb.com"><img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" alt="MongoDB"></a>
  <a href="https://pandas.pydata.org"><img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="pandas"></a>
  <a href="https://numpy.org"><img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy"></a>
  <a href="https://scikit-learn.org"><img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn"></a>
</p>
<p><b>Platforms & Automation</b><br>
  <a href="https://vercel.com"><img src="https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white" alt="Vercel"></a>
  <a href="https://pptr.dev"><img src="https://img.shields.io/badge/Puppeteer-40B5A4?style=flat-square&logo=puppeteer&logoColor=white" alt="Puppeteer"></a>
  <a href="https://scapy.net"><img src="https://img.shields.io/badge/Scapy-2F4F4F?style=flat-square" alt="Scapy"></a>
</p>

### Technologies I'm exploring

<p>
  <a href="https://pytorch.org"><img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch"></a>
  <a href="https://www.tensorflow.org"><img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" alt="TensorFlow"></a>
  <a href="https://modelcontextprotocol.io"><img src="https://img.shields.io/badge/Model%20Context%20Protocol-000000?style=flat-square&logo=modelcontextprotocol&logoColor=white" alt="Model Context Protocol"></a>
  <a href="https://en.wikipedia.org/wiki/Vector_database"><img src="https://img.shields.io/badge/Vector%20Databases-5A4FCF?style=flat-square" alt="Vector Databases"></a>
</p>

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

- **[sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff)** — `fix` could weld
  adjacent tokens together, so the file it writes lexes differently from the one
  it read: in Oracle, two *keywords* — `MULTISET EXCEPT` → `MULTISETEXCEPT` —
  fused by `LT01`. Upstream fixed the arithmetic case I led with ([#8395]), which
  made my opening example stale. **Closed unmerged**, and the reason was
  reviewability rather than correctness — too verbose, and missing a real-world
  query as the motivating test. Worth recording as written
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
  <b>{{UPSTREAM_PRS}}</b> pull requests into repositories I don't own —
  <b>{{UPSTREAM_MERGED}}</b> merged · <b>{{UPSTREAM_OPEN}}</b> open · <b>{{UPSTREAM_CLOSED}}</b> closed
</p>

<p align="center">
  <b>{{COMMITS}}</b> commits · <b>{{ISSUES}}</b> issues · <b>{{STARS}}</b> stars across <b>{{REPOS}}</b> projects
</p>

<p align="center">
  <sub>Public contributions, counted {{UPDATED}} by
  <a href="https://github.com/WAHIB-EL-KHADIRI/WAHIB-EL-KHADIRI/actions/workflows/readme.yml">a daily Action</a>
  · contributor to {{CONTRIBUTED}} repos I don't own</sub>
</p>
