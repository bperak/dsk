# 03. Python i Google Colab — osnove

**Kolegij:** Data Science u kulturi | 2026./2027.

## Zašto Python?

- Standard u data science-u i digitalnoj humanistici
- Čitljiva sintaksa, ogroman ekosustav biblioteka
- pandas, numpy, matplotlib, scikit-learn, nltk, google-generativeai

## Google Colab

Google Colab je besplatno **kolaborativno mrežno sučelje** za izvršavanje
Python koda u pregledniku — idealno za nastavu i istraživanje:

- https://colab.research.google.com
- Nula instalacije (sve radi u pregledniku)
- GPU/TPU dostupni (za veće modele)
- Dijeljenje i suradnja u stvarnom vremenu
- Povezivanje s Google Driveom

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

## Struktura Colab bilježnice

- **Markdown ćelije** — teorija, objašnjenja, tablice
- **Code ćelije** — izvršni Python
- **@title** — naslov za skrivanje koda
- **userdata** — sigurno čuvanje API ključeva

## Postavljanje

```python
!pip install -q pandas numpy matplotlib seaborn google-generativeai
import pandas as pd
import numpy as np
```

## Ishodi učenja (7)

- Svladati osnovne statističko-analitičke funkcije data-science programa.

## Praktično

Colab: `colab/DS_KULT_Podatkovna_znanost_u_kulturi.ipynb` (ćelija "Instalacija i setup")
