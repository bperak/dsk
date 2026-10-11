#!/usr/bin/env python3
"""
Data Science u kulturi — 2026./2027.
Skripta 05: LLM analiza u podatkovnoj znanosti
===============================================
Primjena velikih jezičnih modela za označavanje, klasifikaciju,
sažimanje i interpretaciju kulturoloških podataka — uz kritički
pristup (halucinacije, pristranost, provjera).

Teorijska pozadina:
- Perak (2025), Komunikacija u doba umjetne inteligencije
  — LLM-ovi kao komunikacijski agenti, kritičko vrednovanje
- Bommasani et al. (2021), On the Opportunities and Risks of Foundation Models

Upute: pip install google-genai; export GEMINI_API_KEY.
Ključ izradi prije nastave (https://aistudio.google.com). Kvota je po projektu.
"""

import json
import os
import time

# Pri promjeni provjeri https://ai.google.dev/gemini-api/docs/deprecations
MODEL = "gemini-3.5-flash"

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


def generiraj(client, prompt):
    odgovor = pozovi_model(
        lambda: client.models.generate_content(model=MODEL, contents=prompt)
    )
    return odgovor.text


def llm_klasifikacija(client, tekstovi, kategorije):
    """Klasificira tekstove u zadane kategorije, vraća JSON."""
    prompt = f"""
Klasificiraj svaki tekst u jednu od kategorija: {kategorije}.
Vrati VALIDAN JSON (bez markdowna):
{{"rezultati": [{{"id": 1, "kategorija": "...", "vjerojatnost": 0.9}}]}}

Tekstovi:
{json.dumps(tekstovi, ensure_ascii=False)}
"""
    tekst = generiraj(client, prompt)
    try:
        cist = tekst.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        return json.loads(cist)
    except json.JSONDecodeError:
        return {"rezultati": [], "raw": tekst[:300]}


def llm_sazetak(client, tekst):
    """Sažima tekst uz upozorenje o provjeri."""
    prompt = f"""
Sažmi sljedeći tekst na 3 rečenice, zadržavajući ključne podatke.
Dodaj na kraju: "Provjeri izvorne podatke prije upotrebe."

Tekst: {tekst}
"""
    return generiraj(client, prompt)


def llm_ekstrakcija(client, tekst):
    """Strukturirana ekstrakcija podataka iz teksta."""
    prompt = f"""
Iz teksta izdvoji strukturirane podatke. Vrati VALIDAN JSON:
{{"entiteti": [{{"naziv": "...", "tip": "osoba|mjesto|organizacija|djelo", "godina": null}}]}}

Tekst: {tekst}
"""
    odgovor = generiraj(client, prompt)
    try:
        cist = odgovor.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        return json.loads(cist)
    except json.JSONDecodeError:
        return {"entiteti": [], "raw": odgovor[:300]}


def klijent():
    if not os.environ.get("GEMINI_API_KEY", "").strip():
        print(PORUKA_KLJUC)
        raise SystemExit(PORUKA_KLJUC)
    from google import genai
    return genai.Client(api_key=os.environ["GEMINI_API_KEY"])


if __name__ == "__main__":
    client = klijent()

    tekstovi = [
        "Izložba 'Digitalni krajobrazi' otvorena je u Muzeju moderne umjetnosti.",
        "Novi katalog donosi 200 reprodukcija s popratnim tekstovima kustosa.",
        "Radionica o umjetnoj inteligenciji u kulturi okupila je 40 sudionika.",
    ]
    print("=== 1. LLM klasifikacija ===")
    rezultat = llm_klasifikacija(client, tekstovi, "vijest, najava, izvjestaj")
    print(json.dumps(rezultat, ensure_ascii=False, indent=2))

    print("\n=== 2. LLM ekstrakcija entiteta ===")
    tekst_entiteti = (
        "HNK Ivan pl. Zajc u Rijeci, sagrađen 1885., jedno je od najstarijih kazališta. "
        "Guvernerova palača iz 1896. danas je Pomorski i povijesni muzej."
    )
    print(json.dumps(llm_ekstrakcija(client, tekst_entiteti), ensure_ascii=False, indent=2))

    print("\n=== 3. LLM sažetak ===")
    tekst = """
    Digitalna humanistika razvija se kao interdisciplinarno polje koje povezuje
    računalne metode s tradicionalnim humanističkim istraživanjima. U zadnjih
    deset godina veliki jezični modeli omogućili su automatsku analizu golemih
    korpusa tekstova, što je otvorilo nove mogućnosti, ali i etičke izazove
    vezane uz pristranost, privatnost i interpretaciju.
    """
    print(llm_sazetak(client, tekst))
