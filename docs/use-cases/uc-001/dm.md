# Domain Model for UC-001

## Metadata
| Key | Value |
| --- | --- |
| ID | DM-001 |
| CrossReference | [UC-001], [SA-001], [SSD-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Added the CrossReference to SSD-001, now that it exists | pending |

---

## Purpose and Scope

Covers UC-001 (Write without stopping). The model answers concern CN-001 (text must disappear after more than 5 seconds without typing) and supports CN-003 (tests protect the rules) of [SA-001], and serves S01, the Writer, and S02, who reads the rules. No project Domain Model exists yet, so every concept here is new; after acceptance the concepts are added to the project Domain Model.

Two terms of the use case are deliberately not concepts. The seconds left (the Countdown) is worked out from the last typing moment and the Idle Timeout, so it is not stored data. The Warning is how the system tells the Writer that the end is near; it is a part of the screen and first appears in the Operation Contract, the Sequence Diagram and the Design Class Diagram. What the Warning depends on, the warning period, is an attribute of Idle Timeout.

## Diagram

Concepts, attributes and associations only — no operations.

```plantuml
@startuml
hide methods
class "Writing Session" as WritingSession {
  last typing moment
  text lost
}
class Text {
  words
}
class "Idle Timeout" as IdleTimeout {
  length in seconds
  warning period in seconds
}
WritingSession "1" --> "1" Text : holds
WritingSession "0..*" --> "1" IdleTimeout : ends after
@enduml
```

## Concept Table

| Concept | Definition | Attributes | Source (use case / glossary) |
| --- | --- | --- | --- |
| Writing Session | One stretch of writing, from the first words the Writer types until the Writer is done or the words are lost. | last typing moment (when the Writer last changed the Text); text lost (whether the Text was lost because the Writer stopped for too long) | UC-001 "Writer opens the application", "Writer keeps typing", "Writer stops typing" |
| Text | The words the Writer has written so far. | words | UC-001 "Text", "types Text", "deletes all of the Text" |
| Idle Timeout | How long the Writer may go without typing before the words are lost, and how near the end the Writer is warned. | length in seconds (5); warning period in seconds (2, the last seconds before the end) | UC-001 "Idle Timeout", "Warning", business rules of steps 4 and 8 |

## Association Table

| From | Association (reading direction) | To | Multiplicity |
| --- | --- | --- | --- |
| Writing Session | holds (a Writing Session holds its Text) | Text | 1 at the Writing Session end, 1 at the Text end |
| Writing Session | ends after (a Writing Session ends after an Idle Timeout) | Idle Timeout | 0..* at the Writing Session end, 1 at the Idle Timeout end |

## Generalizations

| General | Specializations | Is-a justification |
| --- | --- | --- |
| None | None | The three concepts are not kinds of one another |

---

[UC-001]: ./uc.md
[SA-001]: ../../stakeholder-analysis.md
[SSD-001]: ./ssd.md
