# 03. Python i Google Colab — osnove

> **U ovoj cjelini.** Postavit ćete radno okruženje u pregledniku i napisati prve naredbe u Pythonu —
varijable, liste, rječnike, petlje i funkcije — bez prethodnog programerskog
iskustva. Nakon cjeline moći ćete u Colabu učitati tablicu i izračunati
osnovne mjere.
> **Ishodi:** DSK-7 Svladati osnovne statističko-analitičke funkcije data-science programa.
> **Uz ovu cjelinu idu:** skripta [`scripts/01_pandas_osnove.py`](../scripts/01_pandas_osnove.py), bilježnica [`colab/DSK_analiza_upitnika_jednostavno.ipynb`](../colab/DSK_analiza_upitnika_jednostavno.ipynb) i [cjelina 04: Pandas — tablični podaci](04_pandas_tablice.md).

**Kolegij:** Data Science u kulturi | 2026./2027.

## Zašto Python?

Python je najčešći jezik podatkovne znanosti i digitalne humanistike. Ima tri
prednosti presudne za kulturna istraživanja: čitljivu sintaksu, velik ekosustav biblioteka i zajednicu koja
uz znanstvene radove objavljuje i kod.

- Standard u data science-u i digitalnoj humanistici
- Čitljiva sintaksa, ogroman ekosustav biblioteka
- pandas, numpy, matplotlib, scikit-learn, nltk, google-genai

Usporedba s proračunskom tablicom pokazuje gdje leži razlika: Python podnosi
mnogo veće tablice, analizu zapisuje kao skriptu, kod je ujedno dokumentacija
postupka, a uz njega dolaze obrada teksta i API velikih jezičnih modela. Ključna riječ je **ponovljivost**: skripta se pokreće na novim podacima i može
se provjeriti. Programiranje se zato opisuje kao **nova pismenost** — sposobnost izražavanja
analitičke namjere u jeziku koji stroj razumije. Ne morate postati programer;
morate moći zapisati što želite izračunati. Veliki jezični modeli taj prag
spuštaju, ali razumijevanje onoga što kod radi ostaje vaša odgovornost.

## Google Colab

Google Colab je besplatno **kolaborativno mrežno sučelje** za izvršavanje
Python koda u pregledniku — idealno za nastavu i istraživanje:

- https://colab.research.google.com
- Nula instalacije (sve radi u pregledniku)
- GPU/TPU dostupni (za veće modele)
- Dijeljenje i suradnja u stvarnom vremenu
- Povezivanje s Google Driveom

Bilježnica se sastoji od ćelija dviju vrsta: **Markdown** ćelije nose tekst,
teoriju i tablice, a **Code** ćelije Python koji se izvršava redoslijedom
kojim ga pokrećete. Dobra je praksa držati teoriju u Markdown ćelijama, a kod u
Code ćelijama, pa bilježnica postaje istovremeno analiza i izvješće. Nekoliko
je naredbi korisno znati odmah: `Shift+Enter` pokreće ćeliju i prelazi na
sljedeću, znak `!` na početku izvršava ljusku naredbu (`!pip install ...`), a
znak `%` uvodi magične naredbe bilježnice.

Varijable žive samo dok traje sesija: nakon duže neaktivnosti ili ponovnog
pokretanja okruženja (*Runtime → Restart session*) sve se iz memorije briše.
Bilježnicu i podatke zato čuvajte na Driveu ili u GitHub repozitoriju, a
analizu organizirajte tako da se izvršava od početka do kraja.

## Osnovni koncepti Pythona

```python
# Varijable i tipovi
ime = "kultura"
broj = 42
prosjek = 3.14
istina = True

# Liste i rječnici
podaci = ["kino", "glazba", "muzeji"]
katalog = {"id": 1, "naziv": "Portret", "godina": 1920}

# Petlje i uvjeti
for p in podaci:
    if p == "kino":
        print("kino je tu")

# Funkcije
def prosjek(lista):
    return sum(lista) / len(lista)
```

