# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

This analysis names the people who use or judge the project, rates their power
and interest, and records what each needs, so later artifacts cite stakeholder
IDs. It follows the power/interest grid and maps concerns to FURPS+.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer and reviewer | Tirsvad (Udemy course participant) | HIGH | HIGH | Manage Closely | Finish the assignment with a clean, tested, documented result and a useful reflection |
| S02 | Udemy coursists | Course participants who share code and compare solutions | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public on GitHub | LOW | MEDIUM | Monitor | A clear repository description, topics and README, and no runtime dependencies beyond what is needed |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews every artifact and accepts the plan.
- **Keep Informed (S02):** cannot change the project but depends on the quality of
  the code and the README, so they get the documentation and the wiki.
- **Monitor (S03):** casual visitors; a good description, topics and README are
  enough. Their interest rises if the repository is clear.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Text must disappear after more than 5 seconds without typing | Functionality |
| CN-002 | S01 | Work follows the plan-first process with reviewed artifacts | Supportability |
| CN-003 | S01 | Tests protect the session rules | Reliability |
| CN-004 | S02 | Code is readable and uses the assignment's function names | Supportability |
| CN-005 | S02 | README explains how to create a venv and run the app and tests | Usability |
| CN-006 | S02 | Each build step is explained with a screenshot and what was gained, in English, Danish and Bahasa Malaysia | Usability |
| CN-007 | S03 | Repository has a description, topics and a clear README | Usability |
| CN-008 | S03 | No runtime dependencies beyond the necessary one | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| C-001 | Chat with S01 | Once per run | Accepted plan; final summary of pull requests, reviews and stand-in decisions | All milestones |
| C-002 | Pull request on the git host | One per milestone | Reviewed change | All milestones |
| C-003 | README and wiki | Once, at delivery | Instructions, screenshots, lessons learned | MIL-004 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S03 wants no runtime dependencies, but the assignment requires Flask | S01, S03 | Flask is the single runtime dependency and is stated in the README; pytest is a development extra only |
| S02 wants the assignment's function names, but clean layering suggests other names | S01, S02 | Function names from the assignment's wording are kept in the core and the routes, and the layering is kept around them |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-003 | [BC-001] objectives 1, 2 and 3 |
| S01 | CN-002 | [BC-001] objective 3 and constraints |
| S02 | CN-004, CN-005 | [BC-001] objective 4 |
| S02 | CN-006 | [BC-001] objective 5 |
| S03 | CN-007, CN-008 | [BC-001] objectives 4 and 6 |

## Sign-Off

Pending the review of S01.

---

[BC-001]: ./business-case.md
