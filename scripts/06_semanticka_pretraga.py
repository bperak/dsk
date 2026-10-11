#!/usr/bin/env python3
"""
Data Science u kulturi — 2026./2027.
Skripta 06: Semantička pretraga kulturnih zbirki (embedding)
==============================================================
Umjesto pretrage po ključnim riječima, embedding reprezentacije
omogućuju pronalazak po ZNAČENJU: upit "morski pejzaži" nalazi i
zapise koji ne sadrže te riječi.

Koncept: Perak (2025), Komunikacija u doba umjetne inteligencije
— poglavlje o embedding reprezentacijama i semantičkoj pretrazi.

Upute: pip install google-genai numpy scikit-learn; export GEMINI_API_KEY.
Ključ izradi prije nastave (https://aistudio.google.com). Kvota je po projektu.
"""

import os
import time

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Pri promjeni provjeri https://ai.google.dev/gemini-api/docs/deprecations
EMB_MODEL = "gemini-embedding-2"

PORUKA_KLJUC = (
    "Ključ nije postavljen. Izradi ga na https://aistudio.google.com "
    "→ Get API key i zalijepi ga ovdje."
)
PORUKA_KVOTA = "Prekoračena kvota za minutu — pričekaj pa ponovi"


def _je_kvota(greska):
    kod = getattr(greska, "code", None)
    if kod is None:
        kod = getattr(greska, "status_code", None)
    return kod == 429 or "429" in str(greska)


def pozovi_model(poziv):
    """Poziv modela. Na 429 ispiše uputu, čeka 5 s i pokušava ponovno (najviše 2 puta)."""
    for pokusaj in range(3):
        try:
            return poziv()
        except Exception as greska:
            if not _je_kvota(greska) or pokusaj == 2:
                raise
            print(PORUKA_KVOTA)
            time.sleep(5)


def embed(client, tekstovi):
    """Vektori iz response.embeddings[i].values."""
    odgovor = pozovi_model(
        lambda: client.models.embed_content(model=EMB_MODEL, contents=list(tekstovi))
    )
    return np.array([stavka.values for stavka in odgovor.embeddings])


def semanticka_pretraga(client, upit, opisi, vektori, k=3):
    qv = embed(client, [upit])
    sim = cosine_similarity(qv, vektori)[0]
    top = sim.argsort()[-k:][::-1]
    print(f"Upit: '{upit}'")
    for i in top:
        print(f"  [{sim[i]:.3f}] {opisi[i]}")
    print()


def klijent():
    if not os.environ.get("GEMINI_API_KEY", "").strip():
        print(PORUKA_KLJUC)
        raise SystemExit(PORUKA_KLJUC)
    from google import genai
    return genai.Client(api_key=os.environ["GEMINI_API_KEY"])


if __name__ == "__main__":
    client = klijent()

    opisi = [
        "Portret starog ribara s mrežama na obali",
        "Mrtva priroda s cvijećem i voćem na stolu",
        "Pejzaž s jedrenjakom na pučini Kvarnera",
        "Apstraktna kompozicija u crvenoj i plavoj",
        "Stara fotografija riječke luke s parobrodom",
        "Skica djevojke s kišobranom u parku",
        "Grafika s motivom gradske vijećnice",
        "Akvarel kazališne zgrade u sumrak",
        "Crtež tornja s pogledom na grad",
        "Ulje na platnu s prikazom industrijske luke",
    ]

    vektori = embed(client, opisi)

    print("=== Semantička pretraga zbirke ===")
    semanticka_pretraga(client, "morski pejzaži i brodovi", opisi, vektori)
    semanticka_pretraga(client, "arhitektura i gradske znamenitosti", opisi, vektori)
    semanticka_pretraga(client, "priroda i cvjetni motivi", opisi, vektori)

    print("→ Ključna razlika: pretraga razumije TEMU, ne samo riječi.")
    print("→ Temelj moderne preporuke i pretrage u digitalnoj humanistici.")
