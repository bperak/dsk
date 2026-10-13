# 09. Embedding i semantička pretraga

**Kolegij:** Data Science u kulturi | 2026./2027.

> **U ovoj cjelini.** Učimo kako se tekst pretvara u vektor brojeva — **embedding** — i kako se iz toga gradi pretraga po značenju. Umjesto podudaranja istih riječi, uspoređivat ćemo položaj tekstova u vektorskom prostoru mjerom **kosinusne sličnosti**. Vidjet ćemo zašto upit „morski pejzaži" pronalazi i zapis „portret ribara s mrežama", te kako se to koristi u muzejskim zbirkama, preporukama, uklanjanju duplikata i grupiranju kulturnih sadržaja.
>
> **Ishodi:** **DSK-3** Koristiti javne data-science alate uključujući AI alate. · **DSK-8** Praktične vještine digitalne humanistike.
>
> **Uz ovu cjelinu idu:** skripta [`scripts/06_semanticka_pretraga.py`](scripts/06_semanticka_pretraga.py), bilježnica [`colab/DSK_analiza_upitnika_Rijeka.ipynb`](colab/DSK_analiza_upitnika_Rijeka.ipynb) i sljedeća cjelina [10. RAG — razgovor s kulturnom baštinom](content/10_rag.md).

Klasifikacija iz prethodne cjeline svrstava tekst u kategorije koje smo unaprijed zadali. No često nam treba nešto drukčije: pronaći ono što je *najbliže* nekom sadržaju, ili otkriti koji su zapisi međusobno slični. Za takve zadatke ne trebaju nam kategorije, nego mjera blizine. Tu nastupa embedding.

## Što je embedding?

**Embedding** pretvara tekst u vektor brojeva (npr. 768 dimenzija). Slični tekstovi imaju slične vektore → bliski su u vektorskom prostoru. Svaka dimenzija nosi neko svojstvo koje je model naučio iz velikog korpusa: jednom je to „govori li tekst o moru", drugom „je li riječ o osobi ili predmetu", ali ta svojstva nisu unaprijed imenovana. Ono što je važno jest da se blizina u tom prostoru poklapa s blizinom po značenju.

| Pojam | Značenje |
|-------|----------|
| Embedding | prikaz teksta kao vektora brojeva |
| Vektor | niz brojeva koji opisuje položaj u prostoru |
| Dimenzija | broj komponenata vektora (npr. 768) |
| Vektorski prostor | prostor u kojem su značenja blizine razmaka |
| Semantička blizina | sličnost po značenju, a ne po riječima |
| Model embeddinga | model koji izračunava vektore (npr. `gemini-embedding-2`) |

```python
from google import genai
import numpy as np

EMB_MODEL = "gemini-embedding-2"
client = genai.Client()
resp = client.models.embed_content(model=EMB_MODEL, contents=["kultura", "umjetnost"])
vektori = np.array([e.values for e in resp.embeddings])
```

**Mali primjer.** Uzmimo četiri pojma iz kulturne sfere: „muzej", „galerija", „izložba" i „cijena". Prva tri vektora završit će blizu jedan drugome jer se u tekstovima o kulturi pojavljuju u sličnim okruženjima; vektor riječi „cijena" bit će udaljen. Model tu blizinu nije naučio iz rječnika, nego iz toga kako se riječi stvarno ponašaju u rečenicama. Zato vrijedi načelo **distribucijske semantike**: značenje riječi određeno je kontekstima u kojima se pojavljuje.

## Kosinusna sličnost

Mjeri kut između vektora (1 = identično, 0 = nepovezano):

```python
from sklearn.metrics.pairwise import cosine_similarity
sim = cosine_similarity([vektor_upita], vektori_zbirke)
```

Kut, a ne udaljenost, zato što nas zanima smjer u kojem vektor pokazuje, a ne njegova duljina. Dva teksta različite duljine — kratak muzejski natpis i dugačak kustoski opis — mogu govoriti o istoj temi, pa je mjera koja zanemaruje duljinu pravednija.

