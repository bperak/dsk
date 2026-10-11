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

Upute: pip install google-genai numpy scikit-learn; export GEMINI_API_KEY.
Ključ izradi prije nastave (https://aistudio.google.com). Kvota je po projektu.
"""

import os
import time

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Pri promjeni provjeri https://ai.google.dev/gemini-api/docs/deprecations
MODEL = "gemini-3.5-flash"
EMB_MODEL = "gemini-embedding-2"

PORUKA_KLJUC = (
    "Ključ nije postavljen. Izradi ga na https://aistudio.google.com "
    "→ Get API key i zalijepi ga ovdje."
)
PORUKA_KVOTA = "Prekoračena kvota za minutu — pričekaj pa ponovi"

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


def dohvati_dokaze(client, pitanje, korpus, k=3):
    vk = embed(client, korpus)
    vp = embed(client, [pitanje])
    sim = cosine_similarity(vp, vk)[0]
    top = sim.argsort()[-k:][::-1]
    return [(i, korpus[i], sim[i]) for i in top]


def rag_pitaj(client, pitanje, korpus=KORPUS, k=3):
    dokazi = dohvati_dokaze(client, pitanje, korpus, k)
    kontekst = "\n\n".join(f"[{i+1}] {tekst}" for i, tekst, _ in dokazi)

    prompt = f"""
Odgovori na pitanje ISKLJUČIVO na temelju priloženih dokaza.
Ako odgovor nije u dokazima, reci: "Nije navedeno u izvorima."
Citiraj izvor u zagradi: (izvor [N])

Dokazi:
{kontekst}

Pitanje: {pitanje}
"""
    odgovor = pozovi_model(
        lambda: client.models.generate_content(model=MODEL, contents=prompt)
    )
    print(f"Pitanje: {pitanje}")
    print(f"Dohvaćeni dokazi ({k}):")
    for i, tekst, s in dokazi:
        print(f"  [{i+1}] (sim={s:.3f}) {tekst[:70]}...")
    print(f"\nOdgovor: {odgovor.text}")
    print("-" * 60)


def klijent():
    if not os.environ.get("GEMINI_API_KEY", "").strip():
        print(PORUKA_KLJUC)
        raise SystemExit(PORUKA_KLJUC)
    from google import genai
    return genai.Client(api_key=os.environ["GEMINI_API_KEY"])


if __name__ == "__main__":
    client = klijent()

    print("=== RAG: razgovor s korpusom riječke baštine ===\n")
    rag_pitaj(client, "Kada je sagrađeno riječko kazalište?")
    rag_pitaj(client, "Tko je projektirao Gradsku vijećnicu?")
    rag_pitaj(client, "Što se danas nalazi u Guvernerovoj palači?")
    rag_pitaj(client, "Koji je najstariji dio riječke utvrde?")
