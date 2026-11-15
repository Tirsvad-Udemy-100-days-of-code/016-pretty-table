**English** · [Dansk](Getting-Started-da) · [Bahasa Melayu](Getting-Started-ms)

# Getting Started

## Requirements

Python 3.13 or newer. PrettyTable is the only runtime dependency and is installed from PyPI with the project. To run the tests and the code checks, install the development tools with `python -m pip install -e ".[dev]"`.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

## Run

```bash
python -m pretty_table
```

## Tests

```bash
python -m pytest
```

## Licence

The code is licensed under the GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later). See the `LICENSE` file.
