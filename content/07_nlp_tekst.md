# 07. NLP — obrada tekstualnih podataka

**Kolegij:** Data Science u kulturi | 2026./2027.

> **U ovoj cjelini.** Tekst — novinski članak, stih pjesme, ulomak romana, muzejski opis, transkript razgovora — pretvaramo u podatak koji se može prebrojavati i mjeriti. Prolazimo osnovni put obrade prirodnog jezika (NLP): tokenizaciju, čišćenje, stop-riječi, frekvencije i kolokacije, a zatim i suvremeni put prema značenju — embedding, automatsko označavanje velikim jezičnim modelom, analizu sentimenta i tematsko modeliranje.
>
> **Ishodi:** **DSK-4** Primijeniti tehnike analize tekstualnih podataka. · **DSK-5** Analizirati kvalitativne tipove podataka.
>
> **Uz ovu cjelinu idu:** skripta [`scripts/04_nlp_obrada_teksta.py`](../scripts/04_nlp_obrada_teksta.py) i sljedeća cjelina [08. LLM u podatkovnoj znanosti](08_llm_alati.md).

## Zašto NLP u kulturi?

Tekstualni podaci (novinski članci, društvene mreže, arhivi, katalozi) čine velik dio humanističkih podataka. NLP (Natural Language Processing) omogućuje njihovu sustavnu analizu. Vrijedi odmah reći i ono što je lako zaboraviti: tekst nije samo građa, nego **kulturni artefakt**. On nosi značenja, vrijednosti i poglede na svijet. Kada tekst pretvorimo u brojeve, ta dimenzija ne smije nestati — zato brojanje riječi uvijek pratimo čitanjem i tumačenjem.

NLP ne zamjenjuje čitanje. On ga dopunjuje tako da pitanja koja bismo postavili o jednom tekstu postavimo o stotinama ili tisućama tekstova odjednom, i to ponovljivo.

| Vrsta teksta | Primjer istraživačkog pitanja |
|--------------|-------------------------------|
| Novinski članci | Kako se izvještava o kulturi i koje se riječi ponavljaju? |
| Pjesme | Koje se riječi ponavljaju u ljubavnoj lirici nekog razdoblja? |
| Romani | Koji se likovi, prostori i predmeti spominju najčešće? |
| Muzejski opisi | Kojim se riječima opisuju predmeti u katalogu? |
| Transkripti razgovora | Kako govornici uvode temu baštine i sjećanja? |
| Katalozi i metapodaci | Kako su djela klasificirana i opisana? |

**Mali primjer.** Uzmimo tri različita izvora: naslov novinskog članka („Muzej otvara izložbu o industrijskoj baštini Rijeke"), stih pjesme („more se sjeća svakoga broda") i inventarni opis („akvarel, prikaz riječke luke, 1931."). Za računalo su to u početku samo nizovi znakova. Nakon istih pet koraka sva tri postaju nizovi riječi s brojevima, koje možemo usporediti — iako svaki od njih pripada drugom žanru i drugoj ustanovi.

## Osnovni koraci

Put od sirovog teksta do prebrojane tablice uvijek je isti. Pet koraka u nastavku čine okosnicu svake tekstualne analize u digitalnoj humanistici.

1. **Tokenizacija** — razbijanje teksta na riječi
2. **Čišćenje** — lowercase, uklanjanje interpunkcije
3. **Stop-riječi** — uklanjanje čestih funkcionalnih riječi (i, a, se, u...)
4. **Frekvencije** — najčešće riječi
5. **Kolokacije** — česti spojevi riječi (bigrami, trigrami)

| Korak | Što se događa | Zašto je važan | Primjer iz kulture |
|-------|---------------|----------------|--------------------|
| Tokenizacija | tekst postaje niz jedinica (riječi) | bez jedinica nema brojanja | stih se razbija na riječi |
| Čišćenje | mala slova, uklanjanje interpunkcije | ista riječ ne smije se brojiti dvaput | „Kultura" i „kultura" postaju jedno |
| Stop-riječi | uklanjaju se česte funkcionalne riječi | u prvi plan izlaze noseće riječi | ostaju imenice: baština, izložba, luka |
| Frekvencije | broji se pojavljivanje | daje prvi pregled korpusa | najčešće riječi u godištu novina |
| Kolokacije | traže se česti spojevi riječi | pokazuje obrasce, ne samo pojedine riječi | „kulturna baština", „muzejska zbirka" |

```python
import re
from collections import Counter

rijeci = re.findall(r"[a-zžćčšđ]+", tekst.lower())
frekvencije = Counter(rijeci)
```

```python
tekst = "Kultura se prenosi kroz jezik, a jezik oblikuje kulturu."
rijeci = re.findall(r"[a-zžćčšđ]+", tekst.lower())
print(Counter(rijeci).most_common(3))
# [('jezik', 2), ('kultura', 1), ('se', 1)]
```

```python
STOP = {"i", "a", "se", "je", "u", "na", "od", "do", "kroz", "koji"}
sadrzajne = [r for r in rijeci if r not in STOP and len(r) > 1]

def bigrami(rijeci):
    return list(zip(rijeci, rijeci[1:]))

print(bigrami(sadrzajne))
```

Kolokacije „izložba" u novinskom korpusu — uz koje riječi najčešće stoji („otvorena", „kustos", „ulaznica") — otkrivaju diskurzivni okvir: način na koji se o kulturnoj ustanovi uopće govori.

