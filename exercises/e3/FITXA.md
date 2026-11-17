# E3 — TDD AA-rekin

**Saioa:** 3 · **Iraupena:** 60 min · **Modua:** bikoteka  
**Entregagarria:** `app/faktura.py` + `tests/test_faktura.py` + commit-a

**Izena:** ______________________________  **Taldea:** ______________  **Data:** __________

---

## Helburua

Testak **lehenago** idaztea, AAren inplementazioa neurtzeko. AAk kodea sortzen du, baina testak dira egiaztapenaren epaile.

## Espezifikazioa

Sortu `faktura_totala(items, zerga_tasa, deskontu_kodea)` funtzioa `app/faktura.py` fitxategian.

- `items`: `{"prezioa": float, "kopurua": int}` hizteen zerrenda.
- `zerga_tasa`: portzentajea, 0–30 artekoa (adibidez, 21).
- `deskontu_kodea`: `None`, `"HASI"` (%10) edo `"LAGUN"` (%5).
- Deskontua **zerga aurretik** aplikatzen da.
- Emaitza 2 dezimaletara biribilduta.
- Items zerrenda hutsa → `0.00`.
- Sarrera okerrak → `ValueError`: prezio negatiboa, kopurua ≤ 0, zerga 0–30etik kanpo, deskontu-kode ezezaguna.

## 1. urratsa — Stub-a sortu

```python
# app/faktura.py
def faktura_totala(items, zerga_tasa, deskontu_kodea):
    raise NotImplementedError("E3: inplementatu")
```

## 2. urratsa — Testak idatzi

Sortu `tests/test_faktura.py`. Gutxienez **6–8 test**:

```python
import pytest

from app.faktura import faktura_totala


def test_zerga_aplikatzen_du():
    items = [{"prezioa": 100.0, "kopurua": 1}]
    assert faktura_totala(items, 21, None) == pytest.approx(121.00)


def test_hasi_deskontua_zerga_aurretik():
    items = [{"prezioa": 100.0, "kopurua": 1}]
    assert faktura_totala(items, 21, "HASI") == pytest.approx(108.90)


def test_lagun_deskontua():
    items = [{"prezioa": 100.0, "kopurua": 1}]
    assert faktura_totala(items, 21, "LAGUN") == pytest.approx(114.95)
```

Gehitu:

- items hutsa → `0.00`;
- deskontu-kode okerra → `ValueError`;
- zerga 31 → `ValueError`;
- prezio negatiboa → `ValueError`;
- kopurua 0 → `ValueError`.

## 3. urratsa — Gorri

```bash
pytest tests/test_faktura.py -q
```

Testak **gorri** egon behar dira. Ez aldatu testak kodea pasatzeko.

## 4. urratsa — AAri inplementazioa eskatu

Eman testak eta espezifikazioa. Erabili murrizketa hau:

> Hemen daude nire testak eta espezifikazioa. Inplementatu `app/faktura.py`. Ez aldatu testak. Azaldu zergatik betetzen dituzun ertz-kasuak.

## 5. urratsa — Berde eta refactor

```bash
pytest tests/test_faktura.py -q
```

- Test guztiak berde egon arte iteratu.
- Refactor: izenak, funtzio txikiak, docstring-a.
- Egiaztatu estaldura:

```bash
pytest --cov=app.faktura --cov-report=term-missing
```

## 6. urratsa — Erregistroa

| Iterazioa | Zer aldatu da? | Testak gorri/berde | Denbora |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Onarpen-checklista

- [ ] Gutxienez 6 test, ertz-kasuak barne.
- [ ] Test guztiak berde.
- [ ] Estaldura > %80.
- [ ] Testak ez dira aldatu justifikaziorik gabe.
- [ ] Kodea hitzez hitz azaltzeko gai.
- [ ] Commit-a eginda.
- [ ] AA erregistroan jasota.

## Gogoeta

> Zergatik da errazagoa AAren kodea ebaluatzea testak lehenago idazten badira? Zer gertatzen da testak geroago idazten badira?
