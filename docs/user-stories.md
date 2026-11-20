# User Stories

## Metadata
| Key | Value |
| --- | --- |
| ID | US-001 |
| CrossReference | [BC-001], [SA-001], [MIL-002], [UC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [99eebd6] |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Added the CrossReference to UC-001, now that it exists | [99eebd6] |

---

## Purpose and Scope

The stories of the writer for milestone [MIL-002], the core writing session: text that disappears when the writer stops typing, and the countdown that tells the writer how long is left. They support objective 1 of [BC-001] (text deleted after more than five seconds without typing) and success criterion 1. The writer is stakeholder S01 of [SA-001] in the role of the person who writes in the application. Stories about the web page itself, the README and the wiki belong to later milestones and are not covered here.

## Story List

### US-001.01 — Text disappears when I stop typing

**As a** writer, **I want** my text to disappear when I stop typing for more than five seconds, **so that** I am forced to keep writing without stopping to edit.

**Acceptance Criteria**

- Given the writer has typed text, when more than 5 seconds pass without a change of the text, then all the text is deleted.
- Given the writer has typed text, when exactly 5 seconds have passed without a change, then the text is still there.
- Given the writer has typed text, when the writer changes the text before 5 seconds have passed, then the text is kept and the 5 seconds start again.
- Given the text has been deleted, when the writer types again, then a new text starts from what the writer typed.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| UC-001, [MIL-002] | fits one iteration | none | Must | It is objective 1 of [BC-001] and the core of the assignment |

### US-001.02 — I see how long is left

**As a** writer, **I want** to see how many seconds are left before my text disappears, with a warning at the end, **so that** I know when I must type again.

**Acceptance Criteria**

- Given the writer has typed text, when the writer looks at the page, then the seconds left before deletion are shown.
- Given the text is not empty and 2 seconds or less are left, when the writer looks at the page, then a warning is shown.
- Given there is no text, when the writer looks at the page, then no countdown is shown.
- Given the text has just been deleted, when the writer looks at the page, then the page says that the text is gone.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| UC-001, [MIL-002] | fits one iteration | none | Should | It makes the rule visible to the writer, but the rule works without it |

## INVEST Check

Both stories are Independent (US-001.02 only shows what US-001.01 decides, and can be built after it), Negotiable (the warning length is a constant, not a promise), Valuable to the writer, Estimable, Small (one session rule and one display each) and Testable through the acceptance criteria. There are no exceptions.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[MIL-002]: ./milestones/mil-002-core-writing-session.md
[UC-001]: ./use-cases/uc-001/uc.md
[99eebd6]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/commit/99eebd69b73173ca68a4d9676c39855a30cdf1b9