## Dalje od frekvencija

Frekvencije govore **što se pojavljuje**, ali ne i **što znači**. Za značenje idemo dalje:

- **Embedding** — riječi kao vektori, sličnost po značenju
- **LLM označavanje** — automatska klasifikacija, ekstrakcija entiteta
- **Sentiment analiza** — emocionalni ton
- **Tematsko modeliranje** — teme u korpusu

| Pristup | Na koje pitanje odgovara | Primjer iz kulture |
|---------|--------------------------|--------------------|
| Embedding | Koje su riječi ili tekstovi bliski po značenju? | „pjesma" blizu „stih", daleko od „cijena" |
| LLM označavanje | Kojoj vrsti pripada ovaj tekst? | je li članak vijest, najava ili recenzija |
| Sentiment analiza | Kakav je emocionalni ton teksta? | ton recenzije izložbe |
| Tematsko modeliranje | Koje teme prožimaju veliki korpus? | teme u godištu lokalnih novina |

```python
import os
from google import genai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

KLJUC = os.environ["GEMINI_API_KEY"]
klijent = genai.Client(api_key=KLJUC)

EMB_MODEL = "gemini-embedding-2"
odgovor = klijent.models.embed_content(
    model=EMB_MODEL,
    contents=["pjesma", "stih", "roman", "cijena"],
)
vektori = np.array([e.values for e in odgovor.embeddings])
print(cosine_similarity(vektori))
```

Kada je izlaz modela potreban kao podatak, a ne kao tekst, tražimo strukturirani oblik. Tada je važno da model vrati **ugovor izlaza** — strojno čitljiv JSON po točno određenoj shemi.

```python
prompt = (
    "Klasificiraj naslov u kategoriju [vijest, najava, recenzija]. "
    "Vrati JSON: {\"kategorija\": \"...\"}. "
    "Naslov: 'Izložba u Muzeju moderne umjetnosti otvara se u petak'"
)
odgovor = klijent.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config={"response_mime_type": "application/json"},
)
print(odgovor.text)
```

Za otkrivanje tema u velikom korpusu često je dovoljno vektore grupirati u skupine.

```python
from sklearn.cluster import KMeans

grupe = KMeans(n_clusters=3, n_init=10).fit_predict(vektori)
```

## Kritički pristup

- Frekvencije ne govore o značenju — samo o pojavljivanju
- Stop-riječi mogu sakriti važne obrate
- LLM rezultate treba provjeriti (halucinacije)

Prvo upozorenje najlakše je pokazati na negaciji. Rečenice „izložba je dobra" i „izložba nije dobra" imaju gotovo istu frekvencijsku sliku, ali suprotan smisao — brojanje riječi tu razliku ne vidi. Drugo: preagresivno uklanjanje stop-riječi može izbrisati „ne", „ni" i veznike koji nose obrat u argumentu. Treće: jezični model može izmisliti podatak koji u korpusu ne postoji, pa se svaki citat i svaka godina provjeravaju u izvoru.

| Rizik | Kako se očituje | Kako se provjerava |
|-------|-----------------|--------------------|
| Frekvencija bez značenja | ista slika za tvrdnju i negaciju | pročitaj primjere, ne samo brojke |
| Izgubljen obrat | stop-riječi uklone „ne", „ni", „ali" | prilagodi listu stop-riječi svom korpusu |
| Halucinacija | izmišljen citat ili godina | pronađi tvrdnju u izvorniku |
| Pristranost korpusa | neki glasovi podzastupljeni | opiši sastav i način odabira tekstova |

