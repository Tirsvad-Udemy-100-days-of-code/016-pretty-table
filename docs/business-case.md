# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [MIL-002] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [c55db0e] |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Re-review fixes: justify the qualitative cost-benefit, add the one-week delivery constraint, spell out PyPI, SQA and QC | [cd85bb4] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added objective O5, a success criterion, a scope item, a constraint and a risk for the baseline phase MIL-002; set the domain to education; the baseline phase is allowed to be committed and merged in autonomous mode; reviewed in autonomous mode, not independent | pending |

---

## Executive Summary

This project delivers the Udemy "100 Days of Code" lesson on adding Python packages from PyPI, the Python Package Index. It is a small, runnable Python program that builds a table of Pokémon names and types with the PrettyTable package, packaged as a clean, tested and documented repository that other course participants and GitHub visitors can read and run. The effort is deliberately small, and the single runtime dependency is the one the assignment teaches.

## Methodological and Standards Foundation

The work follows the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/` (Business Case, Stakeholder Analysis, Project Plan, milestones, tasks as issues, then code). Quality characteristics follow ISO/IEC 25010:2023. Code follows the framework's `coding-conventions` skill for Python and is reviewed against its `qc-programming-*` checklist.

## Problem Statement

The assignment solution exists only as lesson material. Without a repository there is nothing to share, compare or reuse, and the install-and-import workflow for PyPI packages is not documented in a reproducible form (virtual environment, dependency declaration, tests).

## Business Opportunity

A clear, runnable reference solution lets other course participants compare their code, and gives GitHub viewers a tidy example of a small Python project with tests, documentation and project configuration.

## Objectives

1. O1: Provide a Python program that prints the Pokémon type table with PrettyTable, using the assignment's function names.
2. O2: Document how to create and use a local `.venv`, upgrade pip, run the program and run the tests.
3. O3: Provide pytest tests, a `pyproject.toml`, constants in `constants.py`, Doxygen comments and a Doxyfile.
4. O4: Publish the repository with a description and topics.
5. O5: Bring the finished project to the common baseline of the framework: the adopted framework release, a wiki in English, Danish and Malay, the README in the framework template, complete licence metadata, a traceability matrix and review records ([MIL-002]).

## Scope

### In Scope

- Python 3.13 or newer source under `src/`, tests under `tests/`, documents under `docs/`.
- `pyproject.toml`, Python `.gitignore`, `Doxyfile`, and a README built from the template.
- Repository description and topics on the git host.
- The baseline phase [MIL-002]: framework release, wiki in English, Danish and Malay, README in the framework template, licence metadata, traceability matrix and review records. It changes no behaviour of the program.

### Out of Scope

- Features beyond the lesson (the PrettyTable styling exercises of later lessons).
- Publishing the package to PyPI.
- Using, importing or testing the `.env` file; it is personal and only used to reach the git host.
- Any change to `src/` or `tests/` in the baseline phase.

## Expected Benefits

### Tangible Benefits

- A runnable, tested repository that others can clone and run in minutes.
- A reproducible environment recipe for Windows, Linux and macOS.

### Intangible Benefits

- A consistent portfolio of course assignments.
- Practice with packages, PyPI and project hygiene.

## Strategic Alignment

The project supports the participant's goal of completing the bootcamp with consistent, reviewable work, and the community goal of sharing readable solutions.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Program prints the Pokémon table | Exit code 0 and the expected table text | pytest test of the rendered table |
| 2 | Tests pass | 100% of tests pass in a fresh `.venv` | `python -m pytest` |
| 3 | README steps work | A new reader runs the program using only the README | Manual walkthrough on one OS |
| 4 | Repository metadata | Description and at least 3 topics set | Inspect the repository page |
| 5 | The baseline phase is done ([MIL-002]) | Wiki pages in 3 languages, `framework/scripts/check-readme.sh` exits with code 0, 100% of the continuous integration (CI) checks of the pull request pass | Files in `docs/wiki/`, the script exit code and the pull request status on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| PrettyTable API changes | Output or tests break | Declare a minimum version in `pyproject.toml` and test the rendered output |
| Token leaks into the repository | Credential exposure | `.env` is git-ignored and never imported or tested |
| Over-engineering a tiny assignment | Wasted effort | Keep one runtime dependency and a minimal layout |
| The author is also the reviewer of the baseline documents | A defect is missed because the review is not independent | Every review record says `Mode: autonomous, not independent`, and the end-of-run summary lists it for challenge |

## Assumptions

- Python 3.13 or newer is installed by the reader.
- PyPI is reachable when installing PrettyTable.
- The git host accepts a description and topics through its API.
- For the baseline phase an AI assistant acts as stand-in reviewer for S01, because author and reviewer are one person (source: [SA-001], Conflicting Interests).

## Constraints

- Python 3.13 or newer, `venv` for environments, pytest for tests.
- Constants live in `constants.py`; source uses Doxygen comments.
- Configuration lives in `pyproject.toml`.
- Delivery within one week of the start: 2026-10-07 to 2026-10-14.
- Only the user performs commits, pushes and merges, except in the baseline phase: there the Product Owner has authorised the assistant to commit, push, open the pull request and merge it in autonomous mode.
- The baseline phase [MIL-002] is finished within one week, by 2026-11-22.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| A few hours of the participant's time; no licence or hosting cost | A shareable, tested reference solution and a reusable project template |

The assessment is qualitative on purpose: the only cost is the participant's own time and the project earns no revenue, so a monetary return on investment would not be meaningful.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns the work and wants an accepted, reviewed result |
| S02 | Wants readable, runnable code with the assignment's function names |
| S03 | Wants a clear description, topics and README, with no runtime dependencies beyond the lesson's |

## Recommendation

Proceed — the scope is small, the cost is minimal and the result is directly reusable.

---

[SA-001]: ./stakeholder-analysis.md
[c55db0e]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-pretty_table/commit/c55db0e0f2f7c259018b85a90824b124cc0b780d
[cd85bb4]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-pretty_table/commit/cd85bb42593077fc462fae258e9336f4ddd34985
[PP-001]: ./project-plan.md
[MIL-002]: ./milestones/mil-002-framework-baseline.md
