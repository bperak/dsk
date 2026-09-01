# Poglavlje 7: Tekst i NLP — obrada tekstualnih podataka

---

## Sažetak poglavlja

Tekst je najčešći "podatak" u kulturnim istraživanjima: novinski članci,
objave na društvenim mrežama, arhivski dokumenti, književna djela, katalozi.
Ovo poglavlje uvodi obradu prirodnog jezika (NLP) od osnovnih tehnika —
tokenizacija, čišćenje, frekvencije, kolokacije — prema suvremenim
pristupima: embedding reprezentacije, automatsko označavanje LLM-om i
analiza sentimenta. Poseban naglasak na kritičkom pristupu: što tekstualna
analiza može, a što ne može reći.

---

## 7.1 Tekst kao podatak u kulturi

Tekstovi su **kulturni artefakti**: nose značenja, vrijednosti i ideologije.
Kada tekst tretiramo kao podatak, ne gubimo to — moramo ga zadržati u
vidu tijekom analize.

| Vrsta teksta | Primjer istraživačkog pitanja |
|--------------|-------------------------------|
| Novinski članci | Kako se izvještava o kulturi? Koje metafore dominiraju? |
| Društvene mreže | Kako se govori o muzejima? Koji sentiment? |
| Arhivski dokumenti | Što otkrivaju o povijesnim praksama? |
| Književnost | Koje teme, likovi, prostori? |
| Anketna otvorena pitanja | Kako ispitanici opisuju svoje navike? |
| Katalozi i metapodaci | Kako su djela opisana i klasificirana? |

> **Teorijski okvir — od teksta do korpusa.**
> **Korpus** je strukturirana, reprezentativna zbirka tekstova — ne
> "hrpa dokumenata" nego **dizajniran uzorak** (Sinclair 2005).
> Pitanja pri izgradnji korpusa: koji tekstovi, koliko, iz kojeg razdoblja,
> kojeg žanra, kako su odabrani? Odgovori određuju valjanost svega što slijedi.
> U doba LLM-ova korpus dobiva novu ulogu: postaje **izvor za RAG sustave**
> (pogl. 10) — sustav odgovara onoliko dobro koliko je korpus dobar.

---

## 7.2 Tokenizacija i čišćenje

### Tokenizacija

**Tokenizacija** razbija tekst na jedinice (tokene) — obično riječi ili
interpunkcijske znakove. Osnovni pristup:

```python
import re

tekst = "Kultura! Jezik, mišljenje i kultura — tri ključna pojma."
rijeci = re.findall(r"[a-zžćčšđ]+", tekst.lower())
print(rijeci)
# ['kultura', 'jezik', 'mišljenje', 'i', 'kultura', 'tri', 'ključna', 'pojma']
```

**Suvremena tokenizacija (BPE):** LLM-ovi ne koriste jednostavne razmake
nego **Byte Pair Encoding** — najčešće podriječi:

| Riječ | BPE tokeni |
|-------|-----------|
| "kultura" | ["kultura"] ili ["kul", "tura"] |
| "kulturologija" | ["kulturo", "logija"] |
| "umjetnost" | ["umjet", "nost"] |

Prednost: model uči morfologiju (zajedničke korijene) i rješava
nepoznate riječi. U Pythonu (tiktoken za OpenAI, sentencepiece za druge):

```python
# Primjer s tiktokenom
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
print(enc.encode("kulturologija"))   # [37371, 11461] — podriječi
```

> **Zašto je BPE važan za hrvatski?** Morfološki bogati jezici imaju
> tisuće oblika jedne riječi ("kultura", "kulture", "kulturi"...) —
> BPE ih povezuje kroz zajedničke podriječi, što poboljšava analizu
> i smanjuje "gluhe" tokene.

### Čišćenje teksta

```python
# Lowercase, uklanjanje interpunkcije, brojki (po potrebi)
cisto = re.sub(r"[^a-zžćčšđ\s]", " ", tekst.lower())
cisto = re.sub(r"\s+", " ", cisto).strip()
```

> **Oprez s čišćenjem!** Uklanjanje interpunkcije briše i značenje
> ("nije" vs "ne je" — negacija je ključna za sentiment). Uvijek čuvajte
> originalnu verziju teksta i dokumentirajte transformacije.

---

## 7.3 Frekvencije, kolokacije, n-grami

### Frekvencije riječi

