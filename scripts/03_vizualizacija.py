#!/usr/bin/env python3
"""
Data Science u kulturi — 2026./2027.
Skripta 03: Vizualizacija podataka (Matplotlib, Seaborn)
=========================================================
Pravila dobre vizualizacije u znanstvenim izvješćima:
jasne oznake, čitljiv font, poštena skala, kontekst.

Upute: pip install matplotlib seaborn pandas numpy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def generiraj(n=50, seed=3):
    rng = np.random.default_rng(seed)
    return pd.DataFrame({
        "kino": rng.integers(0, 25, n),
        "citam": rng.integers(0, 12, n),
        "koncerti": rng.integers(0, 12, n),
        "kultura_index": rng.integers(0, 50, n),
    })


def vizualizacije(df: pd.DataFrame):
    sns.set_theme(style="darkgrid")
    fig, osi = plt.subplots(2, 2, figsize=(12, 9))
    fig.suptitle("Kulturne navike — vizualizacije", fontsize=14)

    # 1. Histogram
    osi[0, 0].hist(df["kino"], bins=8, color="#4fc3f7", edgecolor="white")
    osi[0, 0].set_title("Kino posjeti godišnje")
    osi[0, 0].set_xlabel("broj posjeta")
    osi[0, 0].set_ylabel("frekvencija")

    # 2. Scatter + regresija
    sns.regplot(x="citam", y="kino", data=df, ax=osi[0, 1],
                scatter_kws={"alpha": 0.6}, line_kws={"color": "red"})
    osi[0, 1].set_title("Čitanje vs kino (s regresijskom linijom)")

    # 3. Box plot
    df2 = df.copy()
    df2["kategorija"] = np.where(df2["kultura_index"] > 25, "visoka", "niska")
    sns.boxplot(x="kategorija", y="kino", data=df2, ax=osi[1, 0])
    osi[1, 0].set_title("Kino po kategoriji kulture")

    # 4. Bar chart srednjih vrijednosti
    srednje = df[["kino", "citam", "koncerti"]].mean()
    osi[1, 1].bar(srednje.index, srednje.values, color=["#81c784", "#ffb74d", "#ba68c8"])
    osi[1, 1].set_title("Prosječne vrijednosti aktivnosti")
    osi[1, 1].set_ylabel("prosjek")

    plt.tight_layout()
    plt.savefig("vizualizacije_kultura.png", dpi=150)
    plt.show()
    print("✅ Spremljeno: vizualizacije_kultura.png")


if __name__ == "__main__":
    podaci = generiraj()
    vizualizacije(podaci)
