#!/usr/bin/env python3
"""
Data Science u kulturi — 2026./2027.
Skripta 02: Statistička analiza — korelacije i testovi
=======================================================
Primjena deskriptivne statistike, korelacijske analize i
testiranja hipoteza u kulturološkim istraživanjima.

Upute: pip install pandas scipy
"""

import numpy as np
import pandas as pd
from scipy import stats


def generiraj_podatke(n=60, seed=7):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        "id": range(1, n + 1),
        "dob": rng.integers(18, 35, n),
        "kino": rng.integers(0, 25, n),
        "citam": rng.integers(0, 12, n),
        "koncerti": rng.integers(0, 12, n),
        "netflix_sati": rng.integers(0, 30, n),
    })
    # Ugradimo stvarnu korelaciju: više čitanja → manje Netflixa (slaba negativna)
    df["netflix_sati"] = df["netflix_sati"] - df["citam"].astype(float) * 0.5
    df["netflix_sati"] = df["netflix_sati"].clip(lower=0)
    return df


def korelacijska_analiza(df: pd.DataFrame):
    print("=== KORELACIJSKA MATRICA (Pearson) ===")
    matrica = df[["dob", "kino", "citam", "koncerti", "netflix_sati"]].corr()
    print(matrica.round(3))
    print()

    print("=== POJEDINAČNE KORELACIJE S p-VRIJEDNOSTIMA ===")
    parovi = [
        ("kino", "citam"),
        ("citam", "netflix_sati"),
        ("dob", "koncerti"),
        ("kino", "koncerti"),
    ]
    for x, y in parovi:
        r, p = stats.pearsonr(df[x], df[y])
        znak = "✓ značajno" if p < 0.05 else "✗ nije značajno"
        print(f"  {x} ↔ {y}: r = {r:+.3f}, p = {p:.4f} {znak}")

    print()
    print("⚠️ Važno: korelacija ≠ uzročnost!")
    print("   Npr. 'kino' i 'koncerti' mogu korelirati jer oboje odražavaju")
    print("   opću kulturnu aktivnost (treća varijabla), ne zato što jedno uzrokuje drugo.")


def t_test(df: pd.DataFrame):
    print("=== t-TEST: kultura index — muškarci vs žene ===")
    df["kultura"] = df["kino"] + df["koncerti"] * 2
    m = df[df["spol"] == "M"]["kultura"]
    z = df[df["spol"] == "Ž"]["kultura"]
    t, p = stats.ttest_ind(m, z)
    print(f"  M: n={len(m)}, mean={m.mean():.2f}")
    print(f"  Ž: n={len(z)}, mean={z.mean():.2f}")
    print(f"  t = {t:.3f}, p = {p:.4f}")
    print(f"  Zaključak: {'postoji razlika' if p < 0.05 else 'nema statistički značajne razlike'}")


if __name__ == "__main__":
    podaci = generiraj_podatke()
    # Dodaj spol za t-test
    rng = np.random.default_rng(1)
    podaci["spol"] = rng.choice(["M", "Ž"], len(podaci))
    korelacijska_analiza(podaci)
    print()
    t_test(podaci)