Svaki dio ima jasnu namjenu. **Varijabla** je ime pod kojim je vrijednost
spremljena: `ime` je tekst (`str`), `broj` cijeli broj (`int`), `prosjek`
decimalni broj (`float`), `istina` logička vrijednost (`bool`). **Lista** je
uređeni niz s indeksom od nule — `podaci[0]` je "kino". **Rječnik** čuva parove
ključa i vrijednosti i najbliži je zapisu iz kataloga. **Petlja** `for` ponavlja
radnju, **uvjet** `if` odlučuje hoće li se izvršiti, a **funkcija** je imenovani
postupak. Uvlačenje redaka dio je sintakse: tijelo petlje, uvjeta i funkcije
mora biti uvučeno.

Na kulturnom primjeru to izgleda ovako:

```python
# Brojanje žanrova: rječnik, petlja i list comprehension
zanrovi = ["drama", "komedija", "drama", "dokumentarac", "komedija"]

ucestalost = {}
for z in zanrovi:
    ucestalost[z] = ucestalost.get(z, 0) + 1

print(ucestalost)
print(sorted(ucestalost.items(), key=lambda par: par[1], reverse=True))
print([z.upper() for z in zanrovi])
```

Prvi ispis daje frekvencije žanrova, drugi ih poreda od najčešćega prema
rjeđemu, a treći pokazuje *list comprehension* — sažeto preslikavanje liste u
novu listu. Isti obrazac (prođi kroz zapise, prebroji pojavu) koristit ćete u
svakoj analizi upitnika.

## Struktura Colab bilježnice

- **Markdown ćelije** — teorija, objašnjenja, tablice
- **Code ćelije** — izvršni Python
- **@title** — naslov za skrivanje koda
- **userdata** — sigurno čuvanje API ključeva. Ključ se izrađuje na `https://aistudio.google.com` **prije nastave** i svatko koristi svoj (kvota se mjeri po projektu, ne po ključu).

Oznaka `@title` u prvoj liniji ćelije stvara sklopivi naslov, pa se pomoćne
ćelije mogu sakriti i bilježnica ostaje čitljiva. Funkcija `userdata` čuva
tajne izvan koda: API ključ se upiše u sigurno spremište Colaba i dohvaća
pozivom, umjesto da stoji u tekstu bilježnice. To je i sigurnosno i praktično
pravilo — ključ koji je jednom zalijepljen u ćeliju i podijeljen s kolegama
treba smatrati izloženim. Svaki student koristi vlastiti ključ s Google AI
Studija, jer se kvota mjeri po projektu, a ne po ključu.

## Postavljanje

```python
!pip install -q pandas numpy matplotlib seaborn google-genai
import pandas as pd
import numpy as np
```

Biblioteke pandas, numpy i matplotlib u Colabu su predinstalirane, pa
instalacijska naredba služi za dodatne pakete. Prvi susret s tablicom:

```python
import pandas as pd

anketa = pd.DataFrame({
    "spol": ["Ž", "M", "Ž", "Ž"],
    "kino_godisnje": [12, 3, 8, 20],
    "citam_sati": [5, 1, 3, 7],
})

print(anketa.head())
print(anketa.describe().round(2))
print(anketa["kino_godisnje"].mean())
```

Rječnik pretvaramo u tablicu jednim pozivom, stupce dohvaćamo imenom, a mjere
računamo gotovim funkcijama: `head()` prikazuje prvih pet redaka, `describe()`
osnovnu statistiku, a `mean()` prosjek stupca. Ako se pojavi poruka
`ModuleNotFoundError`, nedostaje biblioteka koju treba instalirati naredbom
`!pip install -q ime`; ako se pojavi `NameError`, varijabla nije definirana u
trenutku izvršavanja.

## Ishodi učenja (7)

- Svladati osnovne statističko-analitičke funkcije data-science programa.

## Ključni pojmovi

