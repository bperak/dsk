# 05. Statistika — deskriptivna analiza i korelacije

**Kolegij:** Data Science u kulturi | 2026./2027.

## Deskriptivna statistika

Opisuje podatke brojkama:

| Mjera | Značenje |
|-------|----------|
| Srednja vrijednost (mean) | Prosjek |
| Medijan | Srednja vrijednost sortiranih podataka |
| Mod | Najčešća vrijednost |
| Standardna devijacija | Raspršenost oko prosjeka |
| Min/Max | Raspon |

## Korelacija

**Korelacija** mjeri povezanost dviju varijabli (od -1 do +1):

- +1: savršena pozitivna povezanost
- 0: nema povezanosti
- -1: savršena negativna povezanost

```python
import scipy.stats as stats
r, p = stats.pearsonr(df["kino"], df["citam"])
```

**⚠️ Važno: korelacija ≠ uzročnost!**

Npr. "kino" i "koncerti" mogu korelirati jer oboje odražavaju opću kulturnu
aktivnost (treća varijabla), ne zato što jedno uzrokuje drugo.

## Statistička značajnost (p-vrijednost)

- p < 0.05 = statistički značajno (5% rizik pogreške)
- p ≥ 0.05 = nije značajno
- Značajnost ovisi o veličini uzorka

## AI u statistici

LLM može pomoći: generirati analitički kod iz pitanja, interpretirati rezultate,
predložiti testove. **Ali konačna interpretacija je na istraživaču.**

## Ishodi učenja (5)

- Analizirati kvantitativne i kvalitativne tipove podataka te primijeniti
  postupke statističke analize.

## Praktično

Skripta: `scripts/02_statistika_korelacije.py`
