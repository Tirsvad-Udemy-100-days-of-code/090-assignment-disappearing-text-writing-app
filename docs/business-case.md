# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [a8ae467] |

---

## Executive Summary

Writers often stall in front of a blank page. This project builds a small web
application, served locally with Flask, in which the writer types into one text
area and every word is lost if no key is pressed for five seconds. The pressure
to keep going is the point: it pushes the writer past the inner critic. The
application is the solution to the Udemy "100 Days of Code" Day 90 assignment
and is published as a readable, runnable example for other course participants.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/`: Business
Case, Stakeholder Analysis, Project Plan, milestones, tasks as issues, then code,
each step reviewed before the next. Design follows Larman's *Applying UML and
Patterns* (use case, domain model, system sequence diagram, operation contract,
sequence diagram, design class diagram). Quality characteristics are those of
ISO/IEC 25010:2023. Code follows the Python conventions of the framework and is
checked with pytest and a static scan with opengrep before every push.

## Problem Statement

- A writer facing a blank page cannot start, and editing while writing breaks
  the flow of thought.
- Course participants need a small, complete Flask example that shows timers,
  state held on a server and a page that reacts to it, and they find few that are
  readable and documented step by step.

## Business Opportunity

A finished, documented example lets the Product Owner complete the assignment,
reflect on the work and share it. Course participants get a solution to compare
with their own, and repository visitors get ideas for a small Flask project.

## Objectives

1. Deliver a Flask application where typed text is deleted after more than five
   seconds without typing.
2. Keep the timeout in one constant, so it can change without touching logic.
3. Cover the rules of the writing session with automated pytest tests.
4. Document how to create and use a local virtual environment, run the
   application and run the tests.
5. Document each build step in the README and in a wiki in English, Danish and
   Bahasa Malaysia, each step with a screenshot and a note on what was learned.
6. Publish the repository with a description and topics.

## Scope

### In Scope

- A single-page writing application served by Flask on the local machine.
- A countdown that shows the time left before the text disappears.
- A pure Python core for the writing session rules, independent of Flask.
- Tests, `pyproject.toml`, Python `.gitignore`, `constants.py`, Doxygen comments
  and a `Doxyfile`.
- README from the framework template, and a three-language wiki.
- One screenshot per build step.
- A static scan with opengrep before each push.

### Out of Scope

- User accounts, saving, export or any database.
- Deployment to a public server, and multi-user sessions.
- Mobile layout beyond what a responsive page gives for free.
- Any runtime dependency beyond Flask.

## Expected Benefits

### Tangible Benefits

- A completed assignment with tests and documentation.
- A reusable, documented example repository in three wiki languages.

### Intangible Benefits

- Practice with Flask, timers and clean separation of rules from the web layer.
- A written reflection that improves the next project.

## Strategic Alignment

The project supports the course goal of building one portfolio project per day,
and the Product Owner's habit of working plan first with reviewed artifacts.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Text disappears after inactivity | Cleared when more than 5 s pass without typing | Automated test of the session rules, manual check on screenshots |
| 2 | Tests | All pytest tests pass on Python 3.13 or newer | `python -m pytest` exit code 0 |
| 3 | Runtime dependencies | Flask only | `pyproject.toml` `dependencies` list |
| 4 | Documentation | README and 3 wiki languages complete | Every English page has a Danish and a Malay page |
| 5 | Screenshots | One per build step in README and wiki | Count of images per step is 1 or more |
| 6 | Static scan | No findings left open before push | opengrep exit code and report |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Browser and server clocks drift, so the countdown looks wrong | Medium | The server decides when text is deleted; the browser only displays the remaining time reported by the server |
| Screenshots taken on the host desktop take over the Product Owner's mouse and keyboard | Medium | Take screenshots inside a Docker container as `framework/process/gui-testing.md` requires |
| Secrets in `.env` end up in the repository | High | `.env` is ignored, never imported or tested by the project, and scanned for before each push |
| Translations drift from English | Low | English is authoritative; every page exists in all three languages and is reviewed as a set |
| Scope creep into saving or accounts | Low | Out of Scope list; a change needs a plan change |

## Assumptions

- The Product Owner has Python 3.13 or newer and a Docker engine available.
- The Gitea repository exists and tokens are available in a local `.env` used
  only by the Product Owner's tooling.
- The Product Owner is the reviewer; a reviewer who is a stakeholder other than
  the Product Owner is replaced by a stand-in marked as not independent.
- The people the idea is for can be reached only by the Product Owner.

## Constraints

- Python 3.13 or newer, with a local `venv`.
- Flask for the web layer; pytest for tests; constants in `constants.py`.
- Folders `src/`, `tests/` and `docs/`.
- Doxygen comments in source and a `Doxyfile`.
- The word for artificial intelligence is not written in any artifact or file of
  the repository.
- One branch and pull request per milestone.

## Cost–Benefit Assessment

The assessment is qualitative on purpose: no money flows, so there is no return on investment to compute; the only cost is the time of S01.

| Costs | Benefits |
| --- | --- |
| About 150 minutes of build time as set by the course, plus documentation time | Completed assignment, reusable example, three-language wiki |
| No licence or hosting cost | Practice that carries over to later projects |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Completes the assignment and reflects; owns scope and reviews |
| S02 | Reads, runs and compares the code |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — the scope is small, the risks have mitigations and the result serves all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[a8ae467]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/commit/a8ae4670fbe5ea1e5fe952f7201da04ed809966a
