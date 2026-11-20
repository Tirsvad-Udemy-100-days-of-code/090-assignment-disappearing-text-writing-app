# MIL-003 Flask Web App

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [a8ae467] |

---

## Purpose

Decide whether the writer can use the application in a browser: Flask serves the page and the state, and the page shows the countdown and the disappearing text. Branch: `mil-003-flask-web-app`.

## Deliverable

A Flask application started from the package, an editor page with a countdown, a small JSON interface, integration tests with the Flask test client, and run instructions.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m disappearing_text` serves the editor page on localhost | Met | Not met |
| 2 | The page shows a countdown that restarts at every key press | Met | Not met |
| 3 | After more than 5 seconds idle the server clears the text and the page shows it empty | Met | Not met |
| 4 | Integration tests pass and Flask stays the only runtime dependency | Met | Not met |
| 5 | Code review against `QC-PY-001` is a `Go` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The web layer calls the use cases of the core |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 and 4; success criteria 1, 2 and 3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-22 — inside the one-week window of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add Flask app factory and composition root | Create the Flask application factory that builds the use cases with the system clock, and the entry point for `python -m disappearing_text`. | Yes | UC-001 |
| 2 | Add state and text routes | Add controllers: read the session state with the remaining seconds, and send the current text. Map requests and responses to plain data. | Yes | UC-001 |
| 3 | Add editor page and view model | Add the Jinja template for the single screen from the wireframe, with a view model holding the data the page shows. | Yes | UC-001 |
| 4 | Add browser script for typing and countdown | Write the small script that sends the text on input, polls the state and shows the countdown, a warning in the last seconds and the empty state. | Yes | UC-001 |
| 5 | Add integration tests with the Flask test client | Test the routes and the page with a fake clock for the cases kept and cleared. | No |  |
| 6 | Document how to run the application | Describe running the app and opening it in the browser, in the README. | No |  |
| 7 | Review web code against Python checklist | Review the web layer against the Python checklist and record the review. | No |  |

---

[BC-001]: ../business-case.md
[a8ae467]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/commit/a8ae4670fbe5ea1e5fe952f7201da04ed809966a