**Pravilo:** brojka je početak pitanja, a ne odgovor. Rezultat NLP-a uvijek se vraća tekstu i čita.

## Ishodi učenja (4, 5)

- Primijeniti tehnike analize tekstualnih podataka.
- Analizirati kvalitativne tipove podataka.

## Ključni pojmovi

| Pojam | Značenje |
|-------|----------|
| Korpus | svrhovito odabrana zbirka tekstova za analizu |
| Tokenizacija | razbijanje teksta na jedinice — riječi |
| Token | jedna jedinica teksta (riječ ili znak) |
| Stop-riječi | česte funkcionalne riječi koje uklanjamo |
| Frekvencija | broj pojavljivanja riječi u korpusu |
| N-gram | niz od *n* uzastopnih riječi |
| Kolokacija | n-gram koji se javlja češće od slučajnoga |
| Embedding | prikaz teksta kao vektora brojeva |
| Sentiment analiza | mjerenje emocionalnog tona teksta |
| Halucinacija | tvrdnja modela bez osnove u izvoru |

## Provjeri razumiješ

1. Zašto dvije rečenice — „izložba je dobra" i „izložba nije dobra" — mogu imati gotovo istu frekvencijsku sliku?
2. Čemu služe stop-riječi i kada nam mogu nauditi?
3. Što je kolokacija i što nam otkriva u novinskom korpusu?
4. Zašto frekvencije riječi nisu dovoljne za tumačenje značenja?

<details><summary>Odgovori</summary>

1. Zato što brojanje gleda samo koje se riječi pojavljuju, a ne njihov redoslijed ni negaciju. Obje rečenice sadrže iste nosive riječi, a razlika je u riječi „nije" koju lako uklonimo među stop-riječi.

2. Stop-riječi uklanjamo da u prvi plan izađu nosive, sadržajne riječi. Naude kada izbrišu riječi koje nose obrat ili odnos — „ne", „ni", „ali", „bez" — jer tada analiza izgubi smisao rečenice.

3. Kolokacija je spoj riječi koji se javlja češće nego što bi se očekivalo slučajno, na primjer „kulturna baština". U novinskom korpusu pokazuje ustaljene načine govora o temi, odnosno diskurzivni okvir.

4. Zato što frekvencija mjeri pojavljivanje, a ne značenje. Da bismo došli do značenja, trebamo embedding, označavanje modelom ili tematsko modeliranje — i, u svakom slučaju, čitanje samih tekstova.

</details>

## Praktično

Povezana skripta: [`scripts/04_nlp_obrada_teksta.py`](../scripts/04_nlp_obrada_teksta.py).

- 🟢 Pokreni skriptu i zapiši broj tokena, broj tokena nakon stop-riječi te pet najčešćih riječi za oba ugrađena teksta.
- 🟢 Uzmi kratki stih ili naslov novinskog članka i ručno ga tokeniziraj na papiru; zatim isto napravi kodom i usporedi rezultat.
- 🟡 Izračunaj deset najčešćih bigrama u jednom od ugrađenih tekstova i objasni što ti spojevi otkrivaju.
- 🟡 Sastavi vlastiti mini-korpus od pet do deset kratkih kulturnih tekstova (naslovi, opisi, stihovi) i napravi frekvencijsku analizu.
- 🏆 Usporedi frekvencijski pristup i označavanje velikim jezičnim modelom na istom korpusu. Zapiši što svaki pristup vidi, a što prešućuje, i provjeri barem tri tvrdnje modela u izvornim tekstovima.

## Dalje

Frekvencije i kolokacije daju prvi pregled korpusa, ali ne i tumačenje. Sljedeća cjelina, [08. LLM u podatkovnoj znanosti](08_llm_alati.md), pokazuje kako veliki jezični model preuzima posao koji strojno brojanje ne može obaviti: klasifikaciju, ekstrakciju entiteta i sažimanje — uz jasna pravila provjere.

## Literatura

- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije: Razvoj velikih jezičnih modela i komunikacijskih agenata*. Rijeka: Filozofski fakultet u Rijeci. Open access: https://github.com/bperak/komunikacija_u_doba_ai
- Jurafsky, D., & Martin, J. H. (2025). *Speech and Language Processing* (3. izd.). Stanford. (open access)
- Grus, J. (2019). *Data Science from Scratch*. O'Reilly.
- Bommasani et al. (2021). *On the Opportunities and Risks of Foundation Models*. arXiv:2108.07258
- Python za lingviste: https://github.com/nljubesi/python-for-linguists
