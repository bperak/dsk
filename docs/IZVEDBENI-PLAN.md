# Izvedbeni plan — Data Science u kulturi (2026./2027.)

**Nositelj:** izv. prof. dr. sc. Benedikt Perak
**Studij:** Sveučilišni prijediplomski studij Kulturologija (jednopredmetni), Filozofski fakultet u Rijeci
**Status kolegija:** obvezni, 1. semestar (zimski)
**Opterećenje:** 5 ECTS — 150 sati (45 sati nastave + 105 sati samostalnog rada)
**Izvedba:** koncentrirano u prva dva tjedna zimskog semestra (znanstveno usavršavanje nositelja)
**Ocjenjivanje:** 100 bodova kroz rad tijekom semestra, **bez završnog ispita**

---

## Kako je kolegij složen

Kolegij ide od pitanja prema odgovoru, a ne od alata prema alatu. Svaka od četiri cjeline završava nečim što se može pokazati: malom analizom, slikom, tekstom ili vlastitim istraživanjem.

| Modul | Naslov | ECTS | Sati | Ishodi |
|---|---|---|---|---|
| 1 | Podaci, alati i Python | 1,5 | 45 | DSK-1, DSK-2, DSK-7 |
| 2 | Analiza, statistika i vizualizacija | 1,5 | 45 | DSK-4, DSK-5 |
| 3 | Tekst, jezik i AI alati | 1 | 30 | DSK-3, DSK-8 |
| 4 | Agentski sustavi i odgovorna uporaba | 1 | 30 | DSK-6 |

**Ishodi učenja**

| Kod | Ishod |
|---|---|
| DSK-1 | Opisati osnovne teorijske postavke znanosti o znanosti te razumjeti teorijske pretpostavke kulturološki usmjerenih data-science metoda |
| DSK-2 | Navesti temeljne znanstvene metode i ocijeniti prikladnost istraživačkih metoda s obzirom na vrstu podataka i cilj istraživanja |
| DSK-3 | Prepoznati, pretražiti i koristiti javne data-science alate i podatkovne resurse, uključujući AI alate |
| DSK-4 | Objasniti i primijeniti data-science tehnike analize, dohvaćanja, pripreme i pohrane podataka |
| DSK-5 | Analizirati kvantitativne i kvalitativne tipove podataka te primijeniti postupke statističke analize |
| DSK-6 | Kritički vrednovati rezultate, metode i tehnike analize podataka, uključujući rezultate AI alata |
| DSK-7 | Svladati osnovne statističko-analitičke funkcije data-science programa (Python, Pandas, Google Colab) |
| DSK-8 | Koristiti praktične vještine znanstvenih metoda digitalne humanistike uz primjenu velikih jezičnih modela |

---

## Modul 1 — Podaci, alati i Python (1,5 ECTS · 45 sati)

**Cilj modula:** od istraživačkog pitanja do uredne tablice podataka u Colabu.

