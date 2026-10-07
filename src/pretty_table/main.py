"""!
@file main.py
@brief Builds and prints the Pokemon type table with PrettyTable.
"""

from prettytable import PrettyTable

from pretty_table.constants import COLUMN_NAME, COLUMN_TYPE, POKEMON


def create_table() -> PrettyTable:
    """!
    @brief Build the table of Pokemon names and their types.
    @return A PrettyTable with one row per Pokemon in POKEMON.
    """
    table = PrettyTable()
    table.add_column(COLUMN_NAME, [name for name, _ in POKEMON])
    table.add_column(COLUMN_TYPE, [type_ for _, type_ in POKEMON])
    return table


def main() -> None:
    """!
    @brief Print the Pokemon type table to standard output.
    """
    print(create_table())


if __name__ == "__main__":
    main()
