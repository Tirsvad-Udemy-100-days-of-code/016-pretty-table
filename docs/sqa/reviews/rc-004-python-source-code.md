# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-004 |
| CrossReference | [MIL-001], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [10337f4] |

---

## Artifact Under Review

- Instance reviewed: Python source code in `src/pretty_table/` and its tests in `tests/` (task 9 of [MIL-001], Go criterion 6)
- Checklist used: [QC-PY-001] (`qc-programming-python.md`)
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | PEP 8 casing | Pass | Modules `constants.py`, `main.py`; functions `create_table`, `main`; constants `COLUMN_NAME`, `POKEMON` |
| 2 | Names state purpose; no abbreviations | Pass | Minor: the comprehension variable `type_` in `main.py` could be `pokemon_type`, which avoids the trailing underscore. Not a defect |
| 3 | Formatter and linter pass, no suppressions | Pass | `ruff format --check .` reports 17 files already formatted; `ruff check .` passes; no `noqa` comments |
| 4 | Every signature annotated | Pass | `create_table() -> PrettyTable`, `main() -> None`, all test functions annotated |
| 5 | No bare except or swallowed exceptions | N-A | The code has no exception handling |
| 6 | No mutable defaults, no shadowed builtins | Pass | No default arguments; no builtin names shadowed |
| 7 | Context managers for files, locks and connections | N-A | The code opens no files, locks or connections |
| 8 | Docstrings say what, not how | Pass | Every module and function has a Doxygen docstring |
| 9 | `logging` instead of `print`; no secrets in output | Pass | `main()` uses `print` to produce the program's required output, not diagnostics; no secrets or personal data are printed |
| 10 | Classes and operations trace to a DCD | N-A | The task is a plain technical task (MIL-001 task 3, no use case or DCD); there is no DCD in the project |
| 11 | Tests for new behaviour, named for the behaviour, order- and network-independent | Pass | 8 tests in `tests/test_main.py` and `tests/test_constants.py`; `python -m pytest` passes |
| 12 | Type checker strict, `Any` justified | Pass | `mypy` (strict, set in `pyproject.toml`) reports no issues in 7 source files; no `Any` |
| 13 | Dependencies declared and pinned, none unused | Pass | `prettytable>=3.10` is declared and used; dev tools are in the `dev` extra. The pin is a lower bound, not an exact version |

## Overall Verdict

Go — every mandatory criterion passes or does not apply, and the optional criteria pass. This satisfies Go criterion 6 of [MIL-001]. The author and the reviewer are both S01, the only stakeholder, as in RC-001 to RC-003.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Optionally rename `type_` to `pokemon_type` in `main.py` | S01 | next change to `main.py` |
| Re-review RC-001 to RC-003 against the checklists in `framework/qc/`, which were missing when those records were written | S01 | when convenient |

---

[MIL-001]: ../../milestones/mil-001-pretty-table-project.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[10337f4]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-pretty_table/commit/10337f404f9bfebaaeabdd7beb1ce4683737f7bc
