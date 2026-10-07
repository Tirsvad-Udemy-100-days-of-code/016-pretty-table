"""!
@file constants.py
@brief Constants of the Pokemon table: column titles and the rows shown.
"""

## Title of the column holding the Pokemon name.
COLUMN_NAME: str = "Pokemon Name"

## Title of the column holding the Pokemon type.
COLUMN_TYPE: str = "Type"

## Column titles in display order.
COLUMN_TITLES: tuple[str, str] = (COLUMN_NAME, COLUMN_TYPE)

## Pokemon names in display order, paired with their type.
POKEMON: tuple[tuple[str, str], ...] = (
    ("Pikachu", "Electric"),
    ("Squirtle", "Water"),
    ("Charmander", "Fire"),
)
