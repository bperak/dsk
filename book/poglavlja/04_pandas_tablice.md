# Poglavlje 4: Tablični podaci s Pandas

---

## Sažetak poglavlja

Pandas je "Python Excel": biblioteka koja tablične podatke čini
programabilnima. Ovo poglavlje uvodi DataFrame — temeljnu strukturu
podatkovne analize — te vodi kroz cijeli radni tijek: učitavanje,
istraživanje, čišćenje, transformaciju, grupiranje i spajanje podataka,
zaključno s pripremom podataka za AI sustave. Svi primjeri izvršivi su
u Google Colabu.

---

## 4.1 DataFrame: retci, stupci, varijable

**DataFrame** je dvodimenzionalna tablica: **retci** su opažanja
(ispitanici, djela, tekstovi), **stupci** su varijable (dob, spol,
frekvencija, ocjena). Usporedba s poznatim formatima:

| Format | Retci | Stupci |
|--------|-------|--------|
| Excel tablica | Retci | Stupci |
| CSV datoteka | Redovi | Polja |
| SPSS | Slučajevi (cases) | Varijable |
| **Pandas DataFrame** | Opažanja | Varijable |

```python
import pandas as pd

anketa = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "spol": ["Ž", "M", "Ž", "Ž"],
    "dob": [19, 21, 20, 18],
    "kino_godisnje": [12, 3, 8, 20],
    "citam_sati": [5, 1, 3, 7],
})

print(anketa.shape)          # (4, 5) — 4 retka, 5 stupaca
print(anketa.columns)        # imena stupaca
print(anketa.dtypes)         # tipovi podataka
```

> **Teorijski okvir — tablica kao model.**
> Tablica je više od "formata": ona je **model podataka** koji pretpostavlja
> da svako opažanje ima iste varijable (širina), da je svaki redak zasebna
> jedinica (neovisnost) i da su vrijednosti usporedive (operacionalizacija).
> Ove pretpostavke u kulturi nisu uvijek očite — katalog muzeja miješa
> djela i zbirke, anketa miješa stavove i ponašanja. Prije analize pitajte:
> što je JEDAN redak? Koja je JEDNA varijabla? Što vrijednosti ZNAČE?

---

## 4.2 Učitavanje podataka

Pandas čita gotovo sve: CSV, Excel, JSON, SQL, HTML tablice, Google Sheets.

```python
# CSV (najčešći izlaz Google Forms anketi)
anketa = pd.read_csv("anketa.csv")

# Excel
katalog = pd.read_excel("katalog.xlsx", sheet_name="Zbirka")

# JSON
podaci = pd.read_json("metapodaci.json")

# Google Sheets (preko CSV linka)
url = "https://docs.google.com/spreadsheets/d/.../export?format=csv"
gs = pd.read_csv(url)
```

### Prvi uvid u podatke

```python
anketa.head()        # prvih 5 redaka
anketa.tail(3)       # zadnja 3 retka
anketa.info()        # tipovi + null vrijednosti
anketa.describe()    # deskriptivna statistika numeričkih stupaca
anketa.nunique()     # broj jedinstvenih vrijednosti po stupcu
anketa["spol"].value_counts()   # frekvencije kategorija
```

> **Rubrika "Što ako ne radi?"**
> - `UnicodeDecodeError` → `pd.read_csv("fajl.csv", encoding="utf-8")`
>   ili `encoding="latin-1"` (hrvatski znakovi na starijim sustavima)
> - `ParserError` → provjerite separator: `sep=";"` za hrvatske CSV-ove
>   (Excel ih sprema s točka-zarezom)
> - Pogrešni tipovi → `pd.to_numeric(..., errors="coerce")`

---

## 4.3 Čišćenje podataka

"Prljavi" podaci su pravilo, ne iznimka. Google Forms ankete, muzejski
katalozi i medijski izvozi pune su duplikata, nedosljednosti i praznina.
Čišćenje je **najveći dio posla** u podatkovnoj znanosti — procjene sežu
od 60 do 80 % ukupnog vremena.

### Koraci čišćenja

```python
# 1. Duplikati
print(f"Duplikati: {anketa.duplicated().sum()}")
anketa = anketa.drop_duplicates()

# 2. Null vrijednosti
print(anketa.isnull().sum())       # po stupcu
print(anketa.isnull().sum().sum()) # ukupno

# Opcije: ispusti retke s null (ako ih je malo)
anketa = anketa.dropna(subset=["spol"])
# ili popuni (npr. medijanom za numeričke)
anketa["dob"] = anketa["dob"].fillna(anketa["dob"].median())

# 3. Normalizacija teksta (vodeći/praveći razmaci, velika slova)
anketa["grad"] = anketa["grad"].str.strip().str.title()

# 4. Konzistentnost kategorija
print(anketa["spol"].value_counts())
# "Ž", "ž", "Z", "zensko" → sve u "Ž"
zamjena = {"ž": "Ž", "Z": "Ž", "zensko": "Ž", "m": "M", "musko": "M"}
anketa["spol"] = anketa["spol"].replace(zamjena)

# 5. Tipovi
anketa["dob"] = pd.to_numeric(anketa["dob"], errors="coerce")
```

### Dokumentiranje čišćenja

Svaka transformacija mora biti **zabilježena** — tko, što, kada, zašto:

```markdown
# README — čišćenje podataka (2026-10-05)
- uklonjeno 3 duplikata (id: 7, 12, 34)
- "ž/Z/zensko" normalizirano u "Ž"
- 2 null vrijednosti u "dob" popunjene medijanom (20)
- izvor: anketa_2026.csv (Google Forms, N=45)
```

