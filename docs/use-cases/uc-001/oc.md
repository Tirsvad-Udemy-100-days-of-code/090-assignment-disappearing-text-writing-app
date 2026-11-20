# Operation Contracts for UC-001

## Metadata
| Key | Value |
| --- | --- |
| ID | OC-001 |
| CrossReference | [SSD-001], [DM-001], [SD-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [99eebd6] |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Added the CrossReference to SD-001, now that it exists | [99eebd6] |

---

Terms: the contracts use the terms of the Domain Model [DM-001]. The IT terms equal the PO terms (English, IT domain), so no dictionary exists. The current moment is the time at which the operation runs. The Idle Timeout has length 5 seconds and warning period 2 seconds.

## Contract: type_text

| Item | Value |
| --- | --- |
| Operation | `type_text(text: str): None` |
| Traces to | `type_text` (steps 2, 4 and 7 of the System Operations table) in [SSD-001] |
| Domain Model concepts | Writing Session, Text, Idle Timeout; associations holds and ends after ([DM-001]) |

**Preconditions**

- A Writing Session exists, and it holds a Text and is associated with an Idle Timeout.
- `text` is the whole Text as the Writer has it now. It may be empty.

**Postconditions**

- Text.words was set to `text`.
- WritingSession.last typing moment was set to the current moment.
- WritingSession.text lost was set to false.
- No instance was created or deleted, and the association to the Idle Timeout is unchanged.

**Exceptions**

| Condition (failing precondition) | Outcome |
| --- | --- |
| `text` is not text (precondition on `text` fails) | The operation is rejected with an error; Text, last typing moment and text lost keep their values |

## Contract: get_state

This contract includes the check of the Idle Timeout (`check_timeout`). The check is not a system operation of its own, because the Writer never sends it; it runs as the first part of every `get_state`.

| Item | Value |
| --- | --- |
| Operation | `get_state(): WritingState` |
| Traces to | `get_state` (steps 1, 3, 5 and 6 of the System Operations table) in [SSD-001] |
| Domain Model concepts | Writing Session, Text, Idle Timeout; associations holds and ends after ([DM-001]) |

**Preconditions**

- A Writing Session exists, and it holds a Text and is associated with an Idle Timeout.

**Postconditions**

- When Text.words is not empty and the seconds from WritingSession.last typing moment to the current moment are more than Idle Timeout.length in seconds: Text.words was set to empty and WritingSession.text lost was set to true.
- When exactly Idle Timeout.length in seconds have passed, or fewer, nothing was changed; the Text is kept.
- When Text.words is empty, nothing was changed.
- The returned WritingState describes the Writing Session after the check:
  - `text` equals Text.words;
  - `seconds_left` is Idle Timeout.length in seconds minus the seconds since last typing moment, never below zero, and is none when Text.words is empty;
  - `is_warning` is true when Text.words is not empty and `seconds_left` is at most Idle Timeout.warning period in seconds, and false otherwise;
  - `was_cleared` equals WritingSession.text lost.
- No instance was created or deleted.

**Exceptions**

| Condition (failing precondition) | Outcome |
| --- | --- |
| The Writing Session does not exist | Not possible: the system creates the Writing Session when it starts, before it accepts a message, so no failing precondition has to be handled |

---

[SSD-001]: ./ssd.md
[DM-001]: ./dm.md
[SD-001]: ./sd.md
[99eebd6]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/commit/99eebd69b73173ca68a4d9676c39855a30cdf1b9
