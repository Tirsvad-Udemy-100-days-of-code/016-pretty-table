# G1 Project delivery

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [c55db0e] |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Re-review fixes: cite the Business Case delivery-time constraint, spell out RC | pending |

---

## Purpose

Decide whether the Pretty Table project is complete enough to publish: runnable, tested, documented and described on the git host.

## Deliverable

A Python 3.13+ project with `src/`, `tests/`, `docs/`, `pyproject.toml`, `constants.py`, `Doxyfile`, a Python `.gitignore` and a README built from the template, plus a repository description and topics.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes in a fresh `.venv` | All tests pass | Any failure |
| 2 | The program prints the Pokémon type table | Output matches the tested table | Output differs or the run fails |
| 3 | The README follows the template and its steps work | Each section is filled and the steps run | A section is missing or a step fails |
| 4 | Runtime dependencies | Only PrettyTable | Any other runtime dependency |
| 5 | Repository description and at least 3 topics are set | Visible on the repository page | Missing |
| 6 | Code review record against `qc-programming-python` | The review record (`RC-*`) says Go | No review or No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [BC-001] | Scope and success criteria |
| [SA-001] | Stakeholders S01, S02, S03 |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 Pokémon table program | Tasks 3, 4 |
| O2 Documented run, venv and tests | Tasks 1, 6 |
| O3 Tests, pyproject, constants, Doxygen | Tasks 1, 2, 4, 5 |
| O4 Repository published with description and topics | Task 8 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 — one week from the start, as the Business Case constraint on delivery time requires.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Configure project files | Create `pyproject.toml` (Python 3.13 or newer, PrettyTable runtime dependency, pytest as a dev dependency) and a Python `.gitignore` that also ignores `.env` and `.venv`. Supports O2 and O3. | No | |
| 2 | Add constants module | Create `src/constants.py` holding the Pokémon names, types and column titles so no literals are scattered in the code. Supports O3. | No | |
| 3 | Implement the Pokémon table | Create the program in `src/` that builds and prints the PrettyTable of Pokémon and their types (for example Pikachu Electric, Squirtle Water), with the assignment's function names and Doxygen comments. Supports O1. | No | |
| 4 | Add pytest tests | Create tests in `tests/` that check the rendered table and the program's output, run with `python -m pytest`. Supports O1 and O3. | No | |
| 5 | Add Doxyfile | Create a `Doxyfile` that builds the source documentation from `src/`. Supports O3. | No | |
| 6 | Write the README | Write `README.md` from the template: requirements, local `.venv` and `python -m pip install --upgrade pip` for Windows PowerShell, Linux Debian and macOS, running, testing, CI, Doxygen and layout. Supports O2. | No | |
| 7 | Describe continuous integration | Add a CI workflow that installs the project and runs pytest, and explain it in the README CI section. Supports O2. | No | |
| 8 | Set repository description and topics | Use the token from the personal `.env` (never committed, imported or tested) to set the description and topics on the git host. Supports O4. | No | |
| 9 | Review code against the Python checklist | Review the source and tests against `qc-programming-python` and record an `RC-*` before the pull request. Supports Go criterion 6. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[c55db0e]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-pretty_table/commit/c55db0e0f2f7c259018b85a90824b124cc0b780d
