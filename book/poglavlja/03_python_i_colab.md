# Poglavlje 3: Python i Google Colab za humaniste

---

## Sažetak poglavlja

Ovo poglavlje vodi čitatelja od nula do prvog funkcionalnog analitičkog
okruženja. Ne pretpostavljamo nikakvo programersko iskustvo: polazimo od
toga zašto Python uopće, zatim kroz Google Colab uvodimo osnovne koncepte
jezika — varijable, tipove, liste, rječnike, petlje, uvjete i funkcije —
i završavamo s postavljanjem okruženja spremnog za analizu podataka i rad
s umjetnom inteligencijom (API ključevi, biblioteke). Svaki koncept prati
izvršni primjer i vježba.

---

## 3.1 Zašto Python (a ne Excel)?

Microsoft Excel je izvrstan alat za tablice — i svatko tko radi s podacima
trebao bi ga znati. No za podatkovnu znanost u kulturi Python ima ključne
prednosti:

| Zadatak | Excel | Python |
|---------|-------|--------|
| 1.000.000 redaka | Usporava, ograničeno | Bez problema |
| Automatizacija | Ručno, makroi | Skripta = ponovljivo |
| Reproducibilnost | Teško dokumentirati | Kod je dokumentacija |
| Tekstualni podaci | Ograničeno | NLP + LLM |
| AI integracija | Ne | LLM API, embedding, agenti |
| Verzije | Fino/grubo | Git — povijest svega |

Ključna riječ je **ponovljivost**: skripta koju jednom napišete može se
pokrenuti na drugom podatku, dijeliti s kolegom i provjeriti od strane
recenzenta. Excel proračunska tablica to ne omogućava na isti način.

> **Teorijski okvir — programiranje kao pismenost.**
> U digitalnoj humanistici programiranje se sve češće opisuje kao nova
> **pismenost** (*computational literacy*, diSessa 2000): sposobnost
> izražavanja ideja kroz kod, jednako temeljna kao pisanje. Ne morate
> postati programer — morate moći *izraziti* analitičku namjeru u jeziku
> koji stroj razumije. LLM-ovi ovu pismenost mijenjaju: danas namjeru
> možete izraziti prirodnim jezikom, a model generira kod. No razumijevanje
> onoga što kod radi i dalje je vaša odgovornost.

---

## 3.2 Google Colab kao kolaborativno okruženje

**Google Colab** (colab.research.google.com) je besplatna usluga koja
pokreće Python bilježnice u pregledniku. Zašto je idealan za ovu knjigu?

- **Nula instalacije** — sve radi u pregledniku, na bilo kojem računalu
- **Predinstalirane biblioteke** — pandas, numpy, matplotlib već postoje
- **GPU/TPU** — besplatno dostupan za veće modele
- **Suradnja** — dijeljenje i istovremeno uređivanje kao u Google Docs
- **Drive integracija** — bilježnice se čuvaju na Google Driveu
- **Cloud** — ništa ne ovisi o vašem računalu

### Struktura bilježnice

Bilježnica (notebook) sastoji se od **ćelija** dviju vrsta:

| Vrsta | Svrha |
|-------|-------|
| **Markdown** | Tekst, teorija, tablice, objašnjenja — dokumentacija |
| **Code** | Python kod koji se izvršava redoslijedom |

Dobra praksa: **teorija u Markdown ćelijama, kod u Code ćelijama.**
Bilježnica postaje i analiza i izvješće u jednom.

### Korisne naredbe (Colab)

- `Shift+Enter` — pokreni ćeliju i prijeđi na sljedeću
- `!` na početku ćelije — shell naredba (`!pip install ...`)
- `%` — magične naredbe (`%timeit`, `%matplotlib inline`)
- `userdata` — sigurno čuvanje tajni (API ključevi)

---

## 3.3 Osnove jezika: varijable, tipovi, strukture

### Varijable i tipovi

```python
ime = "kultura"        # str — tekst
broj = 42              # int — cijeli broj
prosjek = 3.14         # float — decimalni broj
istina = True          # bool — istina/laž

print(type(ime))       # <class 'str'>
print(broj + 8)        # 50
print(ime.upper())     # KULTURA
```

### Liste i rječnici — dva najvažnija tipa

**Lista** — uređeni niz:

```python
podaci = ["kino", "glazba", "muzeji"]
print(podaci[0])       # kino
podaci.append("ples")  # dodavanje
print(len(podaci))     # 4
```

**Rječnik (dict)** — parovi ključ:vrijednost, savršeno za podatke:

```python
katalog = {
    "id": 1,
    "naziv": "Portret ribara",
    "godina": 1920,
    "zbirka": "Moderna"
}
print(katalog["naziv"])      # Portret ribara
katalog["licenca"] = "CC-BY" # dodavanje
```

### Petlje i uvjeti

```python
for p in podaci:
    if p == "kino":
        print("kino je tu!")     # ispisuje se
    else:
        print(p)

# Brojanje s enumerate
for i, p in enumerate(podaci):
    print(i, p)                  # 0 kino, 1 glazba...
```

### Funkcije

```python
def prosjek(lista):
    """Vraća aritmetičku sredinu liste."""
    return sum(lista) / len(lista)

ocijene = [5, 4, 3, 5, 4]
print(prosjek(ocijene))          # 4.2
```

