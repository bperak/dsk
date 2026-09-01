# Data Science u kulturi — 2026./2027.

Skripte i materijali za kolegij **Data Science u kulturi** (obvezni, 1. semestar,
Preddiplomski studij Kulturalni studiji, FFRI).

**Nositelj:** izv. prof. dr. sc. Benedikt Perak

Nastava se izvodi **koncentrirano u prva dva tjedna zimskog semestra (listopad 2026.)**
zbog znanstvenog usavršavanja (sabbatical). Kolegij je **AI-first**: uz klasične
data-science metode (Pandas, statistika, vizualizacija), uči se suvremeni AI stack
— veliki jezični modeli, embedding, semantička pretraga, RAG i agentski sustavi —
u kontekstu kulturoloških istraživanja.

## 📖 Temeljni resurs

> **Perak, B. (2025). *Komunikacija u doba umjetne inteligencije: Razvoj velikih jezičnih modela i komunikacijskih agenata*. Rijeka: Filozofski fakultet u Rijeci.**
>
> Open access: https://github.com/bperak/komunikacija_u_doba_ai | ISBN 978-953-361-147-1

Knjiga prati razvoj komunikacijskih tehnologija od usmene predaje do velikih
jezičnih modela i autonomnih komunikacijskih agenata — temeljni okvir za
razumijevanje AI alata u podatkovnoj znanosti.

## Sadržaj

### 📖 Teorija (`content/`)

| # | Poglavlje |
|---|-----------|
| 01 | [Uvod: Data Science u kulturi](content/01_uvod_data_science_u_kulturi.md) |
| 02 | [Podaci u kulturi: FAIR principi](content/02_podaci_fair_ai.md) |
| 03 | [Python i Google Colab](content/03_python_colab.md) |
| 04 | [Pandas — tablični podaci](content/04_pandas_tablice.md) |
| 05 | [Statistika i korelacije](content/05_statistika.md) |
| 06 | [Vizualizacija](content/06_vizualizacija.md) |
| 07 | [NLP obrada teksta](content/07_nlp_tekst.md) |
| 08 | [LLM u podatkovnoj znanosti](content/08_llm_alati.md) |
| 09 | [Embedding i semantička pretraga](content/09_embedding_pretraga.md) |
| 10 | [RAG: razgovor s baštinom](content/10_rag.md) |
| 11 | [Agentski sustavi](content/11_agenti.md) |
| 12 | [Etika i kritičko vrednovanje AI](content/12_etika_ai.md) |

### 💻 Skripte (`scripts/`)

| # | Tema | Skripta |
|---|------|---------|
| 1 | Pandas — tablični podaci i FAIR principi | `01_pandas_osnove.py` |
| 2 | Statistika i korelacije | `02_statistika_korelacije.py` |
| 3 | Vizualizacija | `03_vizualizacija.py` |
| 4 | NLP obrada teksta | `04_nlp_obrada_teksta.py` |
| 5 | LLM analiza (klasifikacija, ekstrakcija, sažetak) | `05_llm_analiza.py` |
| 6 | **Semantička pretraga (embedding)** | `06_semanticka_pretraga.py` |
| 7 | **RAG: razgovor s kulturnom baštinom** | `07_rag_kulturna_bastina.py` |
| 8 | **Agent istraživač (Google ADK)** | `08_agent_istrazivac.py` |

### 🎓 Projekt (`projekt/`)

| Dokument | Opis |
|----------|------|
| [Upute za projekt](projekt/UPUTE_PROJEKT.md) | Faze, rokovi, ocjenjivanje, AI pravila |
| [Predložak prijedloga](projekt/PRIJEDLOG_TEMPLATE.md) | Format Domena/Problem/Cilj |
| [Primjeri iz prošlih godina](projekt/PRIMJERI_IZ_PROSLIH_GODINA.md) | Kako su studenti definirali teme |

### 🧪 Colab vježbe

| Datoteka | Opis |
|----------|------|
| `colab/DS_KULT_Podatkovna_znanost_u_kulturi.ipynb` | AI-first pipeline: FAIR → Pandas+LLM → embedding → RAG → agenti → etika |

## Postavljanje

```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn nltk google-generativeai google-adk
export GEMINI_API_KEY="..."   # https://aistudio.google.com
```

## AI koncepti (knjiga kao okvir)

- **LLM kao komunikacijski agent** — modeli kao sučelja prema podacima (pogl. o LLM-ovima)
- **Embedding** — distribucijska semantika i vektorske reprezentacije
- **Semantička pretraga** — pronalazak po značenju, ne samo po riječima
- **RAG** — dohvat + generiranje, odgovori temeljeni na dokazima iz korpusa
- **Agenti** — LLM + alati + petlja (razmisli → djeluj → promatraj → prilagodi)
- **Kritičko vrednovanje** — halucinacije, pristranost, etika

## Literatura

- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije*. FFRI Rijeka. (open access)
- Grus, J. (2019). *Data Science from Scratch*. O'Reilly.
- Bommasani et al. (2021). *On the Opportunities and Risks of Foundation Models*. arXiv:2108.07258
- Python za lingviste: https://github.com/nljubesi/python-for-linguists

## Resursi

- Google Colab: https://colab.research.google.com
- Google AI Studio: https://aistudio.google.com
- Google ADK: https://adk.dev
- Pandas: https://pandas.pydata.org
- Voyant Tools: https://voyant-tools.org
- Recogito: https://recogito.pelagios.org
- Knjiga: https://github.com/bperak/komunikacija_u_doba_ai
