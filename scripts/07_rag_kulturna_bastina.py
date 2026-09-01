#!/usr/bin/env python3
"""
Data Science u kulturi — 2026./2027.
Skripta 07: RAG — razgovor s kulturnom baštinom
================================================
Retrieval-Augmented Generation: dohvat relevantnih dokaza
iz korpusa (embedding pretraga) + LLM odgovor temeljen na njima.

Rješava problem halucinacija: model odgovara iz VAŠEG korpusa.
Arhitektura današnjih AI asistenata za muzeje, arhive i knjižnice.

Koncept: Perak (2025), Komunikacija u doba umjetne inteligencije
— poglavlje o RAG arhitekturi.

Upute: pip install google-generativeai numpy scikit-learn; GEMINI_API_KEY.
"""

import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

MODEL_EMB = "models/text-embedding-004"
MODEL_LLM = "gemini-2.0-flash"

KORPUS = [
    "Riječki port je sredinom 19. stoljeća postao jedna od najvažnijih luka Austro-Ugarske.",
    "Kazalište HNK Ivan pl. Zajc sagrađeno je 1885. godine u neorenesansnom stilu.",
    "Tornjačić na Trsatu potječe iz 13. stoljeća, a riječ je o najstarijem sačuvanom dijelu utvrde.",
    "Gradska vijećnica u Rijeci građena je od 1885. do 1894. prema projektu Janosa Wagnera.",
    "Prva riječka rafinerija nafte otvorena je 1882. godine, jedna od prvih u Europi.",
    "Palača Modello izgrađena je 1885. godine u historicističkom stilu.",
    "Guvernerova palača, danas Pomorski i povijesni muzej Hrvatskog primorja, sagrađena je 1896.",
    "Kapucinske stube povezuju Stari grad s novijim dijelom Rijeke od 18. stoljeća.",
]


def dohvati_dokaze(genai, pitanje, korpus, k=3):
    vk = embed(genai, korpus)
    vp = embed(genai, [pitanje])
    sim = cosine_similarity(vp, vk)[0]
    top = sim.argsort()[-k:][::-1]
    return [(i, korpus[i], sim[i]) for i in top]


def rag_pitaj(genai, model, pitanje, korpus=KORPUS, k=3):
    dokazi = dohvati_dokaze(genai, pitanje, korpus, k)
    kontekst = "\n\n".join(f"[{i+1}] {tekst}" for i, tekst, _ in dokazi)

    prompt = f"""
Odgovori na pitanje ISKLJUČIVO na temelju priloženih dokaza.
Ako odgovor nije u dokazima, reci: "Nije navedeno u izvorima."
Citiraj izvor u zagradi: (izvor [N])

Dokazi:
{kontekst}

Pitanje: {pitanje}
"""
    odgovor = model.generate_content(prompt)
    print(f"Pitanje: {pitanje}")
    print(f"Dohvaćeni dokazi ({k}):")
    for i, tekst, s in dokazi:
        print(f"  [{i+1}] (sim={s:.3f}) {tekst[:70]}...")
    print(f"\nOdgovor: {odgovor.text}")
    print("-" * 60)


def embed(genai, tekstovi):
    r = genai.embed_content(model=MODEL_EMB, content=tekstovi)
    return np.array(r["embedding"])


if __name__ == "__main__":
    import google.generativeai as genai
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel(MODEL_LLM)

    print("=== RAG: razgovor s korpusom riječke baštine ===\n")
    rag_pitaj(genai, model, "Kada je sagrađeno riječko kazalište?")
    rag_pitaj(genai, model, "Tko je projektirao Gradsku vijećnicu?")
    rag_pitaj(genai, model, "Što se danas nalazi u Guvernerovoj palači?")
    rag_pitaj(genai, model, "Koji je najstariji dio riječke utvrde?")
