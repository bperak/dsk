# 04. Pandas — tablični podaci

**Kolegij:** Data Science u kulturi | 2026./2027.

## DataFrame

**DataFrame** je osnovna struktura Pandasa: retci = opažanja, stupci = varijable.
Analogno tablici u Excelu, ali programabilno.

```python
import pandas as pd

df = pd.DataFrame({
    "id": [1, 2, 3],
    "dob": [19, 21, 20],
    "kino": [12, 3, 8],
})
```

## Osnovne operacije

```python
df.head()          # prvih 5 redaka
df.info()          # tipovi podataka
df.describe()      # deskriptivna statistika
df["kino"].mean()  # prosjek stupca
df.groupby("spol")["kultura"].mean()  # grupiranje
df.isnull().sum()  # provjera null vrijednosti
df.drop_duplicates()  # uklanjanje duplikata
```

## Učitavanje podataka

```python
df_csv = pd.read_csv("anketa.csv")
df_excel = pd.read_excel("katalog.xlsx")
df_json = pd.read_json("podaci.json")
```

## Čišćenje podataka

1. Ukloni duplikate
2. Obradi null vrijednosti (ispusti ili popuni)
3. Normaliziraj formate (datumi, tekst)
4. Provjeri konzistentnost kategorija
5. Dokumentiraj promjene

## FAIR priprema za AI

- Strukturirani format (CSV/JSON)
- Konzistentne vrijednosti
- Data dictionary
- Eksport u JSON za LLM/agente

## Ishodi učenja (4, 7)

- Primijeniti data-science tehnike pripreme i pohrane podataka.
- Svladati osnovne funkcije data-science programa.

## Praktično

Skripta: `scripts/01_pandas_osnove.py`
