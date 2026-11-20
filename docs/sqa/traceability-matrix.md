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
| [US-001] | US | en | it | [BC-001], [MIL-002] | [UC-001] | [RC-022] |
| [UC-001] | UC | en | it | [US-001] | [DM-001], [SSD-001] | [RC-023] |
| [DM-001] | DM | en | it | [UC-001] | [SSD-001] | [RC-024] |
| [SSD-001] | SSD | en | it | [UC-001], [DM-001] | [OC-001] | [RC-025] |
| [OC-001] | OC | - | - | [SSD-001], [DM-001] | [SD-001] | [RC-026] |
| [SD-001] | SD | - | - | [OC-001] | [DCD-001] | [RC-030] |
| [DCD-001] | DCD | - | - | [DM-001], [SD-001] | - | [RC-029] |
| [DM-002] | DM | en | it | [DM-001], [UC-001] | [DCD-002] | [RC-020] |
| [DCD-002] | DCD | - | - | [DCD-001], [DM-002], [SD-001] | - | [RC-031] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [UC-001], [SD-001], [DCD-002] | [ADR-0002] | unit and integration tests (no TP document) | Covered |
| CN-002 | [PP-001], [MIL-001] | [ADR-0001] | - | Covered |
| CN-003 | [OC-001], [DCD-002] | [ADR-0002] | unit tests (no TP document) | Covered |
| CN-004 | [DCD-002] | - | - | Covered |
| CN-005 | README | - | - | Covered |
| CN-006 | README, wiki | - | - | Covered |
| CN-007 | README, repository description and topics | - | - | Covered |
| CN-008 | [DCD-002] | [ADR-0002] | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | [DCD-001], [SD-001] | The Delivery package and `FlaskController` names no longer matched the Presentation layer design | [RC-029] | Closed | [RC-030] |


---

[ADR-0001]: ../adr/adr-0001-skip-optional-analysis-documents.md
[ADR-0002]: ../adr/adr-0002-flask-and-server-side-timer.md
[BC-001]: ../business-case.md
[DCD-001]: ../use-cases/uc-001/dcd.md
[DCD-002]: ../dcd.md
[DM-001]: ../use-cases/uc-001/dm.md
[DM-002]: ../domain-model.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-core-writing-session.md
[MIL-003]: ../milestones/mil-003-flask-web-app.md
[MIL-004]: ../milestones/mil-004-docs-and-delivery.md
[OC-001]: ../use-cases/uc-001/oc.md
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
[RC-013]: ./reviews/rc-013-us-001.md
[RC-014]: ./reviews/rc-014-uc-001.md
[RC-015]: ./reviews/rc-015-dm-001.md
[RC-016]: ./reviews/rc-016-ssd-001.md
[RC-017]: ./reviews/rc-017-oc-001.md
[RC-018]: ./reviews/rc-018-sd-001.md
[RC-019]: ./reviews/rc-019-dcd-001.md
[RC-020]: ./reviews/rc-020-dm-002.md
[RC-021]: ./reviews/rc-021-dcd-002.md
[RC-022]: ./reviews/rc-022-us-001-delta.md
[RC-023]: ./reviews/rc-023-uc-001-delta.md
[RC-024]: ./reviews/rc-024-dm-001-delta.md
[RC-025]: ./reviews/rc-025-ssd-001-delta.md
[RC-026]: ./reviews/rc-026-oc-001-delta.md
[RC-027]: ./reviews/rc-027-sd-001-delta.md
[RC-028]: ./reviews/rc-028-mil-002-code.md
[RC-029]: ./reviews/rc-029-dcd-001-delta.md
[RC-030]: ./reviews/rc-030-sd-001-delta2.md
[RC-031]: ./reviews/rc-031-dcd-002-delta.md
[SA-001]: ../stakeholder-analysis.md
[SD-001]: ../use-cases/uc-001/sd.md
[SSD-001]: ../use-cases/uc-001/ssd.md
[UC-001]: ../use-cases/uc-001/uc.md
[US-001]: ../user-stories.md
