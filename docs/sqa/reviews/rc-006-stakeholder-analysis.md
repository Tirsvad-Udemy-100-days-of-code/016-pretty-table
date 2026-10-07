# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-006 |
| CrossReference | [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [SA-001]
- Checklist used: [QC-SA-001] (`qc-stakeholder-analysis.md`) and [QC-LANG-001] (`qc-language-domain.md`)
- Scope: full review. It replaces [RC-002], which was written when the checklists were not available in `framework/qc/`. Defects found were fixed first, so the version reviewed is the one with the new Version History row.
- Language and domain: en / it
- Language reviewer: none (S01 reads English and knows the IT domain)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Power/Interest grid is filled for every stakeholder | Pass | S01, S02, S03 each have Power, Interest and a Quadrant |
| 2 | Each stakeholder has a unique, stable ID | Pass | S01 to S03; none renumbered |
| 3 | Roles and context are defined with explicit Power and Interest levels | Pass | Role/Title, Organization, Power and Interest columns filled |
| 4 | Communication needs are mapped to phases or milestones | Pass | Channel, frequency, deliverable and phase for S01, S02 and S03 |
| 5 | Conflicting interests are identified with a mitigation | Pass | One conflict (S02 against S03) with a mitigation |
| 6 | Concerns are traced to Business Case objectives | Pass | Traceability table cites [BC-001] O1 to O4 |
| 7 | Concerns use business language and a FURPS+ mapping | Pass | Each concern maps to a FURPS+ attribute |
| 8 | Understandable by non-technical stakeholders | Pass | Short, plain entries per stakeholder |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, neither a placeholder | Pass | `Language` is `en` and `Domain` is `it` |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry's domain list |
| 3 | The content is written in the stated language | Pass | All prose and table cells are English |
| 4 | The register matches the one the registry gives for the type | Pass | IT Professional English: Professional English; business concerns and FURPS+ labels |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | The project has no dictionary (`DICT`), so there are no PO terms to contradict; terms are used consistently (for example PrettyTable, virtual environment, test) |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Checked in the file |
| 7 | No translated twin exists beside the document | Pass | `docs/` has one file per artifact |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | Language and domain are unchanged since the first version |
| 9 | A reviewer competent in the domain and the language has confirmed the domain terms | Pass | S01 reads English and works in the IT domain; the language reviewer is `none` |
| 10 | Abbreviations are spelled out on first use | Pass | FURPS+ is spelled out under its section heading (fixed in this review) |

## Overall Verdict

Go — every mandatory criterion of the type checklist and of QC-LANG-001 passes. One defect was fixed before the verdict: FURPS+ was not spelled out (QC-LANG-001 criterion 10). The author and the reviewer are both S01, the only stakeholder, as in the first reviews.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None open | S01 | n/a |

---

[SA-001]: ../../stakeholder-analysis.md
[QC-SA-001]: ../../../framework/qc/qc-stakeholder-analysis.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
