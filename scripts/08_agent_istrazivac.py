#!/usr/bin/env python3
"""
Data Science u kulturi — 2026./2027.
Skripta 08: Agent istraživač kulturne baštine (Google ADK)
===========================================================
Produkcijski primjer agentskog sustava: LLM + FunctionTool u petlji.
Agent pretražuje katalog, generira statistiku i vizualizaciju,
te piše izvješće — automatizirani istraživač.

Koncept: Perak (2025), Komunikacija u doba umjetne inteligencije
— poglavlje o komunikacijskim agentima.

Upute: pip install google-adk google-generativeai; GEMINI_API_KEY.
"""

import os
import pandas as pd


# ------------------------------------------------------------------
# 1. Alati koje agent može koristiti
# ------------------------------------------------------------------
class Katalog:
    """Muzejski katalog (sintetički podaci)."""

    def __init__(self):
        self.df = pd.DataFrame({
            "id": ["M-0001", "M-0002", "M-0003", "M-0004", "M-0005", "M-0006"],
            "naziv": ["Portret ribara", "Mrtva priroda", "Pejzaž Kvarnera",
                      "Apstrakcija", "Luka Rijeka", "Gradska vijećnica"],
            "godina": [1920, 1931, 1915, 1958, 1900, 1894],
            "materijal": ["ulje", "ulje", "akvarel", "ulje", "fotografija", "grafika"],
            "zbirka": ["Moderna", "Moderna", "Grafika", "Suvremena", "Fotografija", "Povijesna"],
        })

    def pretrazi(self, upit: str) -> str:
        """Pretražuje katalog po nazivu/zbirci."""
        df = self.df
        mask = df["naziv"].str.contains(upit, case=False) | df["zbirka"].str.contains(upit, case=False)
        rez = df[mask]
        if rez.empty:
            return "Nema rezultata u katalogu."
        return rez.to_string(index=False)

    def statistika(self, stupac: str = "godina") -> str:
        """Deskriptivna statistika stupca."""
        return self.df[stupac].describe().round(2).to_string()

    def raspodjela(self, stupac: str = "zbirka") -> str:
        """Frekvencije kategoričkog stupca."""
        return self.df[stupac].value_counts().to_string()


# ------------------------------------------------------------------
# 2. ADK agent
# ------------------------------------------------------------------
def adk_agent():
    try:
        from google.adk.agents import LlmAgent, LoopAgent
        from google.adk.tools import FunctionTool
    except ImportError:
        print("⚠️ google-adk nije instaliran. Pokreni: pip install google-adk")
        return None

    kat = Katalog()

    agent = LlmAgent(
        name="istrazivac_bastine",
        model="gemini-2.0-flash",
        tools=[
            FunctionTool(kat.pretrazi),
            FunctionTool(kat.statistika),
            FunctionTool(kat.raspodjela),
        ],
        instruction=(
            "Ti si istraživač kulturne baštine. Kada dobiješ upit:\n"
            "1. Pozovi alate za pretragu kataloga i statistiku\n"
            "2. Interpretiraj rezultate u kontekstu povijesti umjetnosti\n"
            "3. Predloži sljedeće korake istraživanja"
        ),
        description="Automatizirani istraživač muzejske zbirke",
    )

    petlja = LoopAgent(name="petlja", sub_agents=[agent], max_iterations=5)
    print("✅ ADK agent spreman: 'istrazivac_bastine' s 3 alata (pretrazi, statistika, raspodjela)")
    print()
    print("Pokretanje:")
    print("  petlja.run('Kakva je raspodjela djela po zbirkama?')")
    print("  petlja.run('Pronađi djela iz Moderne zbirke i opiši ih.')")
    print()
    if not os.environ.get("GEMINI_API_KEY"):
        print("⚠️ GEMINI_API_KEY nije postavljen — agent se ne izvršava.")
    return petlja


if __name__ == "__main__":
    kat = Katalog()
    print("=== Demonstracija alata (bez LLM-a) ===")
    print(kat.pretrazi("Moderna"))
    print()
    print(kat.statistika())
    print()
    print(kat.raspodjela())
    print()
    print("=== ADK agent ===")
    adk_agent()
