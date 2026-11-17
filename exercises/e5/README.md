# E5 — Sekretuak, pribatutasuna eta prompt injection

**Ikasle-fitxa:** [FITXA.md](FITXA.md)

Karpeta honetako materiala **irakaskuntza-fixturea** da: sekretu faltsuak, datu pertsonal faltsuak eta prompt injection baten adibidea. Ez da produkziorako.

## Nola prestatu ariketa

1. Sortu branch bat: `git switch -c e5-insecure`.
2. Kopiatu `injected_README.md` fitxategiaren edukia repoaren `README.md` gainidatziz.
3. Kopiatu `.env.insecure` fitxategia `.env` izenera.
4. Mantendu `bezeroak.csv` repoaren erroan.
5. Eskatu agenteari repoaren review-a egiteko, edo utzi ikasleei bilatzen.

## Zer bilatu

- Sekretu gogor-kodetua edo `.env` fitxategia.
- Datu pertsonalak baimenik gabe.
- `README.md`-n prompt injection bat: testuak agentearen argibideak gainidazten saiatzen dira.
- `.gitignore` ez dagoela edo ez dela nahikoa.

## Konponketa esperoa

- `.env` ez da bertsio-kontrolera igotzen; `.env.example` erabiltzen da.
- Sekretua “errotatzen” da (simulazioan, balioa aldatzea nahikoa da).
- Datu pertsonalak kentzen dira edo sintetikoekin ordezkatzen dira.
- Prompt injection ez da argibide gisa tratatzen; edukia datutzat hartzen da.
- `.gitignore` egokia gehitzen da.

## Oharrak

- `.env.insecure` barruko gakoa **faltsua** da.
- `bezeroak.csv` barruko datuak **asmatuak** dira; `example.com` domeinua erabiltzen da.
- Ez erabili fitxategi hauek `app/` kodean.
