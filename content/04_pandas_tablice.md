# 04. Pandas — tablični podaci

**Kolegij:** Data Science u kulturi | 2026./2027.

> **U ovoj cjelini.** Podatke o kulturi — ankete o kulturnim navikama, kataloge izložbi, evidencije posjećenosti događaja — pretvaramo u tablicu s kojom računalo može raditi. Upoznajemo strukturu DataFrame, osnovne operacije, učitavanje različitih formata, čišćenje podataka i FAIR pripremu za daljnju analizu i AI alate.
>
> **Ishodi:** **DSK-4** Primijeniti data-science tehnike pripreme i pohrane podataka. · **DSK-7** Svladati osnovne funkcije data-science programa.
>
> **Uz ovu cjelinu idu:** skripta [`scripts/01_pandas_osnove.py`](../scripts/01_pandas_osnove.py), bilježnica [`colab/DSK_analiza_upitnika_jednostavno.ipynb`](../colab/DSK_analiza_upitnika_jednostavno.ipynb) i sljedeća cjelina [05. Statistika](05_statistika.md).

Podaci u kulturi rijetko dolaze kao gotova tablica: odgovori stižu kao izvoz iz obrasca, popis izložaka kao katalog u Excelu, posjećenost događaja kao dnevni izvještaj. Pandas je Python biblioteka koja sve te oblike svodi na jedan — tablicu u memoriji računala, koju tada možemo reproducibilno filtrirati, grupirati i sažimati, bez ručnog prepisivanja.

## DataFrame

**DataFrame** je osnovna struktura Pandasa: retci = opažanja, stupci = varijable.
Analogno tablici u Excelu, ali programabilno.

Ključna razlika prema Excelu nije u izgledu, nego u tome što je svaki korak analize zapisan kao naredba. Takav zapis možemo ponoviti na novim podacima i poslati kolegi na provjeru — što je osnova znanstvenog izvješća.

| Pojam | U tablici | U Pandasu |
|-------|-----------|-----------|
| Redak | jedno opažanje (ispitanik, izložak, događaj) | `df.iloc[0]` |
| Stupac | jedna varijabla (pitanje, polje) | `df["kino"]` |
| Indeks | redni broj retka | `df.index` |
| Tip podatka | broj, tekst ili logička vrijednost | `df.dtypes` |

```python
import pandas as pd

df = pd.DataFrame({
    "id": [1, 2, 3],
    "dob": [19, 21, 20],
    "kino": [12, 3, 8],
})

print(df.shape)          # (3, 3) — tri opažanja, tri varijable
print(df["dob"].mean())  # 20.0
```

Isti oblik ima katalog izložbe: svaki redak je jedno djelo, svaki stupac jedno njegovo svojstvo.

```python
katalog = pd.DataFrame({
    "naslov": ["Portret", "Pejzaž", "Akt"],
    "godina": [1920, 1935, 1948],
    "tehnika": ["ulje", "akvarel", "ulje"],
    "posjetitelja": [120, 85, 143],
})

print(katalog.groupby("tehnika")["posjetitelja"].sum())
```

## Osnovne operacije

Pregled (`head`, `info`) provjerava je li datoteka pročitana kako smo očekivali, sažetak (`describe`) daje prve brojke, a grupiranje (`groupby`) uspoređuje podskupine.

```python
df.head()          # prvih 5 redaka
df.info()          # tipovi podataka
df.describe()      # deskriptivna statistika
df["kino"].mean()  # prosjek stupca
df.groupby("spol")["kultura"].mean()  # grupiranje
df.isnull().sum()  # provjera null vrijednosti
df.drop_duplicates()  # uklanjanje duplikata
df["spol"].value_counts()      # frekvencije kategorija
df.sort_values("kino", ascending=False)  # sortiranje
```

| Naredba | Što radi | Primjer iz kulture |
|---------|----------|--------------------|
| `head()` | prvih pet redaka | brza provjera uvezenih odgovora |
| `info()` | tipovi i prazna polja | je li „godina“ broj ili tekst |
| `describe()` | prosjek, kvartili, raspon | broj kino posjeta godišnje |
| `mean()` | prosjek jednog stupca | prosječna ocjena programa (1–5) |
| `groupby()` | razdvaja, računa, spaja | ocjena po žanru ili po dobi |
| `isnull().sum()` | broji prazna polja | koliko ispitanika nije odgovorilo |
| `drop_duplicates()` | uklanja dvostruke zapise | dvaput uvezeni isti upitnik |