| Vrijednost | Što znači | Primjer |
|------------|-----------|---------|
| 1,0 | vektori se poklapaju u smjeru | isti zapis dvaput |
| 0,8–0,9 | vrlo srodni pojmovi | „muzej" i „galerija" |
| 0,5–0,7 | povezani, ali različiti | „izložba" i „katalog" |
| oko 0,0 | nepovezani | „muzej" i „cijena" |
| negativno | suprotan smjer | rijetko; znak obrata teme |

```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

sim = cosine_similarity(vektori)
print(f"kultura ~ umjetnost: {sim[0, 1]:.3f}")
```

Skaliranje vektora na jediničnu duljinu prije usporedbe ubrzava pretragu i ne mijenja poredak rezultata — zato se kosinusna sličnost često računa izravno kao skalarni produkt normaliziranih vektora.

## Semantička pretraga

Umjesto pretrage po ključnim riječima, pretraga po **značenju**: upit „morski pejzaži" nalazi i zapise koji ne sadrže te riječi (npr. „ribar", „brod", „val"). Klasična tražilica traži znakove u tekstu; semantička tražilica smješta upit u isti vektorski prostor kao i zapise, pa poredak određuje blizina, a ne podudaranje.

| Upit | Klasična pretraga (riječi) | Semantička pretraga (značenje) |
|------|----------------------------|-------------------------------|
| „morski pejzaži" | pronalazi samo zapise s tim riječima | pronalazi i „ribar", „brod", „val" |
| „gradske znamenitosti" | traži riječ „znamenitost" | pronalazi „vijećnica", „toranj" |
| „cvjetni motivi" | traži „cvijet" | pronalazi „mrtva priroda s voćem" |

Rezultat pretrage uvijek je **poredak prvih k zapisa** (top-k). Broj k birate prema namjeri: manji za precizan odgovor, veći kada želite pregledati širu sliku.

```python
from sklearn.metrics.pairwise import cosine_similarity

def pronadi(upit_vektor, vektori_zbirke, opisi, k=3):
    sim = cosine_similarity([upit_vektor], vektori_zbirke)[0]
    redoslijed = sim.argsort()[::-1][:k]
    for i in redoslijed:
        print(f"{sim[i]:.3f}  {opisi[i]}")
```

**Mali primjer (novinski članak).** Istraživač traži sve tekstove o „zagađenju mora". U arhivu lokalnih novina zapisi govore o „naftnoj mrlji", „otpadnim vodama" i „obali pod pritiskom". Nijedan ne sadrži upitne riječi, ali svi su blizu upitu po značenju — semantička pretraga ih pronalazi, a klasična ne bi.

## Primjena u kulturi

