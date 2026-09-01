# Poglavlje 5: Statistika za kulturologa

---

## Sažetak poglavlja

Statistika je jezik kojim podaci govore — a kulturolog treba razumjeti taj
jezik da bi kritički čitao istraživanja i samostalno provodio analize.
Ovo poglavlje uvodi deskriptivnu statistiku, raspodjele, mjere povezanosti
(korelacije) i statističku značajnost, s posebnim naglaskom na dvije
stvari: (1) **korelacija nije uzročnost** i (2) **kako LLM može pomoći**
u statistici — i gdje su njegove granice.

---

## 5.1 Deskriptivna statistika

Deskriptivna statistika **sažima** podatke u nekoliko brojeva.

### Mjere sredine

| Mjera | Što pokazuje | Kada koristiti |
|-------|--------------|----------------|
| **Aritmetička sredina** (mean) | Prosjek | Simetrične raspodjele |
| **Medijan** | Srednja vrijednost sortiranih podataka | Iskrivljene raspodjele (otporniji) |
| **Mod** | Najčešća vrijednost | Kategorički podaci |

### Mjere raspršenosti

| Mjera | Što pokazuje |
|-------|--------------|
| **Raspon** (min-max) | Koliko je širok podatak |
| **Standardna devijacija** (SD) | Prosječno odstupanje od sredine |
| **Varijanca** | SD na kvadrat |
| **Kvartili / percentili** | Položaj vrijednosti (25 %, 50 %, 75 %) |

```python
import pandas as pd

anketa = pd.DataFrame({
    "kino_godisnje": [12, 3, 8, 20, 5, 15, 2, 9, 30, 6],
})

print(anketa["kino_godisnje"].mean())    # 11.0
print(anketa["kino_godisnje"].median())  # 8.5
print(anketa["kino_godisnje"].std())     # 8.65
print(anketa["kino_godisnje"].describe())
```

> **Zašto medijan često "bolji" od prosjeka?** Ako jedan ispitanik ode u
> kino 30 puta godišnje (ekstrem), prosjek raste na 11, a medijan ostaje
> 8.5 — medijan bolje opisuje "tipičnog" ispitanika. U kulturnim podacima
> ekstremi su česti (zvijezde, viralni sadržaji) — uvijek gledajte i medijan.

---

## 5.2 Raspodjele

**Raspodjela** pokazuje kako se vrijednosti raspoređuju.

### Normalna raspodjela

Zvonolika, simetrična — mean = medijan = mod. Mnoge prirodne pojave slijede
je, ali **kulturni podaci često ne**:

- broj posjetitelja (desno iskrivljena — par velikih, puno malih)
- frekvencije riječi (Zipfov zakon — ogroman pad)
- lajkovi na mrežama (jako iskrivljeno)

```python
# Iskrivljenost (skewness): >0 desno, <0 lijevo
print(anketa["kino_godisnje"].skew())   # pozitivno — iskrivljeno udesno
```

### Zipfov zakon u kulturi

Frekvencija riječi u tekstu obrnuto je proporcionalna rangu: najčešća
riječ ~2× češća od druge, ~3× od treće... Ovaj zakon vrijedi za jezike,
a slični obrasci (power law) javljaju se u popularnosti, citiranju i
prometu kulturnih sadržaja.

```python
from collections import Counter
import re

tekst = "kultura kultura jezik kultura jezik umjetnost jezik kultura"
frek = Counter(re.findall(r"\w+", tekst.lower()))
print(frek.most_common(3))
```

---

## 5.3 Korelacije: mjere povezanosti

**Korelacija** mjeri **povezanost** dviju varijabli: kreće se od -1 do +1.

| Vrijednost | Značenje |
|------------|----------|
| +1 | Savršena pozitivna (obje rastu zajedno) |
| +0,5 | Umjerena pozitivna |
| 0 | Nema linearne povezanosti |
| -0,5 | Umjerena negativna (jedna raste, druga pada) |
| -1 | Savršena negativna |

### Pearson i Spearman

- **Pearson** — linearna povezanost (za približno normalne podatke)
- **Spearman** — monotona povezanost (za redove/iskrivljene; otporniji)

```python
import scipy.stats as stats

# Pearson
r, p = stats.pearsonr(anketa["kino_godisnje"], anketa["citam_sati"])
print(f"Pearson: r={r:.2f}, p={p:.3f}")

# Spearman
rs, ps = stats.spearmanr(anketa["kino_godisnje"], anketa["citam_sati"])
print(f"Spearman: r={rs:.2f}, p={ps:.3f}")

# Matrica korelacija (cijela tablica)
import seaborn as sns
sns.heatmap(anketa.corr(), annot=True)
```

### ⚠️ Korelacija ≠ uzročnost

Najvažnija lekcija statistike za kulturologa:

1. **Treća varijabla:** "kino" i "koncerti" koreliraju jer oboje mjere
   opću kulturnu aktivnost — ne zato što jedno uzrokuje drugo.
2. **Obrnuti smjer:** "TikTok korištenje korelira s lošim raspoloženjem" —
   možda TikTok uzrokuje loše raspoloženje, ali možda loše raspoloženi
   ljudi više koriste TikTok.
3. **Slučajnost:** s puno varijabli, neke korelacije su slučajne
   (problem višestrukog testiranja).

