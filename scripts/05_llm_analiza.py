#!/usr/bin/env python3
"""
Data Science u kulturi — 2026./2027.
Skripta 05: LLM analiza u podatkovnoj znanosti
===============================================
Primjena velikih jezičnih modela za označavanje, klasifikaciju,
sažimanje i interpretaciju kulturoloških podataka — uz kritički
pristup (halucinacije, pristranost, provjera).

Upute: pip install google-generativeai; GEMINI_API_KEY.
"""

import json
import os


def llm_klasifikacija(model, tekstovi, kategorije):
    """Klasificira tekstove u zadane kategorije, vraća JSON."""
    prompt = f"""
Klasificiraj svaki tekst u jednu od kategorija: {kategorije}.
Vrati VALIDAN JSON (bez markdowna):
{{"rezultati": [{{"id": 1, "kategorija": "...", "vjerojatnost": 0.9}}]}}

Tekstovi:
{json.dumps(tekstovi, ensure_ascii=False)}
"""
    r = model.generate_content(prompt)
    try:
        cist = r.text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        return json.loads(cist)
    except json.JSONDecodeError:
        return {"rezultati": [], "raw": r.text[:300]}


def llm_sazetak(model, tekst):
    prompt = f"""
Sažmi sljedeći tekst na 3 rečenice, zadržavajući ključne podatke.
Dodaj na kraju: "Provjeri izvorne podatke prije upotrebe."

Tekst: {tekst}
"""
    return model.generate_content(prompt).text


if __name__ == "__main__":
    import google.generativeai as genai
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-2.0-flash")

    tekstovi = [
        "Izložba 'Digitalni krajobrazi' otvorena je u Muzeju moderne umjetnosti.",
        "Novi katalog donosi 200 reprodukcija s popratnim tekstovima kustosa.",
        "Radionica o umjetnoj inteligenciji u kulturi okupila je 40 sudionika.",
    ]
    print("=== 1. LLM klasifikacija ===")
    rezultat = llm_klasifikacija(model, tekstovi, "vijest, najava, izvjestaj")
    print(json.dumps(rezultat, ensure_ascii=False, indent=2))

    print("\n=== 2. LLM sažetak ===")
    tekst = """
    Digitalna humanistika razvija se kao interdisciplinarno polje koje povezuje
    računalne metode s tradicionalnim humanističkim istraživanjima. U zadnjih
    deset godina veliki jezični modeli omogućili su automatsku analizu golemih
    korpusa tekstova, što je otvorilo nove mogućnosti, ali i etičke izazove
    vezane uz pristranost, privatnost i interpretaciju.
    """
    print(llm_sazetak(model, tekst))
