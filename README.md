# Pretty Table

A table of Pokémon and their types, printed with the PrettyTable package from PyPI.
It is an assignment of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*
about adding Python packages. The functions use the assignment's style: `create_table`
builds the `PrettyTable` and `main` prints it. PrettyTable is the only runtime dependency.

## Requirements

- Python 3.13 or newer.
- `venv` and `pip`, which come with Python (on Debian they are separate packages).
- Git, to clone the repository.
- Optional: [Doxygen](https://www.doxygen.nl/) to build the source documentation.

`prettytable` is installed from PyPI with the project. `pytest`, `ruff` and `mypy`
are installed only for development, through the `dev` extra.

## Set up

Clone the repository and change into it:

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-pretty_table.git
cd 016-pretty_table
```

Then create a local virtual environment named `.venv`, upgrade `pip` and install
the project in it.

### Windows powershell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell refuses to run the activation script, allow it for this window only
with `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.

### Linux debian

```bash
sudo apt install python3 python3-venv python3-pip git
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Debian 13 (trixie) ships Python 3.13. On an older release, install Python 3.13
first (for example with `pyenv`) and use it to create the `.venv`.

### MacOS

```bash
brew install python@3.13 git
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

To leave the virtual environment, run `deactivate`.

## Run

With the virtual environment active:

```bash
python -m pretty_table
```

The installed command does the same:

```bash
pretty-table
```

Output:

```text
+--------------+----------+
| Pokemon Name |   Type   |
+--------------+----------+
|   Pikachu    | Electric |
|   Squirtle   |  Water   |
|  Charmander  |   Fire   |
+--------------+----------+
```

## Run the tests

With the virtual environment active:

```bash
python -m pytest
```

The linter and the strict type check that the project also uses:

```bash
ruff check .
mypy
```

## Continuous integration

The workflow in `.gitea/workflows/ci.yml` runs on Gitea Actions on every push and
pull request. It creates a virtual environment on Python 3.13, upgrades `pip`,
installs the project with the `dev` extra and runs `ruff check .`, `mypy` and
`python -m pytest`. GitHub does not read the `.gitea` folder, so a GitHub mirror
does not run it.

## Build the source documentation

The source uses Doxygen comments and the `Doxyfile` in the repository root. Install
Doxygen (`winget install DimitriVanHeesch.Doxygen` on Windows,
`sudo apt install doxygen` on Debian, `brew install doxygen` on MacOS), then run:

```bash
doxygen Doxyfile
```

The HTML documentation is written to `docs/doxygen/html/`; open `index.html` in a
browser. The output folder is ignored by git.

## Project layout

```text
.
├── src/pretty_table/     The program
│   ├── constants.py      Column titles and the Pokémon rows
│   ├── main.py           create_table and main
│   └── __main__.py       Entry point for python -m pretty_table
├── tests/                pytest tests
├── docs/                 Project documents (business case, plan, reviews)
├── .gitea/workflows/     Continuous integration workflow
├── Doxyfile              Doxygen configuration
└── pyproject.toml        Project configuration
```

## License

GNU Affero General Public License v3.0; see [LICENSE](LICENSE).