```python
from collections import Counter

rijeci = re.findall(r"[a-zžćčšđ]+", tekst.lower())
frek = Counter(rijeci)
print(frek.most_common(10))
```

**Zipfov zakon** (pogl. 5): najčešća riječ ~2× češća od druge itd.
U hrvatskom su najčešće funkcionalne riječi: "i", "je", "u", "da", "se"...

### Stop-riječi

**Stop-riječi** su funkcionalne riječi bez sadržajnog značenja ("i", "a",
"se", "u", "na", "od"...). Uklanjamo ih kada nas zanimaju sadržajne riječi:

```python
STOP = set("""i a je u na da se o za sa od s iz kojega koji koja koje
sve kao što su ih im ga te ne ni no pa li""".split())

sadrzajne = [r for r in rijeci if r not in STOP]
```

### Kolokacije i n-grami

**N-grami** su nizovi od n riječi; **kolokacije** su n-grami koji se
javljaju češće od slučajnog:

```python
def ngrami(rijeci, n=2):
    return list(zip(*[rijeci[i:] for i in range(n)]))

# Bigrami
print(ngrami(["kultura", "i", "umjetnost", "u", "Rijeci"], 2))
# [('kultura', 'i'), ('i', 'umjetnost'), ('umjetnost', 'u'), ('u', 'Rijeci')]

# Najčešći bigrami
bigram_frek = Counter(ngrami(sadrzajne, 2))
print(bigram_frek.most_common(10))
```

> **Kolokacije u kulturnim istraživanjima:** kolokacije "muzeja" u
> novinskom korpusu ("posjetiti", "izložba", "ulaznica", "kustos")
> otkrivaju diskurzivne okvire — kako se o kulturnoj ustanovi govori.

---

## 7.4 Od frekvencija do značenja

Frekvencije govore **što se pojavljuje**, ali ne i **što znači**.
Za značenje idemo dalje:

### Embedding: riječi kao vektori

Riječi sličnog značenja imaju slične vektore (detalji u pogl. 9):

```python
import google.generativeai as genai

r = genai.embed_content(
    model="models/text-embedding-004",
    content=["kultura", "umjetnost", "sloboda", "stolica"],
)
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

vektori = np.array(r["embedding"])
sim = cosine_similarity(vektori)
print(sim[0, 1])   # kultura ~ umjetnost: visoko
print(sim[0, 3])   # kultura ~ stolica: nisko
```

### LLM označavanje: automatizirana klasifikacija

LLM-ovi označavaju tekstove bez ručnog treniranja modela:

```python
prompt = """
Klasificiraj svaki tekst u jednu kategoriju: [vijest, najava, izvještaj].
Vrati VALIDAN JSON: {"rezultati": [{"id": 1, "kategorija": "..."}]}

Tekstovi:
[{"id": 1, "tekst": "Izložba otvorena u Muzeju moderne umjetnosti..."}]
"""
odgovor = model.generate_content(prompt)
import json
print(json.loads(odgovor.text))
```

### Analiza sentimenta

```python
def sentiment(tekst):
    p = f"Ocijeni sentiment (pozitivan/negativan/neutralan) s vjerojatnošću. JSON: {{'sentiment': '...', 'vjerojatnost': 0.9}}. Tekst: {tekst}"
    r = model.generate_content(p)
    return json.loads(r.text)

print(sentiment("Muzej je otvorio fantastičnu novu izložbu!"))
# {'sentiment': 'pozitivan', 'vjerojatnost': 0.95}
```

### Tematsko modeliranje (uvod)

Za otkrivanje tema u velikom korpusu koriste se LDA ili, suvremenije,
embedding + klasteriranje (k-means nad vektorima). Pregled:

```python
from sklearn.cluster import KMeans
model_km = KMeans(n_clusters=3, n_init=10)
grupe = model_km.fit_predict(vektori)
```

---

## 7.5 Kritički pristup tekstualnoj analizi

### Što tekstualna analiza MOŽE

- Otkriti obrasce na velikim razmjerima (tisuće tekstova)
- Kvantificirati (koliko često, gdje, kada)
- Podržati hipoteze dokazima iz korpusa
- Usporediti korpuse (žanrovi, razdoblja, jezici)

### Što tekstualna analiza NE MOŽE (sama)

- Reći **zašto** se obrasci javljaju (treba teorija)
- Razumjeti **ironiju i kontekst** (LLM-ovi to rade bolje od frekvencija,
  ali i dalje griješe)