- Pretraga muzejskih zbirki po temi
- Preporuka sadržaja („slično ovome")
- Deduplikacija (isti sadržaj, različite riječi)
- Grupiranje (klasteriranje) kulturnih sadržaja

| Primjena | Što rješava | Primjer iz kulture |
|----------|-------------|--------------------|
| Pretraga zbirke | pronalazak po temi, ne po riječima | „prikazi mora" u zbirci pomorskog muzeja |
| Preporuka | nudi sadržaj sličan onome koji je odabran | „slično ovoj slici" u digitalnoj galeriji |
| Deduplikacija | spaja dvostruke zapise različitog naziva | isti izložak u dva kataloga |
| Klasteriranje | otkriva skupine srodnih zapisa | tematske skupine u zbirci grafika |

```python
import numpy as np
from sklearn.cluster import KMeans

grupe = KMeans(n_clusters=3, n_init=10).fit_predict(vektori)
print(np.bincount(grupe))
```

U klasteriranju ne zadajemo kategorije unaprijed — one izlaze iz same građe. Tako se, primjerice, u velikoj zbirci fotografija mogu sama izdvojiti tematska žarišta: luka, tržnica, škola, obala. Istraživač zatim gleda što je u kojoj skupini i daje joj ime.

## Ishodi učenja (3, 8)

- Koristiti javne data-science alate uključujući AI alate.
- Praktične vještine digitalne humanistike.

| Ishod | Kako se ostvaruje u ovoj cjelini |
|-------|----------------------------------|
| Javni AI alati (3) | Izračun embeddinga modelom `gemini-embedding-2` i pretraga kosinusnom sličnošću |
| Digitalna humanistika (8) | Pretraga, preporuka i grupiranje vlastite kulturne zbirke opisa |

## Ključni pojmovi

| Pojam | Značenje |
|-------|----------|
| Embedding | prikaz teksta kao vektora brojeva |
| Vektor | niz brojeva koji određuje položaj u prostoru |
| Dimenzija | broj komponenata vektora |
| Vektorski prostor | prostor u kojem blizina odgovara značenju |
| Kosinusna sličnost | mjera kuta među vektorima (1 = poklapanje) |
| Semantička pretraga | pretraga po značenju, ne po riječima |
| Top-k | prvih k najsličnijih zapisa u rezultatu |
| Preporuka | nudenje sadržaja sličnog odabranome |
| Deduplikacija | prepoznavanje istog sadržaja u različitim zapisima |
| Klasteriranje | grupiranje srodnih zapisa bez zadanih kategorija |

## Provjeri razumiješ

1. Zašto upit „morski pejzaži" može pronaći zapis „portret ribara s mrežama"?
2. Zašto kosinusna sličnost mjeri kut, a ne udaljenost među vektorima?
3. Po čemu se semantička pretraga razlikuje od pretrage po ključnim riječima?
4. Čemu služi klasteriranje u kulturnoj zbirci?

<details><summary>Odgovori</summary>

1. Zato što se oba teksta pretvaraju u vektore koji su blizu u vektorskom prostoru. Riječ „ribar", „mreža" i „more" pojavljuju se u sličnim kontekstima u korpusu, pa model njihove vektore smješta blizu.

2. Zato što nas zanima smjer u kojem vektor pokazuje — čemu je tekst sličan — a ne koliko je dug. Dva teksta različite duljine mogu govoriti o istoj temi, a mjera kuta zanemaruje razliku u duljini.

3. Klasična pretraga traži znakove, odnosno točne riječi u tekstu. Semantička pretraga uspoređuje vektore, pa pronalazi zapise koji govore o istoj temi i onda kada ne sadrže nijednu upitnu riječ.

4. Klasteriranje izdvaja skupine srodnih zapisa bez unaprijed zadanih kategorija. Time se u velikoj zbirci sama pokažu tematska žarišta, koja istraživač zatim pregleda i imenuje.

</details>

## Praktično

Povezana skripta i bilježnica: [`scripts/06_semanticka_pretraga.py`](scripts/06_semanticka_pretraga.py), [`colab/DSK_analiza_upitnika_Rijeka.ipynb`](colab/DSK_analiza_upitnika_Rijeka.ipynb).

- 🟢 Pokreni skriptu i zapiši za prvi upit tri najbliža opisa te njihove vrijednosti sličnosti.
- 🟢 Usporedi rezultat jednog upita s ručnim pogledom na popis opisa i procijeni je li poredak smislen.
- 🟡 Dodaj pet novih opisa (npr. stihovi pjesama ili muzejski natpisi) i provjeri kako se mijenja poredak za upit „more i brodovi".
- 🟡 Promijeni broj rezultata k od 1 do 5 za isti upit i zapiši u kojem trenutku počinju dolaziti nepovezani zapisi.
- 🏆 Izradi vlastitu malu zbirku od dvadesetak kulturnih zapisa, pokreni semantičku pretragu za tri upita i klasteriranje u tri skupine. U izvješću navedi koji su upiti dobro radili, gdje je pretraga promašila i koja je imena dobio svaki klaster.

## Dalje

Semantička pretraga vraća najbliže zapise, ali ne sastavlja odgovor. Sljedeća cjelina, [10. RAG — razgovor s kulturnom baštinom](content/10_rag.md), spaja dohvat s generiranjem: pronađeni ulomci postaju dokazi na kojima veliki jezični model gradi odgovor s citatima.

## Literatura

- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije: Razvoj velikih jezičnih modela i komunikacijskih agenata*. Rijeka: Filozofski fakultet u Rijeci. Open access: https://github.com/bperak/komunikacija_u_doba_ai
- Jurafsky, D., & Martin, J. H. (2025). *Speech and Language Processing* (3. izd.). Stanford. (open access)
- Grus, J. (2019). *Data Science from Scratch*. O'Reilly.
- Bommasani et al. (2021). *On the Opportunities and Risks of Foundation Models*. arXiv:2108.07258
- Python za lingviste: https://github.com/nljubesi/python-for-linguists
