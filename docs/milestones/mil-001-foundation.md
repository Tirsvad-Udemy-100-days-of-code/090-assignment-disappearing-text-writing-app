# MIL-001 Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the repository is ready for feature work: tooling, configuration, documentation baseline and repository metadata exist, and the static scan is clean. Branch: `mil-001-foundation`.

## Deliverable

A repository with `pyproject.toml`, a Python `.gitignore`, an `.editorconfig`, `constants.py`, a `Doxyfile`, a README built from the framework template with venv instructions, an opengrep scan script, recorded ADRs, and a repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` requires Python 3.13 or newer and lists Flask as the only runtime dependency | Met | Not met |
| 2 | `python -m pytest` runs and passes in a fresh `.venv` | Met | Not met |
| 3 | `bash framework/scripts/check-readme.sh` and `check-editorconfig.sh` pass | Met | Not met |
| 4 | opengrep scan reports no open finding | Met | Not met |
| 5 | Repository description and topics are set on the git host | Met | Not met |
| 6 | `.env` is ignored and no secret is in the tree | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First phase |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 4 and 6; success criteria 2, 3 and 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-20 — inside the one-week window of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Set the description and topics of the repository through the host's API, using the repository token from the local `.env` of the Product Owner. The `.env` is only used by the shell for this call and is never read or imported by the project. Serves S03 (CN-007). | No |  |
| 2 | Add pyproject.toml | Configure the project: Python 3.13 or newer, Flask as the only runtime dependency, pytest as a `dev` extra, pytest paths and the package under `src/`. Serves CN-008. | No |  |
| 3 | Add Python .gitignore and editorconfig | Add a Python `.gitignore` that also ignores `.env`, `.venv`, caches and generated Doxygen output, and a root `.editorconfig` made from the framework baseline (AGENTS rule 10). | No |  |
| 4 | Create package skeleton with constants.py | Create the `src/` and `tests/` layout from the clean-architecture skill and `constants.py` holding the idle timeout of 5 seconds and other fixed values. Add a first test that imports the constants. | No |  |
| 5 | Add Doxyfile and Doxygen comment convention | Add a `Doxyfile` configured for Python sources in `src/` and document the Doxygen comment style used in the source, so the code is readable for S02 (CN-004). | No |  |
| 6 | Document venv setup in README | Write the README from the framework template, with how to create and use a local `.venv`, upgrade pip with `python -m pip install --upgrade pip`, install the project, run the application and run the tests (CN-005). | No |  |
| 7 | Add opengrep scan script and rules | Add a local scan script that runs opengrep from `~\.opengrep\cli\latest\opengrep.exe` over `src/` and `tests/` with a small rule file, and document that it runs before every push. | No |  |
| 8 | Record ADRs for skipped analysis documents and Flask | Record in ADRs why KPI, Business Model Canvas and BPMN are skipped for a one-assignment project and why Flask is the single runtime dependency with a server-side timer. Each ADR is reviewed. | No |  |
| 9 | Enable local git hooks and plan gate | Install the framework git hooks and the plan gate in this clone so commits on `main` and code outside an accepted milestone are refused. | No |  |

---

[BC-001]: ../business-case.md
