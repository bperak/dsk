# Skripte — isti posao izvan Colaba

Skripte prate nastavne cjeline: ono što se u bilježnici radi ćeliju po ćeliju, ovdje je jedan program koji se pokreće iz terminala. Redoslijed je isti kao redoslijed cjelina.

```bash
pip install -r requirements.txt

python3 scripts/01_pandas_osnove.py          # bez ključa
```

| Skripta | Cjelina | Tema | Treba ključ? |
|---|---|---|---|
| [`01_pandas_osnove.py`](01_pandas_osnove.py) | [02](../content/02_podaci_fair_ai.md), [03](../content/03_python_colab.md), [04](../content/04_pandas_tablice.md) | učitavanje, čišćenje i opis tabličnih podataka (ankete, katalozi, popisi) | ne |
| [`02_statistika_korelacije.py`](02_statistika_korelacije.py) | [05](../content/05_statistika.md) | sredine, raspršenje, korelacije, testovi | ne |
| [`03_vizualizacija.py`](03_vizualizacija.py) | [06](../content/06_vizualizacija.md) | grafovi po pravilima poštene vizualizacije | ne |
| [`04_nlp_obrada_teksta.py`](04_nlp_obrada_teksta.py) | [07](../content/07_nlp_tekst.md) | tokenizacija, frekvencije, stop-riječi, bigrami | ne |
| [`05_llm_analiza.py`](05_llm_analiza.py) | [08](../content/08_llm_alati.md) | klasifikacija, ekstrakcija i sažetak preko modela | **da** |
| [`06_semanticka_pretraga.py`](06_semanticka_pretraga.py) | [09](../content/09_embedding_pretraga.md) | embedding i pretraga po značenju | **da** |
| [`07_rag_kulturna_bastina.py`](07_rag_kulturna_bastina.py) | [10](../content/10_rag.md) | odgovori utemeljeni u dokumentima, s izvorom | **da** |
| [`08_agent_istrazivac.py`](08_agent_istrazivac.py) | [11](../content/11_agenti.md) | agent koji traži, provjerava i zapisuje (Google ADK) | **da** |

## Ključ za skripte 05–08

```bash
export GEMINI_API_KEY="tvoj-ključ"      # https://aistudio.google.com -> Get API key
python3 scripts/05_llm_analiza.py
```

Skripte same provjeravaju postoji li ključ. Ako ga nema, ispisuju uputu i zaustavljaju se **bez prekida rada s greškom** — ne treba ništa popravljati, samo dodati ključ.

Kad model vrati poruku o prekoračenoj kvoti (429), skripta pričeka pet sekundi i pokuša ponovno, najviše dva puta, pa ispiše jasnu poruku. Besplatna kvota se mjeri po projektu, pa svatko koristi **svoj** ključ.

## Kako čitati skriptu

Svaka skripta ima isti oblik:

1. **zaglavlje** — koja je cjelina, što se uči, što treba instalirati;
2. **priprema podataka** — mali, izmišljeni ali javno dostupni primjer, da skripta radi odmah;
3. **analiza** — korak po korak, s ispisom rezultata u terminalu;
4. **napomene** — što promijeniti za vlastite podatke.

Skripte su namjerno male (60–140 redaka) i pisane tako da se čitaju redom, bez skrivenih trikova.