`groupby` radi u tri koraka: razdvaja retke po kategoriji, primjenjuje funkciju na svaku skupinu i spaja rezultate. Rezultat zato ima onoliko redaka koliko ima kategorija.

## Učitavanje podataka

Pandas čita gotovo svaki format u kojem se podaci o kulturi čuvaju: CSV izvoz iz obrasca, Excel katalog, JSON izvoz iz baze događaja.

```python
df_csv = pd.read_csv("anketa.csv")
df_excel = pd.read_excel("katalog.xlsx")
df_json = pd.read_json("podaci.json")
```

Pri učitavanju provjeravamo tri stvari: razdjelnik stupaca, kodiranje znakova i redak s nazivima stupaca. Hrvatski izvozi često koriste točku-zarez kao razdjelnik, a stariji zapisi kodiranje Windows-1250.

| Format | Kada se koristi | Primjer u kulturi |
|--------|-----------------|-------------------|
| CSV | jednostavne tablice, ankete | izvoz odgovora iz Google obrasca |
| Excel | ručno vođene evidencije | katalog izložbe s više listova |
| JSON | ugniježđeni zapisi, izvozi iz baze | popis događaja s atributima |

```python
anketa = pd.read_csv("data/demo_odgovori.csv", sep=",", encoding="utf-8")
print(anketa.head())
print(anketa.columns.tolist())   # nazivi stupaca kakve je uvezao obrazac
```

## Čišćenje podataka

1. Ukloni duplikate
2. Obradi null vrijednosti (ispusti ili popuni)
3. Normaliziraj formate (datumi, tekst)
4. Provjeri konzistentnost kategorija
5. Dokumentiraj promjene

Čišćenje je interpretativni posao, ne tehnička sitnica. Kada prazno polje shvatimo kao nulu, a ne kao „bez odgovora“, donijeli smo sadržajnu odluku koju u izvješću moramo navesti. Isto vrijedi za spajanje naziva „M“, „m“ i „muški“ u jednu kategoriju.

| Problem | Zašto smeta | Tipično rješenje |
|---------|-------------|------------------|
| Duplikati | dvostruko broje iste ispitanike | `drop_duplicates()` |
| Prazna polja | kvare prosjek i grafove | `dropna()` ili `fillna()` |
| Nejednake kategorije | grupiranje daje krive skupine | `replace()`, `str.strip()` |
| Tekst umjesto broja | `mean()` ne radi | `pd.to_numeric()` |
| Netočni datumi | onemogućuju vremensku analizu | `pd.to_datetime()` |

```python
df = df.drop_duplicates()
df["dob"] = pd.to_numeric(df["dob"], errors="coerce")
df["spol"] = df["spol"].str.strip().str.upper().replace({"MUSKI": "M"})
df["kino"] = df["kino"].fillna(df["kino"].median())
df = df.dropna(subset=["dob"])
df["datum"] = pd.to_datetime(df["datum"], errors="coerce")
```

## FAIR priprema za AI

- Strukturirani format (CSV/JSON)
- Konzistentne vrijednosti
- Data dictionary
- Eksport u JSON za LLM/agente

Očišćena tablica još nije podatak koji drugi mogu ponovno upotrijebiti. FAIR načela traže da bude pronađiv, dostupan, interoperabilan i ponovno upotrebljiv: uz tablicu ide opis stupaca, vrijednosti slijede jedan dogovor, a format je strojno čitljiv.

| Stupac | Tip | Opis | Dopuštene vrijednosti |
|--------|-----|------|-----------------------|
| `id` | cijeli broj | identifikator ispitanika | 1, 2, 3 … |
| `dob` | cijeli broj | godine ispitanika | 18–99 |
| `kino` | cijeli broj | posjeti kina godišnje | 0–100 |
| `ocjena_programa` | cijeli broj | zadovoljstvo programom | 1–5 |
| `žanr` | tekst | najdraži žanr | drama, komedija, dokumentarac |

