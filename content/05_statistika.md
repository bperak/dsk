# 05. Statistika — deskriptivna analiza i korelacije

**Kolegij:** Data Science u kulturi | 2026./2027.

> **U ovoj cjelini.** Učimo sažeti podatke brojkama i ispravno čitati povezanost među varijablama. Razlikujemo mjere sredine i raspršenosti, računamo korelacije, tumačimo p-vrijednost i veličinu učinka te učimo zašto korelacija sama po sebi ne dokazuje uzročnost.
>
> **Ishodi:** **DSK-5** Analizirati kvantitativne i kvalitativne tipove podataka te primijeniti postupke statističke analize.
>
> **Uz ovu cjelinu idu:** skripta [`scripts/02_statistika_korelacije.py`](../scripts/02_statistika_korelacije.py), bilježnica [`colab/DSK_analiza_upitnika_jednostavno.ipynb`](../colab/DSK_analiza_upitnika_jednostavno.ipynb) i sljedeća cjelina [06. Vizualizacija](06_vizualizacija.md).

Statistika je način da iz mnogo pojedinačnih odgovora izvučemo provjerljivu tvrdnju. U kulturološkom istraživanju to su najčešće ankete o kulturnim navikama i evidencije posjećenosti. Prije računanja valja znati kakav je podatak: kategorija (žanr), uređena skala (ocjena 1–5) ili broj s pravim rasponom (broj posjeta).

## Deskriptivna statistika

Opisuje podatke brojkama:

| Mjera | Značenje |
|-------|----------|
| Srednja vrijednost (mean) | Prosjek |
| Medijan | Srednja vrijednost sortiranih podataka |
| Mod | Najčešća vrijednost |
| Standardna devijacija | Raspršenost oko prosjeka |
| Min/Max | Raspon |

Prosjek je koristan kada su podaci uravnoteženi, ali ga nekoliko velikih vrijednosti lako povuče. Ako sto posjetitelja izložbe dođe jednom, a petorica pedeset puta, prosjek skače, dok medijan ostaje blizu tipičnog posjetitelja. Zato uz prosjek uvijek navodimo i medijan.

Standardna devijacija govori koliko su vrijednosti raspršene: dvije ustanove mogu imati isti prosjek, ali jedna radi ravnomjerno, a druga ima prazne dane i nabijene vikende.

Kod skale 1–5 prosjek pretpostavlja da je razlika između 1 i 2 jednaka razlici između 4 i 5, što nije nužno točno, pa uz njega navodimo medijan i raspodjelu odgovora.

```python
import pandas as pd

df = pd.read_csv("data/demo_odgovori.csv")

print(df[["kino", "citam", "ocjena_programa"]].describe().round(2))
print(df["ocjena_programa"].median())
print(df["žanr"].value_counts().head(5))
```

## Korelacija

**Korelacija** mjeri povezanost dviju varijabli (od -1 do +1):

- +1: savršena pozitivna povezanost
- 0: nema povezanosti
- -1: savršena negativna povezanost

```python
import scipy.stats as stats
r, p = stats.pearsonr(df["kino"], df["citam"])
```

Pearsonov koeficijent mjeri linearnu povezanost brojčanih varijabli; za uređene skale i raspodjele s ekstremima bolji je Spearmanov, koji radi s rangovima.

```python
rho, p = stats.spearmanr(df["ocjena_programa"], df["ocjena_prostora"])
matrica = df[["kino", "citam", "koncerti"]].corr(method="pearson")
print(matrica.round(3))
```

**⚠️ Važno: korelacija ≠ uzročnost!**

Npr. "kino" i "koncerti" mogu korelirati jer oboje odražavaju opću kulturnu
aktivnost (treća varijabla), ne zato što jedno uzrokuje drugo.

### Kada je korelacija važna

Korelacija nosi težinu kada je povezanost unaprijed pretpostavljena, a ne pronađena pretraživanjem mnogih parova; kada je uzorak dovoljno velik; kada je koeficijent umjeren ili jak; kada se rezultat ponavlja u podskupinama i na novim podacima; i kada nije posljedica jednog ili dva ekstremna opažanja. Gruba orijentacija: do 0,3 slab, 0,3–0,5 umjeren, iznad 0,5 jak, uz napomenu da granice ovise o temi i instrumentu.

