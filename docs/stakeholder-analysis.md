# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [c55db0e] |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Re-review fix: spell out FURPS+ | pending |

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

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Work follows the plan-first process and is verified by tests | Functionality, Supportability |
| S02 | Code is readable and runs with the documented steps | Usability, Functionality |
| S03 | Repository is self-explanatory and light | Usability, Implementation (no extra runtime dependencies) |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat review of the working tree | Per phase | Reviewed documents and code | All |
| S02 | README | Once, on publication | Run and test instructions | Delivery |
| S03 | Repository page | Once, on publication | Description, topics, README | Delivery |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the assignment's exact function names; S03 wants a tidy, idiomatic project | S02, S03 | Keep the assignment's names for public functions and apply the conventions everywhere else |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Reviewed, framework-compliant work | [BC-001] O3, O4 |
| S02 | Runnable code and instructions | [BC-001] O1, O2 |
| S03 | Clear repository presentation | [BC-001] O4 |

## Sign-Off

Accepted by S01 (RC-002).

---

[BC-001]: ./business-case.md
[c55db0e]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-pretty_table/commit/c55db0e0f2f7c259018b85a90824b124cc0b780d
