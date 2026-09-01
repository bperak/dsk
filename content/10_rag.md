# 10. RAG — razgovor s kulturnom baštinom

**Kolegij:** Data Science u kulturi | 2026./2027.

## Što je RAG?

**RAG (Retrieval-Augmented Generation)** = dohvat + generiranje:

1. Korisnik postavi pitanje
2. Sustav pronađe najrelevantnije dijelove korpusa (embedding pretraga)
3. LLM generira odgovor **temeljen na dohvaćenim dokazima**

```
Pitanje → Embedding upita → Pretraga korpusa → Top-k dokaza
       → LLM (dokazi + pitanje) → Odgovor s citatima
```

## Zašto RAG?

- **Rješava halucinacije** — model odgovara iz vašeg korpusa, ne iz pamćenja
- **Ažurnost** — korpus se može mijenjati bez retreniranja modela
- **Transparentnost** — svaki odgovor ima izvore
- **Privatnost** — podaci ne napuštaju vaš korpus

## Primjena u kulturi

- Muzejski asistent: "Što se nalazi u Guvernerovoj palači?"
- Arhivska pretraga: "Kada je sagrađeno kazalište?"
- Digitalna knjižnica: razgovor sa zbirkom dokumenata
- Znanstveni asistent: odgovori temeljeni na vašoj literaturi

## Prompt za RAG

```
Odgovori ISKLJUČIVO na temelju dokaza.
Ako odgovor nije u dokazima, reci: "Nije navedeno u izvorima."
Citiraj izvor: (izvor [N])

Dokazi:
[1] ...
[2] ...

Pitanje: ...
```

## Ishodi učenja (6, 8)

- Kritički vrednovati AI rezultate (RAG kao mitigacija halucinacija).
- Koristiti praktične vještine digitalne humanistike.

## Praktično

Skripta: `scripts/07_rag_kulturna_bastina.py`
