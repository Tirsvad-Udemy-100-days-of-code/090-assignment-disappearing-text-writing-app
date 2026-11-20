# ADR-0002 Flask as the only runtime dependency and a server-side timer

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The assignment says to use Flask and to delete the text after more than 5 seconds without typing. Stakeholder S03 wants no runtime dependencies beyond what is needed ([SA-001], CN-008), and S02 wants readable code ([SA-001], CN-004). Options for where the timer lives: (A) only in the browser with JavaScript; (B) on the server, which keeps the text and the time of the last key press, while the browser shows the countdown it is told. A browser-only timer cannot be tested with pytest and puts the rule outside Python.

## Decision

Option B. Flask is the single runtime dependency. The rule that text disappears lives in a pure Python domain class that receives time from a clock port, and the Flask layer only maps requests to use cases. The browser shows the remaining seconds that the server reports and sends the text on every change.

## Consequences

**Positive:**

- The rule is testable with pytest and a fake clock, without a browser.
- One runtime dependency, which keeps the repository light for S03.
- Browser and server clocks cannot disagree about when text is deleted.

**Negative:**

- The page needs a small amount of polling or sending to the server.
- The server holds one writing session in memory, so the app serves one writer at a time; this is in scope for a local app ([BC-001]).

## Affected Artifacts

- [BC-001] — objectives 1 to 3 and the constraint on dependencies.
- [SA-001] — concerns CN-004 and CN-008.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
