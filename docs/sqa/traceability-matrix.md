# Traceability Matrix: Pretty Table

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; created with the review records of the baseline (autonomous, not independent) | pending |

---

## Purpose

Tracks backward and forward links between the artifact instances of Pretty Table so that the traceability of the documents is measurable. A row is added or updated whenever an instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-002] | [RC-008] |
| [SA-001] | Stakeholder Analysis | en | education | [BC-001] | [PP-001] | [RC-009] |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002] | [RC-010] |
| [MIL-001] | Milestone | en | education | [BC-001], [SA-001], [PP-001] | [MIL-002] | [RC-011] |
| [MIL-002] | Milestone | en | education | [BC-001], [PP-001], [MIL-001] | - | [RC-012] |
| Source code (`src/`, `tests/`) | Source code | - | - | [MIL-001] | - | [RC-004] |
| Wiki | Wiki | en, da, ms | education | [BC-001] | - | [RC-013] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-001] (criteria 1 and 6), [MIL-002] (criteria 1 and 6) | - | - | Covered |
| CN-002 | [MIL-001] (criteria 1 to 3) | - | - | Covered |
| CN-003 | [MIL-001] (criteria 3 to 5), [MIL-002] (criterion 3) | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | none found | - | Closed | - |

## Coverage Notes

- `-` in Upstream means foundational; in Downstream, nothing is built on it yet.
- No KPI, use case, user story or design artifact exists: the course supplies the design, so the tasks in the milestones are plain tasks. The source code is reviewed in [RC-004] and not again in MIL-002.
- The domain of every artifact is `education` since MIL-002; the earlier review records [RC-001] to [RC-007] state the former domain `it` as it was at the time.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-pretty-table-project.md
[MIL-002]: ../milestones/mil-002-framework-baseline.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-004]: ./reviews/rc-004-python-source-code.md
[RC-007]: ./reviews/rc-007-milestone-g1.md
[RC-008]: ./reviews/rc-008-business-case.md
[RC-009]: ./reviews/rc-009-stakeholder-analysis.md
[RC-010]: ./reviews/rc-010-project-plan.md
[RC-011]: ./reviews/rc-011-milestone-001.md
[RC-012]: ./reviews/rc-012-milestone-002.md
[RC-013]: ./reviews/rc-013-wiki.md