- Zamijeniti **čitanje** — dubinsko razumijevanje pojedinačnih tekstova
- Biti **neutralna** — svaki korpus, čišćenje i kategorija su izbori

### Provjera LLM rezultata

| Rizik | Primjer | Provjera |
|-------|---------|----------|
| Halucinacija | Izmišljen citat iz korpusa | Uvijek pronađi u izvorniku |
| Pristranost | Manjinski glasovi podzastupljeni | Provjeri sastav korpusa |
| Anakronizam | Moderno značenje u starom tekstu | Povijesni kontekst |
| Circularnost | Model "potvrđuje" pretpostavke | Neovisna validacija |

> **Rubrika "Što ako ne radi?"**
> - Model vraća markdown umjesto JSON-a → `odgovor.text.strip().removeprefix("```json")`
> - Encoding problemi s dijakritičkim znakovima → uvijek `encoding="utf-8"`
> - Previše/malo stop-riječi → prilagodi listu svom korpusu (provjeri
>   najčešće riječi pa odluči)

---

## Praktikum: mini-analiza korpusa

```python
import re
from collections import Counter
import google.generativeai as genai

korpus = [
    "Muzej je otvorio novu izložbu o industrijskoj baštini Rijeke.",
    "Kazalište najavljuje sezonu s tri premijere domaćih autora.",
    "Posjećenost muzeja porasla je za 20 posto u protekloj godini.",
    "Gradska knjižnica organizira radionice digitalne pismenosti.",
    "Umjetnici traže veću potporu grada za nezavisnu scenu.",
]

# 1. Frekvencije
sve = " ".join(korpus).lower()
frek = Counter(re.findall(r"[a-zžćčšđ]+", sve))
print("Top riječi:", frek.most_common(8))

# 2. Kolokacije "muzej"
for tekst in korpus:
    if "muzej" in tekst:
        print("→", tekst)

# 3. LLM: teme korpusa
odgovor = model.generate_content(
    f"Koje su tri glavne teme ovog korpusa? Navedi primjere. Korpus: {korpus}"
)
print(odgovor.text)
```

---

## Vježbe

### 🟢 Osnovna
1. Preuzmite 5-10 tekstova (npr. kulturne vijesti s portala) i izgradite
   mini-korpus. Tokenizirajte, izračunajte frekvencije i top 10 sadržajnih riječi.
2. Napravite listu stop-riječi za svoj korpus i objasnite izbor.

### 🟡 Srednja
3. Izračunajte najčešće bigrame (kolokacije) oko jednog ključnog pojma
   (npr. "muzej", "kultura", "umjetnik"). Što otkrivaju?
4. LLM-om klasificirajte svoj korpus (vijest/najava/izvještaj) i provjerite
   točnost na 5 primjera ručno.

### 🏆 Napredna
5. Usporedite frekvencijski pristup i LLM pristup na istom korpusu:
   koje uvide svaki daje, a koje ne? Zapišite kao malu raspravu.
6. Analiza sentimenta na komentarima (npr. YouTube recenzije muzeja):
   prikupite 20-30 komentara, analizirajte sentiment, provjerite 5 ručno.

---

## Sažetak i ključni pojmovi

- Tekst je kulturni artefakt; korpus je dizajniran uzorak, ne hrpa dokumenata.
- Tokenizacija (osnovna + BPE), čišćenje, stop-riječi, frekvencije.
- N-grami i kolokacije otkrivaju diskurzivne okvire.
- Za značenje: embedding, LLM označavanje, sentiment, klasteriranje.
- Kritički pristup: korpus/čišćenje/kategorije su izbori; LLM rezultate
  uvijek provjeravajte (halucinacije!).

**Ključni pojmovi:** korpus, tokenizacija, BPE, stop-riječi, n-gram,
kolokacija, embedding, sentiment analiza, označavanje, Zipfov zakon.

---

## Literatura

- Sinclair, J. (2005). Corpus and Text — Basic Principles. U *Developing Linguistic Corpora*.
- Jurafsky, D., & Martin, J. H. (2025). *Speech and Language Processing* (3. izd.). Stanford. (open access)
- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije*. FFRI Rijeka.
- Bird, S., Klein, E., & Loper, E. (2009). *Natural Language Processing with Python*. O'Reilly.