> **Zašto je čišćenje važno za AI?** LLM-ovi i agenti (pogl. 8-11) rade
> točno onoliko dobro koliko su podaci čisti. Ako u katalogu postoje tri
> načina pisanja "Kralj" / "kralj" / "Kralj, J.", semantička pretraga i
> RAG sustav vratit će nepouzdane rezultate. **AI-spremnost počinje čišćenjem.**

---

## 4.4 Grupiranje i agregacije

Grupiranje je odgovor na pitanja tipa "prosjek po spolu", "zbroj po godini",
"raspodjela po zbirci".

```python
# Prosjek kino posjeta po spolu
anketa.groupby("spol")["kino_godisnje"].mean()

# Više mjera odjednom
anketa.groupby("spol").agg({
    "kino_godisnje": ["mean", "median", "count"],
    "dob": "mean",
})

# Frekvencije (i postoci)
anketa["zbirka"].value_counts(normalize=True) * 100

# Križna tablica
pd.crosstab(anketa["spol"], anketa["kino_godisnje"] > 10)
```

### Grupiranje u praksi: usporedba dviju zbirki

```python
katalog.groupby("zbirka")["godina"].agg(["min", "max", "count"])
```

Rezultat: Moderne zbirke od 1920-1958, Povijesne od 1894-1931... — trenutačan
uvid u strukturu zbirke koji ručnim pregledom ne biste vidjeli.

---

## 4.5 Spajanje tablica

U stvarnom životu podaci žive u više tablica: anketa + katalog + popis
ispitanika. Pandas ih spaja kao SQL:

```python
# lijevo spajanje (svi retci lijeve tablice)
merged = pd.merge(anketa, ispitanici, on="id", how="left")

# unutarnje (samo zajednički)
inner = pd.merge(katalog, autori, on="autor_id", how="inner")

# spajanje po indeksu (npr. za vremenske nizove)
combined = pd.concat([siječanj, veljača], ignore_index=True)
```

> **Pitfall:** prije spajanja provjerite da ključevi imaju iste tipove
> (`str` vs `int`) — najčešći izvor grešaka. `merged["id"].dtype` na obje strane.

---

## 4.6 FAIR priprema za AI

Kada su podaci čisti, pripremamo ih za AI sustave (LLM, embedding, RAG):

```python
# Eksport u JSON (LLM/agentima najprirodniji format)
ai_ready = katalog.to_dict(orient="records")
import json
with open("katalog_ai.json", "w", encoding="utf-8") as f:
    json.dump(ai_ready, f, ensure_ascii=False, indent=2)

# Eksport u CSV (za dijeljenje)
katalog.to_csv("katalog_cisto.csv", index=False, encoding="utf-8-sig")
```

**Provjera AI-spremnosti** (iz pogl. 2):
1. Jedinstveni ID na svakom zapisu ✓
2. Konzistentne kategorije ✓
3. JSON/CSV format ✓
4. README s opisom polja ✓
5. Licenca navedena ✓

---

## Praktikum: kompletan tok (anketa → čisto → analiza)

```python
import pandas as pd

# 1. Učitaj
df = pd.read_csv("anketa.csv")

# 2. Očisti
df = df.drop_duplicates()
df["spol"] = df["spol"].str.strip().replace({"ž": "Ž", "z": "Ž", "m": "M"})

# 3. Istraži
print(df.describe())
print(df.groupby("spol")["kultura_indeks"].mean())

# 4. Pripremi za AI
ai_ready = df.to_dict(orient="records")
print(f"✅ {len(ai_ready)} AI-spremnih zapisa")
```

---

## Vježbe

### 🟢 Osnovna
1. Učitajte svoju anketu (CSV iz Google Forms). Koliko redaka, stupaca,
   null vrijednosti, duplikata? Napišite to u jednu rečenicu kao "izvješće o kvaliteti".
2. Izračunajte prosjek, medijan i standardnu devijaciju za dva numerička stupca.
3. `value_counts()` za dva kategorijska stupca — što vidite?

### 🟡 Srednja
4. Očistite podatke: duplikati, null, normalizacija kategorija, tipovi.
   Dokumentirajte svaki korak u README (tko/što/kada/zašto).
5. `groupby` analiza: prosjek jedne numeričke varijable po dvije kategorije
   (npr. kino posjeti po spolu i godini studija).

### 🏆 Napredna
6. Spojite dvije tablice (npr. anketu i popis kulturnih ustanova) na
   zajednički ključ. Provjerite konzistentnost ključa (tipovi!).
7. Pripremite "AI-spremni" JSON iz svojih podataka i dajte ga LLM-u da
   odgovori na 3 pitanja o podacima. Provjerite svaki odgovor.

---

## Sažetak i ključni pojmovi

- DataFrame: retci = opažanja, stupci = varijable.
- Radni tijek: učitaj → istraži → očisti → transformiraj → (spoji) → izvezi.
- Čišćenje je 60-80 % posla; svaki korak dokumentirajte.
- Grupiranje (groupby) odgovara na "prosjek po kategoriji" pitanja.
- Spajanje (merge) povezuje tablice; provjerite tipove ključa.
- AI-spremnost počinje čišćenjem; JSON je prirodni format za LLM/agente.

**Ključni pojmovi:** DataFrame, Series, read_csv, info, describe, duplikati,
null, groupby, agg, merge, to_dict, AI-ready.

---

## Literatura

- McKinney, W. (2022). *Python for Data Analysis* (3. izd.). O'Reilly.
- Grus, J. (2019). *Data Science from Scratch* (2. izd.). O'Reilly. (pogl. 3)
- Pandas dokumentacija: https://pandas.pydata.org
- Wickham, H. (2014). Tidy Data. *Journal of Statistical Software*, 59(10).
