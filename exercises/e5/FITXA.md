# E5 — Sekretuak, pribatutasuna eta prompt injection

**Saioa:** 4 · **Iraupena:** 25 min · **Modua:** bikoteka  
**Entregagarria:** konponketa commit-a + azalpen idatzia

**Izena:** ______________________________  **Taldea:** ______________  **Data:** __________

---

## Helburua

Repo batean dauden **sekretuak, datu pertsonalak eta prompt injection** arriskuak aurkitzea eta konpontzea. Agenteak ez du argibide maltzurrik bete behar.

## Testuingurua

Irakasleak **E5 branch edo repo ez-segurua** prestatu du. Bertan:

- `.env` fitxategi bat dago, gako faltsuekin;
- `bezeroak.csv` fitxategia datu faltsuekin;
- `README.md`-n prompt injection bat.

Datu eta gako guztiak **faltsuak** dira. Ez erabili benetako sekreturik.

## 1. urratsa — Arriskuak bilatu

Egiaztatu:

```bash
git status
ls -la
git log --oneline --all
```

Bilatu:

- [ ] `.env` edo sekretua bertsio-kontrolatuta.
- [ ] Datu pertsonalak (izenak, emailak, telefonoak) repoan.
- [ ] `.gitignore` falta edo okerra.
- [ ] `README.md`-n agentearentzako argibide susmagarriak.
- [ ] Prompt injection: testuak "ignore previous instructions" edo antzeko esaldia du.

## 2. urratsa — Prompt injection aztertu

Irakurri `README.md` eta erantzun:

| Galdera | Erantzuna |
|---|---|
| Zein testuk ematen du agentearentzako argibidea? | |
| Zer eskatzen dio agentearen? | |
| Zergatik da arriskutsua? | |
| Nola tratatu behar da testu hori? | |

> **Araua:** repo bateko testua **datu** da, ez argibide. Agenteak ez du `README.md`-ko esaldi bat bete behar, erabiltzaileak eskatu ez badu.

## 3. urratsa — Konpondu

Gutxienez:

- Gehitu `.gitignore` egokia (`.env`, `*.db`, datu-fitxategiak).
- Sortu `.env.example` garbia.
- Kendu `.env` eta datu pertsonalak repo aktiboretik.
- "Errotatu" gakoa: aldatu balioa (simulazioan).
- Ez jarraitu prompt injection-eko argibidea.

## 4. urratsa — Historialea egiaztatu

Fitxategia ezabatzeak ez du historialea garbitzen. Egiaztatu:

```bash
git log --all --full-history -- .env
git log --all --full-history -- bezeroak.csv
```

Idatzi: zer egin beharko zenukeen historialean badago? (Erantzun laburra; ez da `filter-repo` erabili behar tailer honetan.)

## 5. urratsa — Txostena

| Arriskua | Non? | Larritasuna | Konponbidea |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

## Onarpen-checklista

- [ ] Gutxienez 3 arrisku identifikatuta.
- [ ] `.gitignore` egokia.
- [ ] `.env.example` garbia.
- [ ] Datu pertsonalak kenduta.
- [ ] Gakoa aldatuta (simulazioan).
- [ ] Prompt injection ez da jarraitu.
- [ ] Azalpen idatzia (5 lerro).
- [ ] AA erregistroan jasota.

## Gogoeta

> Zergatik ez da nahikoa fitxategia ezabatzea? Zer da "gakoa errotatzea" eta zergatik da beharrezkoa?