> **Napomena o list comprehensions.** Python ima elegantan način
> transformacije lista koji ćete stalno susretati u primjerima:
> ```python
> kvadriran = [x**2 for x in range(5)]   # [0, 1, 4, 9, 16]
> ```

---

## 3.4 Pandas: prvi susret

Pandas je biblioteka za tablične podatke — "Python Excel". Iako je
posvećeno poglavlje 4, ovdje radimo prvi susret jer je temelj svega.

```python
import pandas as pd

anketa = pd.DataFrame({
    "spol": ["Ž", "M", "Ž", "Ž"],
    "kino_godisnje": [12, 3, 8, 20],
    "citam_sati": [5, 1, 3, 7],
})

print(anketa.head())          # prvih 5 redaka
print(anketa.describe())      # statistika
print(anketa["kino_godisnje"].mean())  # 10.75
```

**DataFrame** = retci (opažanja) + stupci (varijable). Sva analiza u ovoj
knjizi počiva na njemu.

---

## 3.5 Postavljanje okruženja i API ključeva

Za rad s AI alatima (pogl. 8-11) trebat ćemo pristup LLM API-ju.
Koristimo Google Gemini (besplatan tier je dovoljan za sve primjere).

### Korak 1: Dobivanje API ključa

1. Otvorite https://aistudio.google.com
2. Prijavite se s Google računom
3. Kliknite "Get API key" → "Create API key"
4. Kopirajte ključ (čuvajte ga kao lozinku!)

### Korak 2: Sigurno čuvanje ključa u Colabu

```python
from google.colab import userdata
userdata.set("GEMINI_API_KEY", "OVDJE_KLJUC")
```

### Korak 3: Instalacija i spajanje

```python
!pip install -q google-generativeai pandas numpy matplotlib seaborn scikit-learn

import os
import google.generativeai as genai
from google.colab import userdata

genai.configure(api_key=userdata.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

odgovor = model.generate_content("Pošto je 23 + 19?")
print(odgovor.text)    # 42
```

> **Rubrika "Što ako ne radi?"**
> - `ModuleNotFoundError` → instalirajte biblioteku: `!pip install -q ime`
> - `API key not valid` → provjerite jeste li kopirali cijeli ključ
> - `userdata` ne radi → pokrenite ćeliju s `userdata.set` prvo
> - Colab "runtime disconnected" → Runtime → Restart session

---

## 3.6 Radni tijek istraživača (best practices)

1. **Bilježnica kao izvješće:** Markdown uvod (što istražujem) → kod → Markdown interpretacija.
2. **Komentari objašnjavaju "zašto", ne "što"** — kod sam kaže što radi.
3. **Sve verzije u Git/GitHub** — povijest analize.
4. **Podaci u jednom folderu** — `data/`, `scripts/`, `results/`.
5. **Reproducibilnost:** `!pip freeze > requirements.txt` na kraju projekta.
6. **AI kao pomoć:** LLM generira prvi nacrt koda → vi provjeravate i prilagođavate.

---

## Vježbe

### 🟢 Osnovna
1. Napravite DataFrame s podacima o 5 kulturnih ustanova (naziv, grad,
   godina osnivanja, broj posjetitelja). Ispišite `head()`, `describe()`
   i prosjek posjetitelja.
2. Napišite funkciju `kategorija(dob)` koja vraća "adolescent" (13-19),
   "mladi" (20-29), "odrasli" (30+) — i testirajte je na 5 vrijednosti.

### 🟡 Srednja
3. Iz Google Forms ankete izvezite CSV i učitajte ga u Pandas.
   Koliko redaka/stupaca? Koji su tipovi? Koliko null vrijednosti?
4. Napišite petlju koja prolazi kroz sve stupce i ispisuje broj
   jedinstvenih vrijednosti svakog od njih.

### 🏆 Napredna
5. Pomoću LLM-a (Gemini) generirajte Python kod koji iz vašeg CSV-a
   računa prosjek po kategorijama (npr. kino posjeti po spolu).
   Pokrenite kod, provjerite rezultat, a zatim ručno napišite istu analizu.
   Usporedite — što je LLM dobro napravio, što nije?

---

## Sažetak i ključni pojmovi

- Python je alat za ponovljivu, automatiziranu i AI-spremnu analizu.
- Google Colab: bilježnica u pregledniku, nula instalacije, suradnja.
- Osnove: varijable, liste, rječnici, petlje, uvjeti, funkcije.
- Pandas DataFrame: retci = opažanja, stupci = varijable.
- API ključ se čuva sigurno (userdata), nikad u kodu.
- Radni tijek: bilježnica kao izvješće + Git + dokumentacija.

**Ključni pojmovi:** Python, Colab, notebook, DataFrame, varijabla, lista,
rječnik, petlja, funkcija, API ključ, reproducibilnost.

---

## Literatura

- Grus, J. (2019). *Data Science from Scratch* (2. izd.). O'Reilly. (pogl. 1-2)
- McKinney, W. (2022). *Python for Data Analysis* (3. izd.). O'Reilly.
- diSessa, A. A. (2000). *Changing Minds: Computers, Learning, and Literacy*. MIT Press.
- Google Colab: https://colab.research.google.com
- Python za lingviste: https://github.com/nljubesi/python-for-linguists