| Pojam | Značenje u jednoj rečenici |
|-------|----------------------------|
| Python | Programski jezik čitljive sintakse i bogatog ekosustava biblioteka za podatke. |
| Google Colab | Besplatno mrežno okruženje koje izvršava Python bilježnice u pregledniku. |
| Bilježnica (notebook) | Dokument s Markdown i Code ćelijama, istovremeno analiza i izvješće. |
| Varijabla | Ime pod kojim je vrijednost spremljena u memoriji. |
| Tip podatka | Vrsta vrijednosti: tekst, cijeli broj, decimalni broj ili logička vrijednost. |
| Lista | Uređeni niz vrijednosti kojima pristupamo indeksom od nule. |
| Rječnik (dict) | Skup parova ključa i vrijednosti, najbliži zapisu iz kataloga. |
| Petlja i uvjet | Naredbe koje ponavljaju radnju i odlučuju hoće li se izvršiti. |
| Funkcija | Imenovani postupak koji primljene vrijednosti pretvara u rezultat. |
| DataFrame | Tablica s retcima (opažanjima) i stupcima (varijablama) u biblioteci pandas. |

## Provjeri razumiješ

1. Navedi dvije prednosti Pythona pred proračunskom tablicom i objasni zašto je ponovljivost važna u istraživanju.
2. Čemu služe Markdown, a čemu Code ćelije u bilježnici?
3. Što će ispisati `print(podaci[1])` ako je `podaci = ["kino", "glazba", "muzeji"]` i zašto?
4. Što se događa s varijablama u Colabu nakon ponovnog pokretanja okruženja i kako se na to pripremiti?

<details><summary>Odgovori</summary>

1. Python podnosi veće tablice i analizu zapisuje kao skriptu koja se može ponoviti
i provjeriti; uz to nudi obradu teksta i AI alate. Ponovljivost je važna jer
omogućuje da drugi istraživač dobije iste rezultate.
2. Markdown ćelije nose tekst, teoriju i tablice, a Code ćelije Python koji se izvršava; zajedno daju dokument koji je i analiza i izvješće.
3. Ispisuje "glazba", jer indeksiranje počinje od nule: `podaci[0]` je "kino", a `podaci[1]` drugi član liste.
4. Sve varijable iz memorije se brišu, pa ćelije treba pokrenuti od početka; zato
se bilježnica organizira tako da se izvršava odozgo prema dolje.

</details>

## Praktično

- Colab: `colab/DS_KULT_Podatkovna_znanost_u_kulturi.ipynb` (ćelija "Instalacija i setup")
- 🟢 Otvorite bilježnicu u Colabu, pokrenite ćeliju s instalacijom i uvezi
  biblioteka te ispišite tipove četiriju varijabli i provjerite da ste dobili
  `str`, `int`, `float` i `bool`.
- 🟢 Napravite tablicu s podacima o pet kulturnih ustanova (naziv, grad,
  godina osnivanja, broj posjetitelja). Ispišite `head()`, `describe()` i
  prosjek broja posjetitelja.
- 🟡 Napišite funkciju `kategorija(dob)` koja vraća "adolescent" (13-19),
  "mladi" (20-29) ili "odrasli" (30 i više) i pozovite je na pet vrijednosti.
- 🟡 Izvezite anketu iz Google Formsa u CSV i učitajte je u bilježnicu: koliko ima
redaka i stupaca, koji su tipovi i koliko vrijednosti nedostaje? Odgovore
zapišite u Markdown ćeliju.
- 🏆 Neka vam LLM generira kod koji iz vašeg CSV-a računa prosjek po
  kategorijama (npr. posjeti kinu prema spolu). Pokrenite kod, provjerite
  rezultat na uzorku ručno, a zatim istu analizu napišite sami. Zapišite što je
  model dobro napravio, a što ste morali ispraviti.

## Dalje

Sljedeći je korak sustavni rad s tablicama: u
[cjelini 04](04_pandas_tablice.md) učitat ćemo stvarne podatke u pandas,
filtrirati retke, grupirati ih i izračunati deskriptivnu statistiku koju ćemo
kasnije prikazati grafikonima.

## Literatura

- Google Colab: https://colab.research.google.com
- Grus, J. (2019). *Data Science from Scratch*. O'Reilly. (1-2. poglavlje)
- McKinney, W. (2022). *Python for Data Analysis* (3. izd.). O'Reilly.
- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije*. FFRI Rijeka.
  https://github.com/bperak/komunikacija_u_doba_ai
