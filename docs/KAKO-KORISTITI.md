# Kako koristiti materijale

Materijali rade na tri načina: **u Colabu** (najbrže, ništa se ne instalira), **lokalno na računalu** (kad želiš više kontrole) i **kao predložak za vlastiti kolegij** (ako si predavač). Na kraju su i najčešći problemi s rješenjima.

---

## 1. Colab: klik i radi (preporučeno)

1. Otvori bilježnicu iz [README](../README.md) ili izravno:
   - [Analiza upitnika — jednostavna verzija](https://colab.research.google.com/github/bperak/dsk/blob/main/colab/DSK_analiza_upitnika_jednostavno.ipynb) — pravi podaci, osam koraka.
   - [Analiza upitnika — puna verzija](https://colab.research.google.com/github/bperak/dsk/blob/main/colab/DSK_analiza_upitnika_Rijeka.ipynb) — s AI slojem.
2. U Colabu odaberi **File → Save a copy in Drive** ako želiš svoje izmjene (original ostaje netaknut).
3. Pokreni ćelije redom: `Shift+Enter` ili *Runtime → Run all*.
4. Za AI korake treba ti ključ — vidi sljedeći odjeljak.

**Pravilo rada u nastavi:** sve što analiziramo je anonimno, a rezultate objavljujemo zbirno. Nikada ne objavljuj tablicu s osobnim podacima ispitanika.

---

## 2. Ključ za AI korake (besplatno, bez kartice)

1. Otvori [aistudio.google.com](https://aistudio.google.com) i klikni **Get API key**.
2. U Colabu klikni ikonu **ključa** u lijevoj traci → *Add new secret* → ime **`GOOGLE_API_KEY`**, vrijednost tvoj ključ → uključi pristup bilježnici.
3. Ponovno pokreni ćeliju koja traži ključ.

Ključ se **ne dijeli i ne objavljuje**. Besplatna kvota se mjeri po projektu (ne po ključu), pa je vlastiti ključ i praktičniji i sigurniji. Ako kvota presuši, pričekaj sat vremena ili koristi drugi model iz ponude.

---

## 3. Lokalno na računalu

```bash
git clone https://github.com/bperak/dsk.git
cd dsk
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Pokretanje skripti:

```bash
python3 scripts/01_pandas_osnove.py        # ne treba ključ
python3 scripts/02_statistika_korelacije.py
python3 scripts/03_vizualizacija.py
python3 scripts/04_nlp_obrada_teksta.py
export GEMINI_API_KEY="tvoj-ključ"         # za skripte 05-08
python3 scripts/05_llm_analiza.py
```

Provjera da su materijali ispravni (testovi compileiraju sve kodne primjere iz cjelina i provjeravaju da nema ugašenih modela):

```bash
python3 -m pytest tests/ -q
```

---

## 4. Ako si predavač

Materijali su napravljeni kao predložak koji se preuređuje, a ne kao fiksni udžbenik.

- **Struktura:** svaka cjelina ima isti oblik (uvod i ishodi → teorija s primjerima → ključni pojmovi → provjera → zadaci 🟢🟡🏆 → put dalje), pa je zamjena primjera i dodavanje vlastitih pitanja brza.
- **Ishodi:** cjeline su vezane na ishode DSK-1 … DSK-8 (vidi [izvedbeni plan](IZVEDBENI-PLAN.md)); ako mijenjaš ishode, mijenjaj i oznake u zaglavljima cjelina.
- **Bilježnice:** [jednostavna](https://colab.research.google.com/github/bperak/dsk/blob/main/colab/DSK_analiza_upitnika_jednostavno.ipynb) je predložak koji student prilagodi svom upitniku u pet koraka (poveznica na tablicu, kraća imena stupaca, ključne riječi, pokretanje).
- **Podaci:** pokazni odgovori (`data/demo_odgovori.csv`) služe da sve radi i prije nego što prikupiš prave; pravi podaci ulaze preko objavljene tablice.
- **Licenca i korištenje:** vidi napomenu na kraju [README](../README.md).

---

## NotebookLM (danas Gemini Notebook) u seminarskom radu

Googleov alat **NotebookLM** — od 16. srpnja 2026. nosi ime **Gemini Notebook** — radi kao RAG: odgovara isključivo iz izvora koje mu predaš i uz svaku tvrdnju daje citat. Zato je najbrži način da razumiješ što RAG jest (cjelina [10](../content/10_rag.md)), a ujedno praktičan alat za seminarski rad.

Radni tijek koji se u nastavi pokazao korisnim:

1. **Zasebna bilježnica za svaku temu** (bilježnice ne razgovaraju jedna s drugom).
2. **Primarni izvori prvo**: znanstveni radovi, muzejska dokumentacija, novinski arhiv, vlastiti transkripti.
3. **Pitanja s provjerom**: nakon svakog odgovora klikni citat i pročitaj ulomak — prije nego što tvrdnju prepišeš u rad.
4. **Duboko istraživanje (Deep Research)** kad ti trebaju izvori koje još ne poznaješ: alat složi plan, pretraži mrežu i vrati izvješće s izvorima. Uvezene izvore pregledaj jedan po jedan — time korpus prestaje biti samo tvoj odabir.
5. **Zapis za metodologiju**: koji alat, za što, koje izvore je predložio, koje si zadržao, a koje odbacio.

Za seminarski rad to znači i jednu obvezu: **izvore iz alata citiraj kao i svaki drugi izvor** (vidi [Mrežu triju knjiga](MREZA-KNJIGA.md) za formate citiranja), a tvrdnje koje alat nije mogao potkrijepiti izbaci ili izričito označi kao neutemeljene.

## 5. Najčešći problemi

| Simptom | Uzrok | Rješenje |
|---|---|---|
| `Kljuc pronaden: ne` | nema tajne `GOOGLE_API_KEY` | dodaj tajnu u Colabu ili postavi `export GEMINI_API_KEY=...` |
| `429` ili „prekoračena kvota" | iscrpljena besplatna kvota | pričekaj do sat vremena; bilježnica nastavlja raditi bez AI koraka |
| Poveznica na tablicu ne vraća podatke | tablica nije objavljena kao CSV | *File → Share → Publish to web* → list s odgovorima → CSV |
| Stupac nije prepoznat | promijenjen tekst pitanja u obrascu | dodaj ključnu riječ iz svog pitanja u popis u trećem koraku bilježnice |
| Neki odgovor je prazan | ispitanik nije odgovorio na pitanje | prazno nije nula; isključi iz izračuna i napiši to u izvještaju |
| Slika se ne vidi u bilježnici | ćelija nije pokrenuta | pokreni ćeliju s kodom iznad slike |
| Skripta javlja `ModuleNotFoundError` | nije instalirana ovisnost | `pip install -r requirements.txt` |

---

## 6. Redoslijed učenja (ako učiš sam)

1. Cjeline 01–04 s pripadnim skriptama — podaci, Python, Pandas.
2. Bilježnica [jednostavna verzija](https://colab.research.google.com/github/bperak/dsk/blob/main/colab/DSK_analiza_upitnika_jednostavno.ipynb) na pravim podacima.
3. Cjeline 05–06 — statistika i vizualizacija; vrati se u bilježnicu i prilagodi je svom pitanju.
4. Cjeline 07–10 — tekst, LLM, embedding, RAG.
5. Cjeline 11–12 — agenti i etika, pa [projekt](../projekt/UPUTE_PROJEKT.md) od početka do kraja.

Očekivano vrijeme: oko 3 sata po cjelini uz pokretanje primjera, plus vrijeme za vlastito istraživanje.
