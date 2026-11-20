# Review of MIL-003

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-032 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-003]
- Checklist used: [QC-PY-001]
- Scope: full review of the code of the milestone
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Names follow PEP 8 casing. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose in plain English. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check .` and `ruff format --check .` pass. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict` passes, so every signature is annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; no swallowed exceptions. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers | N-A | N-A: no files, locks or connections are opened by the code. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules, classes and functions have Doxygen docstrings that say what. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No print and no logging needed; no secrets exist. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | WritingController, WritingViewModel and create_app match DCD-001 and DCD-002; deviation: the page title lives in a module constant `PAGE_TITLE` that `from_constants` uses (the DCD names the literal), and the script also skips polling while a POST is unanswered (race guard beyond the DCD). |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 59 tests including Flask test-client tests with a fake clock for kept, cleared, warning and 400 cases. The browser script is not covered by an automated test; it is checked by the screenshots of MIL-004 taken in a container. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` passes with no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Dependencies are declared in pyproject.toml; none unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Each rule and constant is defined once. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `lint-imports` keeps the contract; only composition_root.py imports infrastructure. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One reason to change per class; ports are narrow. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Presentation package with features/writing, templates and static; tests under unit, integration. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Names are English, no spaces. |

## Overall Verdict

Go — All mandatory criteria pass.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-003]: ../../milestones/mil-003-flask-web-app.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