> **Teorijski okvir — od korelacije do objašnjenja.**
> U humanistici korelacija nikad nije dovoljna: potrebna je **teorija**
> koja objašnjava *zašto* su pojave povezane. Kulturne prakse nisu
> "prirodni fenomeni" — one su proizvod značenja, moći i povijesti.
> Statistika otkriva obrasce; teorija ih interpretira.

---

## 5.4 Statistička značajnost

**p-vrijednost** odgovara na pitanje: "ako u populaciji NEMA povezanosti,
kolika je vjerojatnost da bismo u uzorku vidjeli ovakvu (ili ekstremniju)
korelaciju?"

- **p < 0,05** → rezultat se smatra statistički značajnim (manje od 5 %
  rizika da je slučajan)
- **p ≥ 0,05** → nije značajno (ne možemo isključiti slučajnost)

### Tri česte zablude

1. **p < 0,05 ne znači "dokazano"** — znači "statistički neočekivano pod
   nul-hipotezom". Interpretacija ostaje na istraživaču.
2. **Značajnost ≠ važnost.** S velikim uzorkom (N=10 000), i beznačajna
   korelacija r=0,02 postaje "značajna".
3. **Neznačajan rezultat ≠ nema efekta.** Možda je uzorak premali
   (snaga testa).

### Veličina efekta

Uvijek izvještavajte i veličinu efekta, ne samo p:

- **r** (korelacija) sam po sebi je veličina efekta: 0,1 mali, 0,3 srednji, 0,5 veliki
- **Cohenov d** za usporedbu grupa: 0,2 mali, 0,5 srednji, 0,8 veliki

---

## 5.5 LLM u statistici: pomoć i granice

### Gdje LLM stvarno pomaže

1. **Generiranje koda:** "napiši Python koji računa Spearmanovu korelaciju
   između kino i koncerata, po spolu"
2. **Interpretacija rezultata:** "što znači r=0,45, p=0,03 za moje istraživanje
   o glazbenim navikama?" — model daje prvi nacrt interpretacije
3. **Odabir testa:** "koji test za usporedbu dvije grupe s malim uzorkom?"
4. **Provjera dizajna:** "koje su zamke moje ankete?"

### Gdje LLM ne valja (⚠️ provjeri uvijek)

1. **Računanje!** Modeli su loši u aritmetici — uvijek pokrenite kod,
   ne vjerujte broju iz teksta.
2. **Halucinirani brojevi:** model može "izmisliti" r=0,87 ili p=0,001.
3. **Cirkularnost:** model "tumači" rezultate koje mu je netko dao, bez
   uvida u stvarne podatke — interpretacija može biti proizvoljna.

### Praktikum: LLM + provjera

```python
# 1. LLM generira kod
prompt = "Napiši Python (pandas+scipy) koji testira korelaciju kino~citam. Samo kod."
kod = model.generate_content(prompt).text

# 2. POKRENI kod — izračun je stvaran
exec(kod)

# 3. LLM interpretira, TI provjeravaš
interp = model.generate_content(
    f"Rezultat: r={r:.2f}, p={p:.3f}, N={len(anketa)}. Protumači za kulturologa."
).text
```

> **Pravilo:** LLM = asistent za prvi nacrt (koda i interpretacije);
> izračun = stroj; konačno tumačenje = istraživač.

---

## Vježbe

### 🟢 Osnovna
1. Za svoju anketu izračunajte: mean, median, SD, min, max za 3 numeričke
   varijable. Koja je raspodjela iskrivljena i zašto?
2. `value_counts()` za kategorijsku varijablu + postoci.

### 🟡 Srednja
3. Testirajte korelaciju dviju varijabli (Pearson + Spearman) i napišite
   tumačenje: smjer, snaga, značajnost. Što bi treća varijabla mogla objasniti?
4. Napravite scatter plot + heatmap korelacija.

### 🏆 Napredna
5. Pomoću LLM-a generirajte cijelu analizu (kod + interpretacija) za svoje
   podatke, zatim **ručno provjerite svaki broj**. Dokumentirajte 3 greške
   koje je model napravio (ili potvrdite da ih nije bilo).
6. Pronađite u medijima jedan "korelacija kao uzročnost" naslov (npr.
   "X povećava Y") i objasnite zašto je zaključak problematičan.

---

## Sažetak i ključni pojmovi

- Deskriptivna statistika: sredina (mean/median/mod) + raspršenost (SD, kvartili).
- Kulturni podaci često su iskrivljeni (Zipf, power law) — medijan je otporniji.
- Korelacija: -1 do +1; Pearson (linearna), Spearman (monotona).
- ⚠️ Korelacija ≠ uzročnost — treća varijabla, smjer, slučajnost.
- p-vrijednost: značajnost ≠ važnost; uvijek i veličina efekta.
- LLM pomaže u kodu i interpretaciji, ali brojeve uvijek provjeravajte.

**Ključni pojmovi:** mean, medijan, mod, standardna devijacija, kvartil,
raspodjela, skewness, Zipfov zakon, korelacija, Pearson, Spearman,
p-vrijednost, veličina efekta.

---

## Literatura

- Field, A. (2018). *Discovering Statistics Using IBM SPSS Statistics* (5. izd.). SAGE.
- Grus, J. (2019). *Data Science from Scratch* (2. izd.). O'Reilly. (pogl. 6)
- Downey, A. (2014). *Think Stats* (2. izd.). O'Reilly. (open access)
- Cumming, G. (2012). *Understanding the New Statistics*. Routledge.
