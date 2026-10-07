"""Tests for the Pokemon table."""

import pytest
from prettytable import PrettyTable

from pretty_table.constants import COLUMN_TITLES, POKEMON
from pretty_table.main import create_table, main

EXPECTED_TABLE = """\
+--------------+----------+
| Pokemon Name |   Type   |
+--------------+----------+
|   Pikachu    | Electric |
|   Squirtle   |  Water   |
|  Charmander  |   Fire   |
+--------------+----------+
"""


def test_create_table_returns_prettytable() -> None:
    assert isinstance(create_table(), PrettyTable)


def test_create_table_has_the_column_titles() -> None:
    assert tuple(create_table().field_names) == COLUMN_TITLES


def test_create_table_has_one_row_per_pokemon() -> None:
    table = create_table()
    assert len(table.rows) == len(POKEMON)
    assert [tuple(row) for row in table.rows] == list(POKEMON)


def test_create_table_renders_the_expected_text() -> None:
    assert create_table().get_string() == EXPECTED_TABLE.rstrip("\n")


def test_main_prints_the_table(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    assert capsys.readouterr().out == EXPECTED_TABLE
