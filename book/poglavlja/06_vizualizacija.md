# Poglavlje 6: Vizualizacija podataka

---

## Sažetak poglavlja

"Graf vrijedi tisuću riječi" — ali loš graf vrijedi tisuću pogrešnih
zaključaka. Ovo poglavlje uči vizualizaciju kao **argumentativnu vještinu**:
kako odabrati pravi tip grafa, kako ga konstruirati pošteno i kako ga
interpretirati. Radimo s Matplotlibom i Seabornom u Colabu, a poseban
odjeljak posvećen je ulozi LLM-a u generiranju i interpretaciji grafova.

---

## 6.1 Zašto vizualizacija?

Vizualizacija ima tri funkcije u istraživanju:

1. **Eksploracija** — otkrivanje obrazaca prije formalne analize
   (što se u podacima uopće događa?)
2. **Komunikacija** — prenošenje rezultata publici
3. **Verifikacija** — provjera pretpostavki (je li raspodjela normalna?
   ima li ekstrema? jesu li podaci "čisti"?)

> **Teorijski okvir — vizualizacija kao retorika.**
> Grafovi nisu neutralni prikazi stvarnosti — oni su **retorički izbori**.
> Tufte (2001) upozorava na *chartjunk*: svaki ukras koji ne nosi
> informaciju smanjuje vjerodostojnost. Cairo (2019) uvodi pojam
> **"poštenog" grafa**: proporcije moraju biti točne, skale ne smiju
> varati, kontekst se ne smije skrivati. Kada čitate bilo koji graf u
> medijima, pitajte: što mi ovaj graf NE pokazuje?

---

## 6.2 Pravila poštene vizualizacije

1. **Naslov govori što graf pokazuje** (ne samo "Graf 1")
2. **Osi jasno označene** s jedinicama ("broj posjeta godišnje")
3. **Skala ne zavarava** — ne počinji y-os na 400 ako podaci kreću od 401
4. **Kontekst** — navedi N (broj opažanja), izvor, godinu
5. **Boja s namjerom** — ne paleta duginih boja bez razloga
6. **Čitljivost** — dovoljno velik font, bez okomitog teksta
7. **Iskrenost** — ako je raspršenje veliko, ne skrivaj ga

### Uobičajene manipulacije (na što paziti)

| Trik | Primjer | Prepoznavanje |
|------|---------|---------------|
| Truncirana y-os | "Skok od 10 %" koji je zapravo 1 % | Provjeri početak osi |
| 3D efekti | Grafički ukrasi zamagljuju proporcije | 2D je čitljiviji |
| Pogrešna vrsta grafa | Pita graf za trendove | Trend = linija |
| Različite skale | Usporedba dvije serije na različitim osima | Provjeri obje osi |

---

## 6.3 Matplotlib i Seaborn

### Postavljanje (Colab)

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Tamna tema (kakva je ova knjiga 😉)
plt.style.use("dark_background")
sns.set_palette("husl")

# Prikaz unutar bilježnice
%matplotlib inline
```

### Vrste grafova i kada ih koristiti

| Graf | Pitanje na koje odgovara | Primjer u kulturi |
|------|--------------------------|-------------------|
| **Histogram** | Kako je raspoređena jedna varijabla? | Raspodjela dobi ispitanika |
| **Bar chart** | Usporedba kategorija? | Posjećenost po zbirkama |
| **Scatter** | Odnos dviju numeričkih? | Kino vs. čitanje |
| **Box plot** | Raspršenost po grupama? | Kino posjeti po spolu |
| **Line chart** | Trend kroz vrijeme? | Posjećenost po mjesecima |
| **Heatmap** | Matrica korelacija? | Sve korelacije odjednom |

### Histogram i bar chart

```python
# Histogram
plt.figure(figsize=(8, 5))
sns.histplot(anketa["kino_godisnje"], bins=8, color="#4fc3f7")
plt.title("Raspodjela godišnjih kino posjeta (N=45)")
plt.xlabel("broj posjeta godišnje")
plt.ylabel("broj ispitanika")
plt.show()

# Bar chart s pogreškama
sns.barplot(data=anketa, x="spol", y="kino_godisnje",
            errorbar="sd", palette="husl")
plt.title("Prosječni kino posjeti po spolu (± SD)")
plt.show()
```

### Scatter i box plot

```python
# Scatter + regresijska linija
sns.regplot(data=anketa, x="kino_godisnje", y="citam_sati",
            scatter_kws={"alpha": 0.6})
plt.title("Odnos kino posjeta i čitanja")
plt.show()

