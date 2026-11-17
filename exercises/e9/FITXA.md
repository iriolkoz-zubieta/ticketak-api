# E9 — Azken erronka: ticketen etiketak

**Saioa:** 6 · **Iraupena:** 60 min · **Modua:** bikoteka  
**Entregagarria:** kode branch-a + `AA_ERREGISTROA.md` + 5 minutuko demo

**Izena:** ______________________________  **Taldea:** ______________  **Data:** __________

---

## Helburua

Ikasitakoa proiektu txiki batean aplikatzea: espezifikazioa, testak, inplementazioa, review-a eta demo. **Prozesua** ebaluatzen da, ez soilik emaitza.

## Testuingurua

`ticketak-api` baseline-a martxan dago: ticketak sortu, bilatu, eguneratu eta ezabatzen dira; statusa, lehentasuna eta esleipena balidatzen dira. Orain **etiketak (tags)** falta dira.

## Erronka

Gehitu etiketak ticketetan:

- `POST /tickets` eta `PATCH /tickets/{id}` endpoint-ek `tags: list[str]` onartzen dute.
- `POST`-ean `tags` ez bada bidaltzen, `[]` izango da.
- `PATCH`-ean `tags` bidaltzen bada, zerrenda osoa ordezten du; ez bada bidaltzen, ez da aldatzen.
- `GET /tickets?tag=...` iragazten du, eta `status`/`priority` iragazkiekin konbinatu daiteke.
- `tag` iragazki-parametroa ere normalizatzen da (minusklaz, espazioak kenduta).

### Adibidea

```http
POST /tickets
{
  "title": "APIak 500 ematen du",
  "description": "Errorea ordainketa egitean",
  "status": "open",
  "priority": "urgent",
  "assignee": "ane",
  "tags": ["BUG", " ordainketa "]
}
```

```http
GET /tickets?tag=bug&status=open
```

## Balidazioa

| Araua | Emaitza |
|---|---|
| Gehienez 5 etiketa | 6 → `422` |
| Etiketa bakoitza 1–30 karaktere | hutsa edo 31 → `422` |
| Minuskulaz eta espazioak kenduta | `" BUG "` → `"bug"` |
| Bikoiztuak kenduta | `["bug", "BUG"]` → `["bug"]` |
| `tags` ez da derrigorrezkoa | lehenetsia `[]` |

## 1. urratsa — Plana (5 min)

Idatzi:

- Zein fitxategi aldatuko dituzun.
- Nola gordeko dituzun etiketak (JSON zutabea edo taula).
- Nola egingo duzun iragazketa.
- Zein proba idatziko dituzun.

> **Aholkua:** ez hasi kodea idazten plana argi izan arte.

## 2. urratsa — Testak (15 min)

Idatzi gutxienez **6–8 proba**:

1. Ticket bat etiketekin sortzea.
2. Normalizazioa (`"BUG"`, `" bug "` → `"bug"`).
3. Bikoiztuak kentzea.
4. 5 etiketa baino gehiago → `422`.
5. `GET /tickets?tag=bug` iragazketa.
6. `status`/`priority` + `tag` konbinatzea.
7. Existitzen ez den etiketa → zerrenda hutsa.
8. `PATCH` bidez etiketak ordeztea; `tags` ez bidalita, ez aldatzea.

## 3. urratsa — Inplementazioa (25 min)

- Erabili `AGENTS.md`.
- Erabili E7ko skill-a.
- Ez gehitu dependendentzia berririk justifikatu gabe.
- Mantendu diff-a txikia.
- Exekutatu probak maiz:

```bash
pytest -q
```

## 4. urratsa — Review-a (10 min)

Bikotekideak review-a egiten du:

- [ ] Espezifikazioa betetzen du?
- [ ] Probak daude? Berde?
- [ ] Etiketak normalizatzen dira?
- [ ] Iragazketa ondo funtzionatzen du?
- [ ] Diff-a txikia da?
- [ ] Dokumentazioa eguneratuta?

## 5. urratsa — Demo (5 min)

Prestatu 3–5 minutuko demo:

1. Erakutsi `POST` bat etiketekin.
2. Erakutsi `GET /tickets?tag=...`.
3. Erakutsi proba bat gorri edo berde.
4. Azaldu erabaki bat (JSON zutabea, iragazketa, balidazioa).
5. Azaldu zer ikasi duzun.

## Onarpen-checklista

- [ ] `tags` onartzen da `POST`/`PATCH`-ean.
- [ ] `GET /tickets?tag=...` funtzionatzen du.
- [ ] Balidazioa: 5 gehienez, 1–30, minuskula, bikoiztuak kenduta.
- [ ] Gutxienez 6 proba berri.
- [ ] Probak berde.
- [ ] README/OpenAPI eguneratuta.
- [ ] `AGENTS.md` eta skill-a erabilita.
- [ ] AA erregistroa osatuta.
- [ ] Demo prest.

## Autoebaluazioa

| Irizpidea | 1 | 2 | 3 | 4 | Ebidentzia |
|---|---|---|---|---|---|
| Espezifikazioa betetzea | | | | | |
| Testak eta kalitatea | | | | | |
| Segurtasuna | | | | | |
| Agentearen erabilera | | | | | |
| Komunikazioa | | | | | |

## Gogoeta

> Zer egin duzu hobeto AA gabe? Zer egin du AAk hobeto? Zer ez zenuke AAri utziko?
