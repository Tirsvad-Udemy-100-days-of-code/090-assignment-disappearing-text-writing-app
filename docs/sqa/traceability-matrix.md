# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [a8ae467] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | [RC-011] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-012] |
| [MIL-001] | MIL | en | it | [PP-001] | [MIL-002] | [RC-004] |
| [MIL-002] | MIL | en | it | [MIL-001] | [MIL-003] | [RC-005] |
| [MIL-003] | MIL | en | it | [MIL-002] | [MIL-004] | [RC-006] |
| [MIL-004] | MIL | en | it | [MIL-003] | - | [RC-007] |
| [ADR-0001] | ADR | - | - | [BC-001], [PP-001] | - | [RC-008] |
| [ADR-0002] | ADR | - | - | [BC-001], [SA-001] | - | [RC-009] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [<view-ID>] | [<ADR-ID>] | [<TP-ID>] | Covered / Gap |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | [<view-ID>], [<view-ID>] | <what differs> | [<RC-ID>] | Open | - |

---

[ADR-0001]: ../adr/adr-0001-skip-optional-analysis-documents.md
[ADR-0002]: ../adr/adr-0002-flask-and-server-side-timer.md
[BC-001]: ../business-case.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-core-writing-session.md
[MIL-003]: ../milestones/mil-003-flask-web-app.md
[MIL-004]: ../milestones/mil-004-docs-and-delivery.md
[PP-001]: ../project-plan.md
[RC-001]: ./reviews/rc-001-bc-001.md
[RC-002]: ./reviews/rc-002-sa-001.md
[RC-003]: ./reviews/rc-003-pp-001.md
[RC-004]: ./reviews/rc-004-mil-001.md
[RC-005]: ./reviews/rc-005-mil-002.md
[RC-006]: ./reviews/rc-006-mil-003.md
[RC-007]: ./reviews/rc-007-mil-004.md
[RC-008]: ./reviews/rc-008-adr-0001.md
[RC-009]: ./reviews/rc-009-adr-0002.md
[RC-010]: ./reviews/rc-010-mil-001-code.md
[RC-011]: ./reviews/rc-011-bc-001-delta.md
[RC-012]: ./reviews/rc-012-pp-001-delta.md
[SA-001]: ../stakeholder-analysis.md