# Box plot po grupama
sns.boxplot(data=anketa, x="spol", y="kino_godisnje")
plt.title("Raspršenost kino posjeta po spolu")
plt.show()
```

### Line chart za trendove

```python
posjete = pd.DataFrame({
    "mjesec": ["10", "11", "12", "1", "2", "3", "4", "5", "6"],
    "posjetitelji": [1200, 900, 1500, 800, 950, 1100, 1300, 1000, 700],
})
sns.lineplot(data=posjete, x="mjesec", y="posjetitelji", marker="o")
plt.title("Posjećenost muzeja po mjesecima (2025/26)")
plt.ylabel("broj posjetitelja")
plt.show()
```

### Spremanje grafa

```python
plt.savefig("posjete.png", dpi=150, bbox_inches="tight")
```

---

## 6.4 Vizualizacija mreža (dodatak)

Kulturne pojave su često **mrežne** (suradnje, citiranja, zajednice).
Za mreže koristimo NetworkX:

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([
    ("muzej A", "galerija B"), ("muzej A", "kazalište C"),
    ("galerija B", "kazalište C"), ("kazalište C", "klub D"),
])

plt.figure(figsize=(6, 6))
nx.draw_networkx(G, with_labels=True, node_color="#4fc3f7",
                 node_size=1500, font_size=10)
plt.axis("off")
plt.show()
```

> **Mrežna analiza** (SNA) tema je koja zaslužuje zaseban kolegij — ovdje
> je spominjemo kao proširenje vizualnih mogućnosti. Ključni pojmovi:
> čvor (node), veza (edge), stupanj (degree), zajednica (community).

---

## 6.5 LLM i vizualizacija

### LLM generira graf iz opisa

```python
prompt = """
Napiši Python (pandas + seaborn) koji crta box plot: 'kino_godisnje'
po 'spol' iz DataFramea 'df'. Tamna tema, naslov, označene osi. Samo kod.
"""
kod = model.generate_content(prompt).text
exec(kod)   # ali provjeri i prilagodi!
```

### LLM interpretira graf

```python
opis = """Histogram kino posjeta: većina ispitanika (N=45) ima 0-10 posjeta,
mali broj 20+, prosjek 11, medijan 8.5. Što to govori o kulturnim navikama?"""
print(model.generate_content(opis).text)
```

### Granice LLM vizualizacije

- Model **ne vidi** graf (osim ako ne koristi multimodalni model) — opisuje
  ono što mu date, ne ono što je stvarno na slici
- Generirani kod često treba popravke (veličina, boje, oznake)
- **LLM ne jamči poštenost** — provjerite skale i proporcije sami

> **Rubrika "Što ako ne radi?"**
> - `RuntimeError: display hook not found` → pokrenite `%matplotlib inline`
> - Graf je prazan → jeste li pozvali `plt.show()`?
> - Crne kutije umjesto teksta → instalirajte font: `!apt-get install fonts-crosextra-carlito`
> - `savefig` prazan → spremajte prije `plt.show()` ili s `bbox_inches="tight"`

---

## Praktikum: izvješće u 3 grafa

Cilj: tri grafa koja govore priču o jednom skupu podataka.

```python
# 1. Tko su ispitanici? (demografija)
sns.histplot(anketa["dob"], bins=10, color="#4fc3f7")
plt.title(f"Raspodjela dobi (N={len(anketa)})")
plt.show()

# 2. Što rade? (ponašanje po kategorijama)
sns.boxplot(data=anketa, x="spol", y="kultura_indeks")
plt.title("Kulturni indeks po spolu")
plt.show()

# 3. Kako se povezano? (odnos dvije varijable)
sns.regplot(data=anketa, x="kino_godisnje", y="koncerti_godisnje",
            scatter_kws={"alpha": 0.6})
plt.title("Kino i koncerti: povezanost?")
plt.show()
```

---

## Vježbe

### 🟢 Osnovna
1. Za svoju anketu napravite: histogram dobi, bar chart po spolu,
   scatter dviju numeričkih varijabli. Dodajte naslove i oznake osi.
2. Spremite grafove kao PNG (150 dpi).

### 🟡 Srednja
3. Box plot iste varijable po dvije kategorije. Što vidite u raspršenosti?
4. Heatmap korelacija za 4+ numeričke varijable. Koji je najjači par?
5. Line chart: trend kroz mjesece (ako imate vremenski niz) ili preko
   javnih podataka (npr. posjećenost muzeja).

### 🏆 Napredna
6. Pomoću LLM-a generirajte graf iz opisa, pokrenite ga i **popravite**
   najmanje 3 stvari (naslov, boje, oznake, skala).
7. Pronađite u medijima jedan **manipulativan graf** i prekrojite ga
   pošteno (ista logika, ispravna skala). Usporedite poruke.

---

## Sažetak i ključni pojmovi

- Vizualizacija = eksploracija + komunikacija + verifikacija.
- Pošteni graf: točne proporcije, iskrene skale, jasne oznake, kontekst (N, izvor).
- Histogram (raspodjela), bar (kategorije), scatter (odnos), box (grupe),
  line (trend), heatmap (korelacije).
- Boja i veličina su argumenti, ne ukrasi.
- LLM generira i interpretira grafove, ali ne jamči poštenost — provjerite.

**Ključni pojmovi:** histogram, bar chart, scatter plot, box plot, line
chart, heatmap, chartjunk, pošteni graf, Tufte, truncirana os.

---

## Literatura

- Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2. izd.). Graphics Press.
- Cairo, A. (2019). *How Charts Lie*. W. W. Norton.
- Healy, K. (2018). *Data Visualization: A Practical Introduction*. Princeton University Press.
- VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly. (open access)
