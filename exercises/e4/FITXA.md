# E4 — AAk sortutako PR baten review-a

**Saioa:** 4 · **Iraupena:** 45 min · **Modua:** bikoteka  
**Entregagarria:** review checklista + iruzkinak + konponketa commit bat

**Izena:** ______________________________  **Taldea:** ______________  **Data:** __________

---

## Helburua

AAk sortutako kodea **kritikoki** berrikustea. Kodea funtzionatzeak ez du esan nahi segurua, argia edo ondo probatua denik.

## Testuingurua

Irakasleak `pr-ai` branch bat emango dizu. Branch horretan AAk sortutako PR bat dago, baina **6 arazo** ditu. Zure lana da review-a egitea, iruzkinak idaztea eta konponketa bat aplikatzea.

## 1. urratsa — Brancha eta diff-a

```bash
git fetch
git switch pr-ai
git diff main...pr-ai
```

Irakurri diff-a osorik. Ez exekutatu kodea itsu; ulertu zer aldatzen duen.

## 2. urratsa — Review checklista

Markatu:

- [ ] Arazoa konpontzen du? Beste ezer apurtzen du?
- [ ] Probak daude? Berde daude?
- [ ] Sekreturik edo datu sentikorrik?
- [ ] Sarrera balidatzen da?
- [ ] SQL injection / XSS / baimen-arazoak?
- [ ] Erroreak ondo kudeatuta?
- [ ] Kodea irakurgarria da? Izenak argiak?
- [ ] Diff-a txikia eta erlazionatua?
- [ ] Dokumentazioa eguneratuta?
- [ ] Dependendentzia berriak justifikatuta?

## 3. urratsa — Iruzkinak idatzi

Bilatu gutxienez **6 arazo**. Kategoria hauek lagungarriak dira:

1. SQL injection edo kontsulta arriskutsua.
2. Sekretu gogor-kodetua.
3. `except:` hutsa edo erroreak ezkutatzea.
4. Sarrera balidaziorik eza.
5. Test bat assertion gabe.
6. Dependendentzia zaharkitua edo arriskutsua.

Erabili txantiloi hau:

```text
Fitxategia:
Lerroa:
Arazoa:
Larritasuna: altua / ertaina / baxua
Konponbidea:
```

## 4. urratsa — AAri review-a eskatu

> Egin review hau: bilatu segurtasun-arazoak, erroreen kudeaketa, proba falta eta balidazioak. Eman iruzkinak larritasunaren arabera. Ez aldatu kodea.

Konparatu AAren review-a zurearekin:

| Arazoa | Nik aurkitu dut? | AAk aurkitu du? | Ados? |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

## 5. urratsa — Konponketa bat

Aukeratu arazo bat eta konpondu. Commit txiki bat egin:

```bash
git add <fitxategia>
git commit -m "Fix: <arazoaren deskribapena>"
```

## Onarpen-checklista

- [ ] Gutxienez 5/6 arazo aurkitu.
- [ ] Iruzkinak kokapena, arazoa, larritasuna eta konponbidea dute.
- [ ] AAren review-a konparatu da.
- [ ] Konponketa bat commit-ean.
- [ ] Ez da testik aldatu justifikaziorik gabe.
- [ ] AA erregistroan jasota.

## Gogoeta

> Zergatik da arriskutsuagoa AAk sortutako kodea berrikusi gabe onartzea? Zer begiratuko duzu lehenengo?
