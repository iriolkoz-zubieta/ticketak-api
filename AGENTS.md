# Proiektuaren arauak

## Komandoak

- Instalatu: `python -m pip install -e ".[dev]"`
- Datu sintetikoak: `python seed.py --reset`
- Zerbitzaria: `uvicorn app.main:app --reload`
- Probak: `pytest -q`
- Lint: `ruff check .`

## Arauak

- Exekutatu probak amaitu aurretik.
- Ez aldatu testak baimenik gabe.
- Ez gehitu dependendentzia berririk baimenik gabe.
- Ezabatu aurretik galdetu.
- Mantendu diff-a txikia eta erlazionatua.
- Ez commit-atu sekreturik.
- Errespetatu egoera-aldaketen arauak (`app/services.py`).
- Etiketak (tags) E9 ariketan gehitzen dira; ez aurreratu.

## Estiloa

- Python 3.10+, type hints.
- Funtzio txikiak, izen argiak.
- Dokumentazioa docstring-ekin.
- Ez erabili datu errealik; dena sintetikoa da.
