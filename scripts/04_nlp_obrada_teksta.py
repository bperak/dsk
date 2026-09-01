#!/usr/bin/env python3
"""
Data Science u kulturi — 2026./2027.
Skripta 04: NLP obrada teksta — frekvencije, stop-riječi, bigrami
=================================================================
Osnove tekstualne analize u digitalnoj humanistici:
tokenizacija, čišćenje, frekvencijska analiza, kolokacije.

Upute: pip install nltk
"""

import re
from collections import Counter

import nltk
from nltk.corpus import stopwords

# Hrvatski stop-riječi (NLTK)
try:
    nltk.download("stopwords", quiet=True)
    STOP = set(stopwords.words("croatian"))
except Exception:
    STOP = {"i", "a", "se", "na", "u", "je", "za", "od", "iz", "da", "su",
            "s", "o", "do", "po", "što", "koji", "kao", "ali", "ili", "te"}


def tokeniziraj(tekst: str) -> list[str]:
    """Čišćenje i tokenizacija — samo alfabetske riječi, lowercase."""
    return re.findall(r"[a-zžćčšđ]+", tekst.lower())


def bez_stop(rijeci: list[str]) -> list[str]:
    return [r for r in rijeci if r not in STOP and len(r) > 1]


def bigrami(rijeci: list[str]) -> list[tuple[str, str]]:
    return list(zip(rijeci, rijeci[1:]))


def analiza(tekst: str, naslov: str):
    print(f"=== {naslov} ===")
    rijeci = tokeniziraj(tekst)
    print(f"Ukupno tokena: {len(rijeci)}")

    ciste = bez_stop(rijeci)
    print(f"Nakon stop-riječi: {len(ciste)}")

    print("\nTop 15 riječi:")
    for rijec, n in Counter(ciste).most_common(15):
        print(f"  {rijec}: {n}")

    print("\nTop 10 bigrama (kolokacija):")
    for bg, n in Counter(bigrami(ciste)).most_common(10):
        print(f"  {' '.join(bg)}: {n}")
    print()


if __name__ == "__main__":
    tekst_kultura = """
    Kultura se prenosi kroz jezik, a jezik oblikuje kulturu.
    Umjetna inteligencija mijenja način na koji komuniciramo i stvaramo.
    Digitalna humanistika povezuje tradicionalne metode s novim alatima.
    Veliki jezični modeli analiziraju korpuse tekstova i otkrivaju obrasce.
    Metafore oblikuju naše razumijevanje svijeta i kulture.
    Kulturalni studiji istražuju odnos moći, identiteta i reprezentacije.
    """
    analiza(tekst_kultura, "Kultura i jezik")

    tekst_umjetnost = """
    Umjetnost odražava društvo i njegove vrijednosti.
    Suvremena umjetnost često propituje granice medija.
    Muzeji čuvaju kulturnu baštinu i omogućuju uvid u prošlost.
    Digitalne zbirke čine baštinu dostupnom široj javnosti.
    Publika danas sudjeluje u stvaranju umjetničkih sadržaja.
    """
    analiza(tekst_umjetnost, "Umjetnost i baština")
