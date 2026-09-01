#!/usr/bin/env python3
"""
Data Science u kulturi — 2026./2027.
Skripta 01: Pandas — tablični podaci i deskriptivna statistika
===============================================================
Osnove rada s podacima u kulturološkim istraživanjima:
ankete, metapodaci, katalozi → DataFrame → analiza.

Upute: pip install pandas numpy
"""

import pandas as pd
import numpy as np


def kreiraj_anketu(n=50, seed=42):
    """Generira sintetičku anketu o kulturnim navikama."""
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        "id": range(1, n + 1),
        "dob": rng.integers(18, 30, n),
        "spol": rng.choice(["M", "Ž", "N"], n),
        "kino_godisnje": rng.integers(0, 30, n),
        "citam_tjedno_sati": rng.integers(0, 15, n),
        "glazbeni_koncerti": rng.integers(0, 15, n),
        "posjecuje_muzej": rng.choice([True, False], n, p=[0.4, 0.6]),
    })
    df["kultura_index"] = df["kino_godisnje"] + df["glazbeni_koncerti"] * 2
    return df


def analiza(df: pd.DataFrame):
    print("=== PRVIH 10 REDAKA ===")
    print(df.head(10))
    print()

    print("=== OPĆE INFORMACIJE ===")
    print(f"Broj redaka: {len(df)}, stupaca: {len(df.columns)}")
    print(df.dtypes)
    print()

    print("=== DESKRIPTIVNA STATISTIKA (numeričke) ===")
    print(df.describe().round(2))
    print()

    print("=== FREKVENCIJE (kategoričke) ===")
    print(df["spol"].value_counts())
    print(df["posjecuje_muzej"].value_counts())
    print()

    print("=== GRUPIRANJE: kultura index po spolu ===")
    print(df.groupby("spol")["kultura_index"].agg(["mean", "median", "count"]).round(2))


if __name__ == "__main__":
    podaci = kreiraj_anketu()
    analiza(podaci)
