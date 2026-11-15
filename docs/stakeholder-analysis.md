# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [c55db0e] |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Re-review fix: spell out FURPS+ | [cd85bb4] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added concern IDs CN-001 to CN-003 (QC-SA-001 criterion 9), a conflict about author and reviewer being one person, the baseline phase in the communication table and the traceability; set the domain to education; reviewed in autonomous mode, not independent | pending |

---

## Purpose

Identify who is affected by the project and what each needs, using a power/interest grid, so the plan and the README serve them.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A finished, reviewed assignment that follows the framework |
| S02 | Udemy coursists | Fellow course participants | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README run instructions |
| S03 | GitHub viewers | Repository browsers | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies beyond the lesson's |

## Power/Interest Classification Rationale

- **Manage Closely:** S01 decides scope, writes and reviews everything.
- **Keep Informed:** S02 cannot change the project but depends on its code and README.
- **Monitor:** S03 browses for ideas and has no say; the description, topics and README are enough.

## Primary Concerns and FURPS+ Mapping

FURPS+ stands for functionality, usability, reliability, performance and supportability, plus design, implementation, interface and physical constraints.

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Work follows the plan-first process and is verified by tests | Functionality, Supportability |
| CN-002 | S02 | Code is readable and runs with the documented steps | Usability, Functionality |
| CN-003 | S03 | Repository is self-explanatory and light | Usability, Implementation (no extra runtime dependencies) |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat review of the working tree | Per phase | Reviewed documents and code | All, including MIL-002 |
| S02 | README | Once, on publication | Run and test instructions | Delivery |
| S03 | Repository page | Once, on publication | Description, topics, README | Delivery |
| S02, S03 | Wiki in English, Danish and Malay | Once, updated on change | Wiki pages | MIL-002 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the assignment's exact function names; S03 wants a tidy, idiomatic project | S02, S03 | Keep the assignment's names for public functions and apply the conventions everywhere else |
| The author and the reviewer of the baseline documents are the same person (S01), so the review is not independent | S01 | The AI assistant acts as stand-in reviewer for S01; every review record says `Mode: autonomous, not independent` and the end-of-run summary lists it for challenge |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Reviewed, framework-compliant work (CN-001) | [BC-001] O3, O4, O5 |
| S02 | Runnable code and instructions (CN-002) | [BC-001] O1, O2 |
| S03 | Clear repository presentation (CN-003) | [BC-001] O4 |
| S01, S02, S03 | A project that follows the common baseline of the framework, with a wiki in three languages | [BC-001] O5 |

## Sign-Off

Accepted by S01 (RC-002). The later edit (concern IDs, conflict, domain) is accepted on the `Go` verdict of its review record, by the AI as stand-in for S01 (autonomous mode, not independent).

---

[BC-001]: ./business-case.md
[c55db0e]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-pretty_table/commit/c55db0e0f2f7c259018b85a90824b124cc0b780d
[cd85bb4]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-pretty_table/commit/cd85bb42593077fc462fae258e9336f4ddd34985
