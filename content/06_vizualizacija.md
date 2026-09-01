# 06. Vizualizacija podataka

**Kolegij:** Data Science u kulturi | 2026./2027.

## Zašto vizualizacija?

"Grafikon vrijedi 1000 riječi" — dobra vizualizacija:

- otkriva obrasce koje tablice skrivaju
- komunicira rezultate publici
- je dio znanstvenog izvješća

## Pravila dobre vizualizacije

1. **Jasne oznake** — naslov, osi, legenda
2. **Čitljiv font** — dovoljno velik
3. **Poštena skala** — ne zavaravaj osima
4. **Kontekst** — jedinice, izvori, broj opažanja
5. **Pravi tip grafa** — histogram za raspodjelu, scatter za odnos,
   bar za usporedbu, box za raspršenost

## Vrste grafova

| Graf | Kada |
|------|------|
| Histogram | Raspodjela jedne varijable |
| Scatter | Odnos dviju numeričkih varijabli |
| Bar chart | Usporedba kategorija |
| Box plot | Raspršenost po grupama |
| Line chart | Trendovi kroz vrijeme |

## Matplotlib + Seaborn

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.histplot(df["kino"], bins=8, color="#4fc3f7")
plt.title("Kino posjeti godišnje")
plt.xlabel("broj posjeta")
plt.show()
```

## LLM u vizualizaciji

- LLM generira kod za graf iz opisa
- LLM interpretira graf (što vidimo?)
- LLM predlaže bolji tip grafa
- Uvijek provjeri: je li graf pošten?

## Ishodi učenja (6)

- Kritički vrednovati rezultate, metode i tehnike analize podataka.

## Praktično

Skripta: `scripts/03_vizualizacija.py`