```python
df.to_json("anketa_fair.json", orient="records", force_ascii=False, indent=2)
```

## Ishodi učenja (4, 7)

- Primijeniti data-science tehnike pripreme i pohrane podataka.
- Svladati osnovne funkcije data-science programa.

## Ključni pojmovi

| Pojam | Značenje |
|-------|----------|
| DataFrame | tablica: retci su opažanja, stupci varijable |
| Opažanje | jedan redak — ispitanik, izložak ili događaj |
| Varijabla | jedan stupac — mjereno svojstvo |
| Indeks | oznaka retka za dohvat i spajanje |
| `groupby` | razdvajanje, izračun i spajanje po kategorijama |
| Null vrijednost | prazno polje koje treba objasniti ili obraditi |
| Duplikat | dvostruko zapisano isto opažanje |
| Data dictionary | opis stupaca, tipova i dopuštenih vrijednosti |
| FAIR | pronađivost, dostupnost, interoperabilnost, ponovna uporaba |

## Provjeri razumiješ

1. Što u DataFrameu predstavlja redak, a što stupac?
2. Zašto `groupby("žanr")["ocjena"].mean()` daje drukčiju sliku od ukupnog prosjeka?
3. Zašto nije dobro automatski ispustiti sve retke s praznim poljima?
4. Čemu služi data dictionary i kome je namijenjen?

<details><summary>Odgovori</summary>

1. Redak je jedno opažanje — jedan ispitanik, jedno djelo u katalogu ili jedan događaj. Stupac je jedna varijabla, odnosno svojstvo koje smo izmjerili za sva opažanja.

2. Ukupni prosjek sabire različite skupine u jedan broj. Ako je drama ocijenjena više, a dokumentarac niže, grupirani rezultat pokazuje taj raspor koji ukupni prosjek skriva.

3. Prazno polje nije uvijek nula niti slučajno. Nekad znači da ispitanik nije bio u doticaju s tom vrstom sadržaja, a nekad da nije želio odgovoriti. Ispuštanjem svih takvih redaka gubimo ispitanike koji su odgovorili na ostala pitanja i mijenjamo sastav uzorka.

4. Data dictionary je popis stupaca s tipovima, opisima i dopuštenim vrijednostima. Namijenjen je istraživačima i alatima koji podatak preuzimaju, a nisu sudjelovali u prikupljanju.

</details>

## Praktično

Povezana skripta i bilježnica: [`scripts/01_pandas_osnove.py`](../scripts/01_pandas_osnove.py), [`colab/DSK_analiza_upitnika_jednostavno.ipynb`](../colab/DSK_analiza_upitnika_jednostavno.ipynb).

- 🟢 Učitaj `data/demo_odgovori.csv` i ispiši broj redaka, broj stupaca i nazive stupaca.
- 🟢 Provjeri koliko je praznih polja u svakom stupcu i zapiši koji ih ima najviše.
- 🟡 Skrati nazive stupaca na kratka, jednoznačna imena i provjeri rezultat.
- 🟡 Grupiraj odgovore po dobnoj skupini i izračunaj prosječnu ocjenu na skali 1–5; usporedi s ukupnim prosjekom.
- 🏆 Očisti skup podataka: ukloni duplikate, uskladi nazive kategorija, obradi prazna polja i napiši kratki dnevnik čišćenja s obrazloženjem svake promjene.

## Dalje

Tablica je sada uredna i opisana, ali još ne znamo što nam govori. Sljedeći korak je mjerenje: koliko su varijable povezane, kolika je razlika među skupinama i je li veća od slučajne. U cjelini [05. Statistika](05_statistika.md) učimo upravo to.

## Literatura

- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije: Razvoj velikih jezičnih modela i komunikacijskih agenata*. Rijeka: Filozofski fakultet u Rijeci. Open access: https://github.com/bperak/komunikacija_u_doba_ai
- Grus, J. (2019). *Data Science from Scratch*. O'Reilly.
- Bommasani et al. (2021). *On the Opportunities and Risks of Foundation Models*. arXiv:2108.07258
- Python za lingviste: https://github.com/nljubesi/python-for-linguists
- Pandas dokumentacija: https://pandas.pydata.org
