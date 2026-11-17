# E1 — Prompt laborategia

**Saioa:** 1 · **Iraupena:** 60 min · **Modua:** bikoteka  
**Entregagarria:** `prompt_liburua.md` (3 prompt + konparaketa-taula)

**Izena:** ______________________________  **Taldea:** ______________  **Data:** __________

---

## Helburua

Prompt baten **testuinguruak, murrizketek eta onarpen-irizpideek** emaitzan duten eragina neurtzea. Ez da "prompt magiko" bat bilatzen; frogatzea zer den beharrezkoa emaitza ona lortzeko.

## Testuingurua

Denda batek prezioen kalkulua egiteko funtzio bat behar du. Zuk hiru prompt maila desberdin probatuko dituzu, eta emaitzak alderatuko dituzu.

## Espezifikazioa

`prezio_osoa(kopurua, unitate_prezioa, bezero_mota, kupoi_kodea)` funtzioak:

- `kopurua` eta `unitate_prezioa` positiboak dira.
- `bezero_mota`: `arrunta`, `bazkidea`, `premium`.
- Bazkideek **%5eko** deskontua dute; premiumek **%10ekoa**.
- Kupoiak deskontu gehigarria ematen du:
  - `KUPOI10`: %10
  - `KUPOI20`: %20
  - `None`: kupoirik ez
  - Beste balio bat: `ValueError`
- Deskontuak **segidan** aplikatzen dira: lehen bezeroaren deskontua, gero kupoia.
- Emaitza 2 dezimaletara biribilduta.
- Sarrera okerrak (`kopurua <= 0`, `unitate_prezioa <= 0`, bezero mota ezezaguna) → `ValueError`.

## 1. urratsa — Hiru promptak idatzi

Idatzi hiru prompt maila desberdinetan, baina **helburu bera** lortzeko.

### A prompta: minimalista

> Idatzi funtzio bat prezio osoa kalkulatzeko.

### B prompta: testuingurua eta murrizketak

Idatzi prompt bat non hauek agertzen diren:

- testuingurua (denda, Python);
- sarrera eta irteera;
- deskontuen arauak;
- erroreen kudeaketa;
- irteera-formatua.

### C prompta: B + adibideak + onarpena

Idatzi B prompta, baina gehitu:

- 2–3 adibide sarrera/irteera;
- ertz-kasuak;
- onarpen-irizpideak;
- eskatu probak edo proba-kasuak.

> **Aholkua:** ez itsatsi prompt luzea behin eta berriz. Gorde bertsioak eta aldatu aldagai bat bakarrik.

## 2. urratsa — Probatu kasu hauek

| # | Kasua | Sarrera | Esperoa |
|---|---|---|---|
| 1 | Arrunta, kupoirik gabe | `2, 50.0, "arrunta", None` | `100.00` |
| 2 | Bazkidea, kupoirik gabe | `2, 50.0, "bazkidea", None` | `95.00` |
| 3 | Premium + KUPOI10 | `2, 50.0, "premium", "KUPOI10"` | `81.00` |
| 4 | Bazkidea + KUPOI20 | `2, 50.0, "bazkidea", "KUPOI20"` | `76.00` |
| 5 | Kupoi okerra | `1, 10.0, "arrunta", "KUPOI99"` | `ValueError` |
| 6 | Kopuru negatiboa | `-1, 10.0, "arrunta", None` | `ValueError` |

Egiaztatu emaitza bakoitza **zenbakiarekin**, ez "itxura ona" delako.

## 3. urratsa — Konparaketa-taula

| Irizpidea | A | B | C |
|---|---|---|---|
| Kodea exekutatzen da? | | | |
| 6 kasuak zuzenak? | | | |
| Ertz-kasuak ondo kudeatzen ditu? | | | |
| Kodea ulergarria da? | | | |
| Erantzunak azalpena ematen du? | | | |
| Zenbat iterazio behar izan dituzu? | | | |

## 4. urratsa — Ondorioa

Idatzi 5–8 lerro:

- Zer gehitu dio B promptak A promptari?
- Zer gehitu dio C promptak B promptari?
- Zein da **gutxieneko testuingurua** emaitza ona lortzeko?
- Zer gertatuko litzateke testuingurua kendu edo murrizten baduzu?

## Onarpen-checklista

- [ ] Hiru promptak idatzita eta exekutatuta.
- [ ] 6 kasuak probatuta, emaitzekin.
- [ ] Konparaketa-taula beteta.
- [ ] Ondorioa idatzita.
- [ ] Promptak `prompt_liburua.md` fitxategian gordeta.
- [ ] AA erregistroan prompt bakoitzaren ebidentzia.

## Gogoeta

> Prompt ona ez da luzea izatea; **beharrezkoa** izatea da. Zer da zure kasuan beharrezkoa?
