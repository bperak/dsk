# 09. Embedding i semantička pretraga

**Kolegij:** Data Science u kulturi | 2026./2027.

## Što je embedding?

**Embedding** pretvara tekst u vektor brojeva (npr. 768 dimenzija).
Slični tekstovi imaju slične vektore → bliski u vektorskom prostoru.

```python
from google import genai
import numpy as np

EMB_MODEL = "gemini-embedding-2"
client = genai.Client()
resp = client.models.embed_content(model=EMB_MODEL, contents=["kultura", "umjetnost"])
vektori = np.array([e.values for e in resp.embeddings])
```

## Kosinusna sličnost

Mjeri kut između vektora (1 = identično, 0 = nepovezano):

```python
from sklearn.metrics.pairwise import cosine_similarity
sim = cosine_similarity([vektor_upita], vektori_zbirke)
```

## Semantička pretraga

Umjesto pretrage po ključnim riječima, pretraga po **značenju**:
upit "morski pejzaži" nalazi i zapise koji ne sadrže te riječi
(npr. "ribar", "brod", "val").

## Primjena u kulturi

- Pretraga muzejskih zbirki po temi
- Preporuka sadržaja ("slično ovome")
- Deduplikacija (isti sadržaj, različite riječi)
- Grupiranje (klasteriranje) kulturnih sadržaja

## Ishodi učenja (3, 8)

- Koristiti javne data-science alate uključujući AI alate.
- Praktične vještine digitalne humanistike.

## Praktično

Skripta: `scripts/06_semanticka_pretraga.py`
