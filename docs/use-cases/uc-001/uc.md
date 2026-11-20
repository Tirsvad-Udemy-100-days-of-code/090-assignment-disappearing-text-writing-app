# UC-001 Write without stopping

## Metadata
| Key | Value |
| --- | --- |
| ID | UC-001 |
| CrossReference | [US-001], [SA-001], [BC-001], [DM-001], [SSD-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Added the CrossReference to DM-001 and SSD-001, now that they exist | pending |

---

**Format:** Fully Dressed

The screen of this use case, with its states, is drawn in `wireframe.md` in this folder.

## Fully Dressed

- **Scope:** The writing application (the system under design).
- **Level:** user-goal
- **Primary Actor:** Writer (stakeholder S01 in [SA-001])
- **Stories:** US-001.01 and US-001.02 in [US-001]
- **Stakeholders and Interests:**
  - S01 — Wants to be forced to keep writing, and to see how long is left before the text disappears.
  - S02 — Wants the rule that deletes the text to be easy to read and to check with automated tests.
- **Preconditions:** The system is running and the Writer can reach it. No text is in the Writing Session, or the Writer has just opened the application.
- **Postconditions (success guarantee):** The Writing Session holds exactly the Text the Writer typed last. When the Writer stopped typing for more than the Idle Timeout, the Text is empty and the Writer has been told that it is gone. No Text is kept anywhere else.

### Main Success Scenario

1. The Writer opens the application.
2. The system shows an empty Text and no Countdown.
3. The Writer types Text.
4. The system keeps the Text and starts the Countdown at the Idle Timeout.
5. The system shows the seconds left of the Countdown.
6. The Writer changes the Text before the Countdown ends.
7. The system keeps the new Text and restarts the Countdown at the Idle Timeout.
8. When the Countdown is in the last 2 seconds, the system shows a Warning.
9. The Writer keeps typing, and steps 6 to 8 repeat until the Writer is done.

### Extensions (Alternative / Exception Flows)

- 6a. The Writer stops typing for more than the Idle Timeout:
  1. The system deletes all of the Text.
  2. The system shows that the Text is gone and shows no Countdown.
  3. The Writer types again.
  4. The system starts a new Text with what the Writer typed, and the use case continues at step 4.
- 6b. The Writer deletes all of the Text by hand:
  1. The system keeps the empty Text and stops the Countdown.
  2. The system shows no Countdown and does not say that Text is gone, because the Writer removed it.
  3. The Writer types again and the use case continues at step 4.

No other use case is included or extended (`<<include>>` and `<<extend>>` are not used).

### Special Requirements / Business Rules

| Step | Rule |
| --- | --- |
| 4 | The Idle Timeout is 5 seconds and is defined once, so that it can change without changing the rules |
| 4, 7 | The Countdown runs only while the Text is not empty |
| 7 | Every change of the Text restarts the Countdown at the Idle Timeout |
| 8 | A Warning is shown while the Text is not empty and 2 seconds or less are left |
| 6a.1 | Text is deleted only when more than 5 seconds have passed since the last change; exactly 5 seconds does not delete |
| 6a.2 | After a deletion the session stays in the expired state, and the Writer is told that the Text is gone, until the Writer types again |

### Open Issues

- The application serves one Writer at a time, so a second Writer would share the same Text; this is accepted for a local application in [BC-001] and the design decision is recorded in ADR-0002.

---

[US-001]: ../../user-stories.md
[SA-001]: ../../stakeholder-analysis.md
[BC-001]: ../../business-case.md
[DM-001]: ./dm.md
[SSD-001]: ./ssd.md