### Kada korelacija nije važna

Koeficijent ne treba precijeniti kada je uzorak malen; kada povezanost nije linearna nego, primjerice, u obliku slova U; kada su vrijednosti stisnute u uski raspon (anketa u kojoj gotovo svi daju 4 ili 5); kada je jedna varijabla izvedena iz druge; ili kada se ispituje dvadesetak parova odjednom, jer će neki slučajno izgledati „značajan“. Korelacija ne govori ništa o smjeru odnosa ni o mehanizmu koji ga objašnjava.

### Zašto korelacija nije uzročnost

Povezanost bez uzročnosti obično ima jedno od četiri objašnjenja. Prvo je treća varijabla: posjet kina i posjet koncertima rastu zajedno jer oboje mjere sklonost kulturnom izlasku. Drugo je obrnut smjer: veća posjećenost izložbe korelira s brojem medijskih objava, ali objave su nastale iz izložbe, ne obrnuto. Treće je odabir uzorka: anketa o kazalištu provedena u kazališnom foajeu daje povezanost koja ne vrijedi za grad. Četvrto je slučajnost, vjerojatnija što je uzorak manji. Tvrdnja o uzročnosti zato se izvodi iz nacrta istraživanja — eksperimenta, ponovljenih mjerenja ili usporedbe uz kontrolu trećih varijabli — a ne iz koeficijenta.

```python
podskup = df[df["dob"] < 30]
r_mladi, p_mladi = stats.pearsonr(podskup["kino"], podskup["koncerti"])
print(f"mladi: r = {r_mladi:+.3f}, p = {p_mladi:.4f}")
```

## Statistička značajnost (p-vrijednost)

- p < 0.05 = statistički značajno (5% rizik pogreške)
- p ≥ 0.05 = nije značajno
- Značajnost ovisi o veličini uzorka

p-vrijednost odgovara na usko pitanje: koliko bi ovakvih ili ekstremnijih podataka bilo vjerojatno kada među varijablama ne bi bilo povezanosti. Nije vjerojatnost da je hipoteza točna, pa mala p-vrijednost ne znači i da je povezanost važna. U velikom uzorku i nevažna povezanost može prijeći prag značajnosti, dok u malom uzorku i jasna povezanost može ostati ispod njega.

```python
m = df[df["spol"] == "M"]["kino"]
z = df[df["spol"] == "Ž"]["kino"]
t, p = stats.ttest_ind(m, z)
print(f"t = {t:.3f}, p = {p:.4f}, M: {m.mean():.2f}, Ž: {z.mean():.2f}")
```

t-test uspoređuje prosjek dviju skupina. Rezultat čitamo s opisnim brojkama: ako su prosjeci 12,1 i 12,3 posjeta uz p = 0,031, razlika je statistički značajna, ali praktično ne mijenja ništa.

## AI u statistici

LLM može pomoći: generirati analitički kod iz pitanja, interpretirati rezultate,
predložiti testove. **Ali konačna interpretacija je na istraživaču.**

Model je koristan u tri posla: prevodi istraživačko pitanje u naredbe, objašnjava što pojedini koeficijent znači i predlaže test primjeren tipu podatka. Njegovi su odgovori prijedlozi, ne nalazi: može pozvati test koji ne odgovara podatku, pretpostaviti stupac koji ne postoji ili proglasiti razliku važnom samo zato što je p-vrijednost mala. Zato tražimo i provjeru pretpostavki, rezultat računamo sami na vlastitim podacima, a osobne podatke iz ankete prije slanja u vanjski alat anonimiziramo.

## Ishodi učenja (5)

- Analizirati kvantitativne i kvalitativne tipove podataka te primijeniti
  postupke statističke analize.

## Ključni pojmovi

