"""Tests for the constants."""

from pretty_table import constants


def test_column_titles_match_the_column_constants() -> None:
    assert constants.COLUMN_TITLES == (constants.COLUMN_NAME, constants.COLUMN_TYPE)


def test_pokemon_includes_the_lesson_examples() -> None:
    assert ("Pikachu", "Electric") in constants.POKEMON
    assert ("Squirtle", "Water") in constants.POKEMON


def test_pokemon_names_are_unique() -> None:
    names = [name for name, _ in constants.POKEMON]
    assert len(names) == len(set(names))
