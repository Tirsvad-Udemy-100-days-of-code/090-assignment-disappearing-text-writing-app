# MIL-002 Core Writing Session

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [a8ae467] |

---

## Purpose

Decide whether the rules of the disappearing text are designed, implemented and tested independent of Flask. Branch: `mil-002-core-writing-session`.

## Deliverable

Use case UC-001 with its Domain Model, System Sequence Diagram, Operation Contract, Sequence Diagram and Design Class Diagram accepted, and the domain, application and infrastructure layers implemented with passing unit tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | UC-001 and its design artifacts are `Accepted` with a `Go` review | Met | Not met |
| 2 | Text is cleared when more than 5 seconds pass without typing (unit test) | Met | Not met |
| 3 | Typing before the timeout keeps the text and restarts the countdown (unit test) | Met | Not met |
| 4 | The domain imports no Flask or system clock | Met | Not met |
| 5 | Code review against `QC-PY-001` is a `Go` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Needs the package skeleton, constants and tooling |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2 and 3; success criteria 1 and 2 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-21 — inside the one-week window of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write use case UC-001 Write without stopping | Write the use case: the writer types, the countdown restarts at every key press, and after more than 5 seconds of silence the text is deleted. Add a wireframe of the single screen with its states. | Yes | UC-001 |
| 2 | Domain Model for UC-001 | Model the concepts of the writing session (session, text, idle timeout) with the PO terms, and add them to the project Domain Model. | Yes | UC-001 |
| 3 | System Sequence Diagram for UC-001 | Show the interaction between the writer and the system: type text, read state, and the timeout event. | Yes | UC-001 |
| 4 | Operation Contract for UC-001 | Specify pre and post conditions of the operations type text and check timeout. | Yes | UC-001 |
| 5 | Sequence Diagram for UC-001 | Design the collaboration for the operations between presentation, use case, session and clock port. | Yes | UC-001 |
| 6 | Design Class Diagram for UC-001 | Design the classes and layer boundaries, then add them to the project Design Class Diagram. | Yes | UC-001 |
| 7 | Implement WritingSession in the domain layer | Implement the session rules with injected time values, test first, and tests for cleared and kept text. Uses the constants. | Yes | UC-001 |
| 8 | Implement use cases and Clock port | Implement the application layer: type text, get state and check timeout, with a Clock port, and tests with a fake clock. | Yes | UC-001 |
| 9 | Implement SystemClock adapter | Implement the infrastructure adapter that reads the system monotonic clock and test it. | No |  |
| 10 | Review core code against Python checklist | Review the code against the Python checklist and record the review. | No |  |

---

[BC-001]: ../business-case.md
[a8ae467]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/commit/a8ae4670fbe5ea1e5fe952f7201da04ed809966a