| Pojam | Značenje |
|-------|----------|
| Srednja vrijednost | zbroj vrijednosti podijeljen brojem opažanja |
| Medijan | vrijednost u sredini sortiranih podataka |
| Mod | najčešća vrijednost, korisna za kategorije |
| Standardna devijacija | prosječno odstupanje od sredine |
| Pearsonov koeficijent | linearna povezanost dviju varijabli |
| Spearmanov koeficijent | povezanost rangova, za uređene skale |
| p-vrijednost | vjerojatnost ovakvih podataka bez povezanosti |
| Veličina učinka | koliko je povezanost jaka |
| Zbunjujuća varijabla | treći čimbenik koji objašnjava obje varijable |
| Uzročnost | utvrđuje se nacrtom istraživanja, ne koeficijentom |

## Provjeri razumiješ

1. Zašto je kod broja posjeta izložbi medijan pouzdaniji od prosjeka?
2. Korelacija između posjeta kinu i posjeta koncertima iznosi 0,48. Znači li to da kino potiče odlazak na koncerte?
3. p-vrijednost iznosi 0,42. Što ova brojka govori, a što ne govori?
4. Zašto mala p-vrijednost u velikom uzorku nije sama po sebi važan nalaz?

<details><summary>Odgovori</summary>

1. Posjećenost ima dugi rep: većina ljudi dolazi rijetko, a mali broj posjetitelja dolazi vrlo često i povlači prosjek prema gore. Medijan pokazuje koliko posjeta ima tipičan posjetitelj i na njega ekstremi ne utječu.

2. Ne. Umjerena pozitivna korelacija samo opisuje da se vrijednosti kreću zajedno. Najvjerojatnije je objašnjenje treća varijabla — sklonost kulturnom izlasku ili gradska kulturna ponuda. Za tvrdnju o uzročnosti potreban je drukčiji nacrt istraživanja.

3. p = 0,42 znači da su ovakvi podaci uobičajeni i kada među varijablama nema povezanosti, pa nalaz ne daje oslonac za tvrdnju o povezanosti. Ne govori da povezanosti nema, nego da je ovaj uzorak ne pokazuje.

4. Kako uzorak raste, i vrlo slab koeficijent može postati značajan. Zato uz p-vrijednost navodimo veličinu učinka, broj opažanja i interval pouzdanosti te procijenimo je li razlika sadržajno relevantna.

</details>

## Praktično

Povezana skripta i bilježnica: [`scripts/02_statistika_korelacije.py`](../scripts/02_statistika_korelacije.py), [`colab/DSK_analiza_upitnika_jednostavno.ipynb`](../colab/DSK_analiza_upitnika_jednostavno.ipynb).

- 🟢 Za tri numerička stupca iz ankete izračunaj prosjek, medijan i standardnu devijaciju.
- 🟢 Prikaži raspodjelu ocjena programa (1–5) i usporedi mod s prosjekom.
- 🟡 Izračunaj Pearsonovu korelaciju za par varijabli i napiši dvije rečenice tumačenja: što povezanost pokazuje, a što ne.
- 🟡 Ponovi korelaciju na podskupu (npr. ispitanici mlađi od 30) i provjeri je li smjer stabilan.
- 🏆 Formuliraj tvrdnju o kulturnim navikama, nađi korelaciju koja je podupire i napiši dva alternativna objašnjenja (treća varijabla, obrnut smjer, odabir uzorka).

## Dalje

Brojke smo izračunali, ali ih publika ne čita kao tablice. Sljedeći korak je prijevod nalaza u sliku koja pošteno i čitljivo prenosi raspodjelu i odnose. U cjelini [06. Vizualizacija](06_vizualizacija.md) učimo koje grafove koristimo i koje pogreške pritom izbjegavamo.

## Literatura

- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije: Razvoj velikih jezičnih modela i komunikacijskih agenata*. Rijeka: Filozofski fakultet u Rijeci. Open access: https://github.com/bperak/komunikacija_u_doba_ai
- Grus, J. (2019). *Data Science from Scratch*. O'Reilly.
- Bommasani et al. (2021). *On the Opportunities and Risks of Foundation Models*. arXiv:2108.07258
- Python za lingviste: https://github.com/nljubesi/python-for-linguists
- SciPy statistika: https://docs.scipy.org/doc/scipy/reference/stats.html
