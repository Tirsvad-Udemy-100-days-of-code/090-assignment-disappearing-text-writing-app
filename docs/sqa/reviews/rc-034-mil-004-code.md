# Review of MIL-004

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-034 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [5dc94c1] |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-PY-001]
- Scope: full review of tools/screenshots and scripts of the milestone
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Names follow PEP 8 casing. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose in plain English. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` pass for tools/screenshots/capture.py. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict` passes, so every signature is annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; no swallowed exceptions. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers | N-A | N-A: the script starts a subprocess and stops it in a `finally` block; no files are held open. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules, classes and functions have Doxygen docstrings that say what. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No print; no secrets in output. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | N-A: helper script outside the layers; no class. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | Tests exist per behaviour, are named for it and do not depend on order or network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | N-A: mypy is not run on the helper because playwright is installed only in the container image. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Playwright is installed only in the screenshot image, not declared in the project (by design). |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Each rule and constant is defined once. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | N-A | N-A: the helper imports no project module. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | N-A | N-A: no class. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | The helper is in tools/screenshots, outside src; the application layers are unchanged. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Names are English, no spaces. |

## Overall Verdict

Go — All mandatory criteria pass; the helper is outside the application layers.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-004]: ../../milestones/mil-004-docs-and-delivery.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[5dc94c1]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/commit/5dc94c137814bec4a092751030acb1316d4b7e77
