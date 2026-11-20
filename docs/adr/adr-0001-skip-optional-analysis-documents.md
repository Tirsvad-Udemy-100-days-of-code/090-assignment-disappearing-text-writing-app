# ADR-0001 Skip optional analysis documents

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The Business Case names KPI Definitions, a Business Model Canvas and a BPMN process model as analysis documents it may need, and the framework offers a Domain Dictionary and a Risk Analysis. The project is one course assignment of about 150 minutes with one developer. Options: (A) write all of them; (B) skip them and keep the same information in the Business Case, the Stakeholder Analysis and the Project Plan.

The Business Case already holds measurable success criteria (the job of a KPI document), no revenue model exists (no Business Model Canvas), the only process is a writer typing (no BPMN needed), PO and IT terms are the same English words (no dictionary), and risks are in the Business Case.

## Decision

Option B: KPI, Business Model Canvas, BPMN, Risk Analysis and Domain Dictionary are skipped for this project. The baseline steps Business Case, Stakeholder Analysis, Project Plan and Milestones are not skipped.

## Consequences

**Positive:**

- Less documentation effort; the one-week window is kept.
- No second place where success criteria or risks can drift.

**Negative:**

- No separate KPI tracking or process model if the project later grows.
- A reviewer must read the Business Case for criteria that a KPI document would normally hold.

## Affected Artifacts

- [BC-001] — success criteria and risks stay in the Business Case.
- [PP-001] — the plan contains no gateway for these documents.

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
