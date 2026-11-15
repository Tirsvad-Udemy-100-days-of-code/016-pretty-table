[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Melayu**

# Bermula

## Keperluan

Python 3.13 atau lebih baharu. PrettyTable ialah satu-satunya kebergantungan semasa larian dan dipasang daripada PyPI bersama projek. Untuk menjalankan ujian dan semakan kod, pasang alat pembangunan dengan `python -m pip install -e ".[dev]"`.

## Persediaan

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

## Jalankan

```bash
python -m pretty_table
```

## Ujian

```bash
python -m pytest
```

## Lesen

Kod ini dilesenkan di bawah the GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later). Lihat fail `LICENSE`.
