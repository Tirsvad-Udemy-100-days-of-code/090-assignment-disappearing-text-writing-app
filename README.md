# 🚀 Disappearing Text Writing App

A small Flask web app for writers who get stuck: type into the page, and if you stop for more than 5 seconds, everything you wrote disappears. It is the Day 90 assignment of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*, built to be read, run and compared by other course participants.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The idea comes from "The Most Dangerous Writing App": a countdown runs while you type, and when it reaches zero the text is deleted. This version keeps the rule in plain Python so it can be tested without a browser, and serves it with Flask.

| Folder | What it holds |
| --- | --- |
| `src/disappearing_text/` | The application: `domain` (the rules), `application` (use cases and ports), `infrastructure` (the clock) and `presentation` (Flask page, routes and script) |
| `tests/` | pytest tests, in `unit/`, `integration/` and `e2e/` |
| `docs/` | The project documents and the wiki pages |
| `scripts/` | Helper scripts, for example the opengrep scan |

The timeout of 5 seconds is the constant `IDLE_TIMEOUT_SECONDS` in `src/disappearing_text/constants.py`.

## 📋 Requirements

- Python 3.13 or newer, because the project targets it.
- Flask, the only runtime dependency, because it serves the page.
- pytest, only for the tests (installed with the `dev` extra).
- Optional: Doxygen to build the API documentation from the source comments, and opengrep to scan the code before a push.

## 🛠️ Setup

Create a local virtual environment named `.venv` in the project folder, activate it, and upgrade pip.

PowerShell on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Bash on Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`. Install only the runtime dependency with `python -m pip install -e .`.

## ▶️ Run

```bash
python -m disappearing_text
```

Open <http://127.0.0.1:5000> in a browser and start typing. Stop for more than 5 seconds and the text is gone.

## 🧪 Tests

```bash
python -m pytest
```

Build the API documentation from the Doxygen comments with `doxygen Doxyfile` (output in `docs/doxygen/`). Scan the code with opengrep before every push:

```powershell
.\scripts\opengrep-scan.ps1
```

## 📄 License

GNU Affero General Public License v3.0, see [LICENSE][license].

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules for automated assistants in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[license]: ./LICENSE
[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
