# MIL-004 Docs and Delivery

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [a8ae467] |

---

## Purpose

Decide whether the project is ready to share: screenshots, README, three-language wiki, reflection and the final scan are complete. Branch: `mil-004-docs-and-delivery`.

## Deliverable

One screenshot per build step in the README and the wiki, a wiki in English, Danish and Bahasa Malaysia explaining what was gained in each step, a reflection page, and a final clean scan.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Four screenshots exist, taken in a Docker container, one per build step | Met | Not met |
| 2 | README shows every step with its screenshot and passes `check-readme.sh` | Met | Not met |
| 3 | Every English wiki page has a Danish and a Malay page | Met | Not met |
| 4 | Wiki review against `QC-WIKI-001` is a `Go` | Met | Not met |
| 5 | opengrep scan is clean and no secret or forbidden word is in the tree | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | The screenshots show the finished application |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 4, 5 and 6; success criteria 4, 5 and 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-23 — inside the one-week window of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add Docker setup for screenshots | Add a Dockerfile and script that start the application and a headless browser inside a container, so the host desktop is not used (`framework/process/gui-testing.md`). The browser tooling is not a project dependency. | No |  |
| 2 | Capture one screenshot per build step | Capture four screenshots: the empty editor, typing with the countdown, the warning in the last seconds, and the text gone. Save them under `docs/images/`. | No |  |
| 3 | Complete README with steps and screenshots | Add the build steps with screenshots, the run and test instructions and the link to the wiki to the README. | No |  |
| 4 | Write English wiki pages | Write the wiki pages in English: home, getting started, one page per build step explaining what was gained with its screenshot, and the reflection. | No |  |
| 5 | Write Danish wiki pages | Translate every English wiki page into Danish with the same page set and the language line. | No |  |
| 6 | Write Bahasa Malaysia wiki pages | Translate every English wiki page into Bahasa Malaysia with the same page set and the language line, and add the sidebar listing the three languages. | No |  |
| 7 | Write reflection | Write the reflection: approach, what was hard and easy, improvements, biggest learning and what to do differently. It is a wiki page in all three languages. | No |  |
| 8 | Run final checks before push | Run the tests, the framework checks, the opengrep scan and a search for secrets and forbidden words, then confirm the repository description and topics. | No |  |

---

[BC-001]: ../business-case.md
[a8ae467]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/commit/a8ae4670fbe5ea1e5fe952f7201da04ed809966a