| Cjelina | Naslov | Ishodi | Materijali |
|---|---|---|---|
| 01 | [Uvod: data science u kulturi](../content/01_uvod_data_science_u_kulturi.md) | DSK-1 | knjiga kolegija, pogl. 1 |
| 02 | [Podaci u kulturi: vrste, FAIR, AI-spremnost](../content/02_podaci_fair_ai.md) | DSK-1, DSK-2 | [`scripts/01_pandas_osnove.py`](../scripts/01_pandas_osnove.py) |
| 03 | [Python i Google Colab](../content/03_python_colab.md) | DSK-7 | [bilježnica: jednostavna analiza upitnika](https://colab.research.google.com/github/bperak/dsk/blob/main/colab/DSK_analiza_upitnika_jednostavno.ipynb) |
| 04 | [Pandas — tablični podaci](../content/04_pandas_tablice.md) | DSK-4, DSK-7 | [`scripts/01_pandas_osnove.py`](../scripts/01_pandas_osnove.py) |

**Provjera znanja 1** (30 bodova, DSK-1, DSK-2, DSK-7): vlastita anketa izrađena i povezana s tablicom odgovora; podaci učitani u Colab.

---

## Modul 2 — Analiza, statistika i vizualizacija (1,5 ECTS · 45 sati)

**Cilj modula:** od sirove tablice do nalaza koji se može braniti.

| Cjelina | Naslov | Ishodi | Materijali |
|---|---|---|---|
| 05 | [Statistika — deskriptivna analiza i korelacije](../content/05_statistika.md) | DSK-5 | [`scripts/02_statistika_korelacije.py`](../scripts/02_statistika_korelacije.py) |
| 06 | [Vizualizacija podataka](../content/06_vizualizacija.md) | DSK-5 | [`scripts/03_vizualizacija.py`](../scripts/03_vizualizacija.py) |

Radna bilježnica: [analiza upitnika — jednostavna verzija](https://colab.research.google.com/github/bperak/dsk/blob/main/colab/DSK_analiza_upitnika_jednostavno.ipynb) (učitavanje, čišćenje, frekvencije, slobodni tekst, skale 1–5, sažetak).

---

## Modul 3 — Tekst, jezik i AI alati (1 ECTS · 30 sati)

**Cilj modula:** tekst kao podatak i uključivanje jezičnog modela u istraživački postupak.

| Cjelina | Naslov | Ishodi | Materijali |
|---|---|---|---|
| 07 | [NLP — obrada tekstualnih podataka](../content/07_nlp_tekst.md) | DSK-4, DSK-5 | [`scripts/04_nlp_obrada_teksta.py`](../scripts/04_nlp_obrada_teksta.py) |
| 08 | [LLM u podatkovnoj znanosti](../content/08_llm_alati.md) | DSK-6, DSK-8 | [`scripts/05_llm_analiza.py`](../scripts/05_llm_analiza.py) |
| 09 | [Embedding i semantička pretraga](../content/09_embedding_pretraga.md) | DSK-3, DSK-8 | [`scripts/06_semanticka_pretraga.py`](../scripts/06_semanticka_pretraga.py) |
| 10 | [RAG — razgovor s kulturnom baštinom](../content/10_rag.md) | DSK-6, DSK-8 | [`scripts/07_rag_kulturna_bastina.py`](../scripts/07_rag_kulturna_bastina.py) |

---

## Modul 4 — Agentski sustavi i odgovorna uporaba (1 ECTS · 30 sati)

**Cilj modula:** samostalan, kritički i dokumentiran rad s AI alatima — i odgovornost za ono što tvrdiš.

| Cjelina | Naslov | Ishodi | Materijali |
|---|---|---|---|
| 11 | [Agentski sustavi](../content/11_agenti.md) | DSK-8 | [`scripts/08_agent_istrazivac.py`](../scripts/08_agent_istrazivac.py) |
| 12 | [Etika i kritičko vrednovanje AI rezultata](../content/12_etika_ai.md) | DSK-6 | [puna bilježnica](https://colab.research.google.com/github/bperak/dsk/blob/main/colab/DSK_analiza_upitnika_Rijeka.ipynb) (AI sloj), [upute za projekt](../projekt/UPUTE_PROJEKT.md) |

**Provjera znanja 2 — projekt** (70 bodova, svi ishodi): vlastito istraživanje od pitanja do izvještaja i prezentacije. Detalji, rokovi i pravila o AI alatima: [`projekt/UPUTE_PROJEKT.md`](../projekt/UPUTE_PROJEKT.md).

---

## Tijek rada i obveze

| Tjedan | Što se radi | Što student predaje |
|---|---|---|
| 1 (tjedan 1 nastave) | moduli 1 i 2: podaci, Python, Pandas, statistika, vizualizacija | anketa izrađena, podaci učitani u Colab |
| 2 (tjedan 2 nastave) | moduli 3 i 4: tekst, LLM, embedding, RAG, agenti, etika | analiza upitnika i definicija projekta |
| nakon nastave | samostalni rad: prikupljanje i analiza podataka | seminarski rad i prezentacija |

Preporučeni ritam samostalnog rada: oko 3 sata tjedno uz svaku cjelinu — čitanje cjeline, pokretanje pripadne skripte ili bilježnice i rješavanje zadataka.

---

## Ocjenjivanje

| Aktivnost | ECTS | Maksimalno bodova |
|---|---|---|
| Pohađanje nastave | 1,5 | 0 |
| Kontinuirana provjera znanja 1 | 1 | 30 |
| Kontinuirana provjera znanja 2 (projekt) | 2,5 | 70 |
| Završni ispit | 0 | 0 |
| **UKUPNO** | **5** | **100** |

Kolegij je izveden u varijanti bez završnog ispita. Kriteriji ocjenjivanja projekta nalaze se u uputama za projekt (jasno definirani kriteriji: definicija teme, kvaliteta uzorka i instrumenta, ispravnost analize, kritičnost prema vlastitim rezultatima, kvaliteta izvještaja i prezentacije).

---

## Što treba za rad

- **Google račun** (Colab i Google Forms) — obavezan.
- **Besplatni Gemini ključ** ([Google AI Studio](https://aistudio.google.com) → *Get API key*) — potreban od modula 3; svatko koristi svoj ključ, kvota se mjeri po projektu.
- **Laptop ili računalo u praktikumu** — za Colab je dovoljan i preglednik; sve ostalo se izvodi u oblaku.

Više o načinima rada, postavljanju i rješavanju problema: [`KAKO-KORISTITI.md`](KAKO-KORISTITI.md).
