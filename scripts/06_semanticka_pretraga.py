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

Upute: pip install google-generativeai numpy scikit-learn; GEMINI_API_KEY.
"""

import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

MODEL_EMB = "models/text-embedding-004"


def embed(genai, tekstovi):
    r = genai.embed_content(model=MODEL_EMB, content=tekstovi)
    return np.array(r["embedding"])


def semanticka_pretraga(upit, opisi, vektori, k=3):
    qv = embed(genai, [upit])
    sim = cosine_similarity(qv, vektori)[0]
    top = sim.argsort()[-k:][::-1]
    print(f"Upit: '{upit}'")
    for i in top:
        print(f"  [{sim[i]:.3f}] {opisi[i]}")
    print()


if __name__ == "__main__":
    import google.generativeai as genai
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

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

    vektori = embed(genai, opisi)

    print("=== Semantička pretraga zbirke ===")
    semanticka_pretraga("morski pejzaži i brodovi", opisi, vektori)
    semanticka_pretraga("arhitektura i gradske znamenitosti", opisi, vektori)
    semanticka_pretraga("priroda i cvjetni motivi", opisi, vektori)

    print("→ Ključna razlika: pretraga razumije TEMU, ne samo riječi.")
    print("→ Temelj moderne preporuke i pretrage u digitalnoj humanistici.")
