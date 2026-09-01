# 07. NLP — obrada tekstualnih podataka

**Kolegij:** Data Science u kulturi | 2026./2027.

## Zašto NLP u kulturi?

Tekstualni podaci (novinski članci, društvene mreže, arhivi, katalozi) čine
velik dio humanističkih podataka. NLP (Natural Language Processing) omogućuje
njihovu sustavnu analizu.

## Osnovni koraci

1. **Tokenizacija** — razbijanje teksta na riječi
2. **Čišćenje** — lowercase, uklanjanje interpunkcije
3. **Stop-riječi** — uklanjanje čestih funkcionalnih riječi (i, a, se, u...)
4. **Frekvencije** — najčešće riječi
5. **Kolokacije** — česti spojevi riječi (bigrami, trigrami)

```python
import re
from collections import Counter

rijeci = re.findall(r"[a-zžćčšđ]+", tekst.lower())
frekvencije = Counter(rijeci)
```

## Dalje od frekvencija

- **Embedding** — riječi kao vektori, sličnost po značenju
- **LLM označavanje** — automatska klasifikacija, ekstrakcija entiteta
- **Sentiment analiza** — emocionalni ton
- **Tematsko modeliranje** — teme u korpusu

## Kritički pristup

- Frekvencije ne govore o značenju — samo o pojavljivanju
- Stop-riječi mogu sakriti važne obrate
- LLM rezultate treba provjeriti (halucinacije)

## Ishodi učenja (4, 5)

- Primijeniti tehnike analize tekstualnih podataka.
- Analizirati kvalitativne tipove podataka.

## Praktično

Skripta: `scripts/04_nlp_obrada_teksta.py`
