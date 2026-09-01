# 08. LLM u podatkovnoj znanosti

**Kolegij:** Data Science u kulturi | 2026./2027.

## Što je LLM?

**Veliki jezični model (LLM)** je model treniran na golemim količinama teksta
koji može generirati, analizirati i transformirati jezik. Primjeri: Gemini,
GPT, Llama, Claude.

**Ključna ideja (Perak 2025):** LLM je **komunikacijski agent** — ne samo alat
za tekst, nego sučelje prema podacima i alatima.

## Primjene u podatkovnoj znanosti

| Zadatak | Primjer |
|---------|---------|
| Klasifikacija | Sentiment recenzija, kategorije sadržaja |
| Ekstrakcija | Entiteti iz teksta (osobe, mjesta, datumi) |
| Sažimanje | Sažetak izvješća |
| Generiranje koda | Pandas analiza iz prirodnog jezika |
| Označavanje | Automatsko kodiranje kvalitativnih podataka |
| Interpretacija | Tumačenje statističkih rezultata |

## Structured output (JSON)

```python
prompt = "Vrati JSON: {\"sentiment\": \"...\", \"vjerojatnost\": 0.9}"
odgovor = model.generate_content(prompt)
import json
data = json.loads(odgovor.text)
```

## Kritičko vrednovanje

| Rizik | Mitigacija |
|-------|-----------|
| Halucinacije | Provjera izvora, RAG |
| Pristranost korpusa | Auditi reprezentacije |
| Anakronizmi | Stručni pregled |
| Nepouzdani brojevi | Uvijek provjeriti izračune |

**Pravilo:** LLM je asistent za prvi nacrt — konačno tumačenje je na istraživaču.

## Ishodi učenja (6, 8)

- Kritički vrednovati rezultate AI alata.
- Koristiti praktične vještine digitalne humanistike uz LLM.

## Praktično

Skripta: `scripts/05_llm_analiza.py`
