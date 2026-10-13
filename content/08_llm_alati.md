# 08. LLM u podatkovnoj znanosti

**Kolegij:** Data Science u kulturi | 2026./2027.

> **U ovoj cjelini.** Upoznajemo veliki jezični model (LLM) kao radni alat podatkovne znanosti. Vidjet ćemo za koje je zadatke koristan — klasifikaciju, ekstrakciju entiteta, sažimanje, generiranje koda, označavanje i interpretaciju — kako se od njega traži strojno čitljiv izlaz i zašto je taj ugovor izlaza toliko važan. Jednako važan dio cjeline je kritičko vrednovanje: gdje model griješi, kako se to prepoznaje i kako se svaki rezultat provjerava.
>
> **Ishodi:** **DSK-6** Kritički vrednovati rezultate AI alata. · **DSK-8** Koristiti praktične vještine digitalne humanistike uz LLM.
>
> **Uz ovu cjelinu idu:** skripta [`scripts/05_llm_analiza.py`](scripts/05_llm_analiza.py), bilježnica [`colab/DSK_analiza_upitnika_Rijeka.ipynb`](colab/DSK_analiza_upitnika_Rijeka.ipynb) i sljedeća cjelina [09. Embedding i semantička pretraga](content/09_embedding_pretraga.md).

Veliki jezični modeli promijenili su način na koji humanisti rade s tekstom. Posao koji je nekada tražio tim označivača i tjedne rada — klasificirati stotine odgovora iz upitnika, izvući osobe i mjesta iz novinskih članaka, sažeti izvješće — danas se može obaviti u nekoliko minuta. Ali upravo zato što je posao tako brz, odgovornost provjere ostaje na istraživaču i postaje veća, a ne manja.

## Što je LLM?

**Veliki jezični model (LLM)** je model treniran na golemim količinama teksta koji može generirati, analizirati i transformirati jezik. Primjeri: Gemini, GPT, Llama, Claude.

U svojoj osnovi model neprestano rješava jedan zadatak: predviđa koji sljedeći token (riječ ili dio riječi) najvjerojatnije dolazi. Iz tog jednostavnog postupka, ponovljenog milijardama puta na velikom korpusu, izrastaju sposobnosti koje nalikuju razumijevanju jezika — prepoznavanje žanra, tona, entiteta i odnosa među njima.

**Ključna ideja (Perak 2025):** LLM je **komunikacijski agent** — ne samo alat za tekst, nego sučelje prema podacima i alatima. Kada modelu pridružimo pristup tablicama, arhivima ili vanjskim programima, on prestaje biti samo razgovorni partner i postaje posrednik između istraživača i njegove građe.

| Pojam | Značenje |
|-------|----------|
| Model | program treniran na velikim količinama teksta |
| Prompt | uputa koju modelu zadajemo |
| Kontekst | tekst koji model dobiva uz uputu |
| Token | jedinica teksta koju model obrađuje |
| Slučajnost generiranja | mjera koliko model odstupa od najvjerojatnijeg izlaza |
| Komunikacijski agent | model kao sučelje prema podacima i alatima |

**Mali primjer.** Novinar pita: „Koliko je izložaba najavljeno u ovom godištu?" Model koji ima pristup tekstu godišta prebroji najave i vrati odgovor. Model koji pristup nema može odgovoriti samouvjereno, ali pogrešno — to je razlika između agenta i pukog razgovora.

```python
import os
from google import genai

KLJUC = os.environ["GEMINI_API_KEY"]
klijent = genai.Client(api_key=KLJUC)

prompt = "Objasni u dvije rečenice što je kulturna baština."
odgovor = klijent.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
)
print(odgovor.text)
```

## Primjene u podatkovnoj znanosti

| Zadatak | Primjer |
|---------|---------|
| Klasifikacija | Sentiment recenzija, kategorije sadržaja |
| Ekstrakcija | Entiteti iz teksta (osobe, mjesta, datumi) |
| Sažimanje | Sažetak izvješća |
| Generiranje koda | Pandas analiza iz prirodnog jezika |
| Označavanje | Automatsko kodiranje kvalitativnih podataka |
| Interpretacija | Tumačenje statističkih rezultata |

Svaki od tih zadataka u kulturnom istraživanju ima svoj tipičan oblik. Klasifikacija je najčešća: tko je izjavu dao i u kojem žanru. Ekstrakcija je najkorisnija za izgradnju registara — osoba, mjesta, djela i godina iz novinskog teksta. Sažimanje je polazište, a ne završetak: sažetak se vraća u izvornik. Generiranje koda spaja jezik i računanje, jer model prevodi rečenicu u naredbe nad tablicom. Označavanje je most prema kvalitativnoj analizi, a interpretacija služi kao drugi pogled na vlastite brojke.

| Zadatak | Što dobivate na izlazu | Primjer iz kulture |
|---------|------------------------|--------------------|
| Klasifikacija | oznaku kategorije i vjerojatnost | recenzija izložbe: pozitivna ili kritična |
| Ekstrakcija | popis entiteta s tipom | kazalište, godina gradnje, kustos |
| Sažimanje | kraći tekst s ključnim podacima | sažetak godišnjeg izvješća muzeja |
| Generiranje koda | naredbu nad tablicom | „prosječna ocjena po žanru" → `groupby` |
| Označavanje | kod ili temu uz svaki odgovor | otvoreni odgovori iz upitnika |
| Interpretacija | objašnjenje rezultata | tumačenje korelacije dobi i posjeta |

**Mali primjer (upitnik).** U bilježnici s upitnikom „Gdje se izlazi van u Rijeci" model može preuzeti posao koji je inače najsporiji: svrstati stotine slobodnih odgovora u nekoliko tema (muzika, sport, kultura) i izdvojiti nazive mjesta. Istraživač zatim provjerava dodjele na uzorku i ispravlja kategorije.

## Structured output (JSON)

Ako od modela tražimo da razgovara, dobit ćemo rečenice. Ako od njega tražimo podatak koji ide dalje u analizu, moramo tražiti **ugovor izlaza** — točno određenu strukturu, najčešće JSON. Ugovor je važan iz tri razloga: takav se izlaz može strojno učitati, može se ponovno dobiti na isti način i može se provjeriti po poljima.

```python
MODEL = "gemini-3.5-flash"
prompt = "Vrati JSON: {\"sentiment\": \"...\", \"vjerojatnost\": 0.9}"
odgovor = klijent.models.generate_content(
    model=MODEL,
    contents=prompt,
    config={"response_mime_type": "application/json"},
)
import json
print(json.loads(odgovor.text))
```

| Zahtjev | Zašto je u promptu | Što sprečava |
|---------|--------------------|--------------|
| Točna shema polja | izlaz mora odgovarati tablici koja ga čeka | polja koja analiza ne može učitati |
| Vjerojatnost uz odluku | omogućuje provjeru nesigurnih slučajeva | slijepo povjerenje svakoj oznaci |
| Bez markdowna | tekst se mora moći izravno parsirati | kodne ograde oko JSON-a |

```python
tekst_odgovora = odgovor.text.strip()
ograda = chr(96) * 3   # tri obrnuta navodnika — markdown ograda
if tekst_odgovora.startswith(ograda):
    tekst_odgovora = tekst_odgovora.strip(chr(96)).removeprefix("json").strip()
podaci = json.loads(tekst_odgovora)
```

## Kritičko vrednovanje

| Rizik | Mitigacija |
|-------|-----------|
| Halucinacije | Provjera izvora, RAG |
| Pristranost korpusa | Auditi reprezentacije |
| Anakronizmi | Stručni pregled |
| Nepouzdani brojevi | Uvijek provjeriti izračune |

**Pravilo:** LLM je asistent za prvi nacrt — konačno tumačenje je na istraživaču.

Halucinacija u kulturnom istraživanju nije apstraktna opasnost. Model može vezati poznato djelo uz krivu godinu, izmisliti kustosa ili pripisati citat autoru koji ga nikada nije napisao — i to učiniti tečno, bez ograde. Pristranost dolazi iz korpusa: ako su izvori o kulturi pisali samo o središtu grada, model će i o periferiji govoriti rjeđe. Anakronizam se javlja kada starom tekstu pripišemo moderno značenje. Brojke su posebno osjetljive jer model računa „otprilike": svaki zbroj i postotak provjeravamo vlastitim izračunom.

| Što provjeravamo | Kako | Primjer |
|------------------|------|---------|
| Činjenicu | traženje u izvorniku | godina gradnje zgrade |
| Citat | usporedba s izvornim tekstom | ulomak iz romana ili pjesme |
| Broj | ponovni izračun | prosjek ocjena iz upitnika |
| Reprezentaciju | pregled sastava korpusa | koje su četvrti zastupljene |

## Ishodi učenja (6, 8)

- Kritički vrednovati rezultate AI alata.
- Koristiti praktične vještine digitalne humanistike uz LLM.

| Ishod | Kako se ostvaruje u ovoj cjelini |
|-------|----------------------------------|
| Kritičko vrednovanje (6) | Provjera klasifikacije i ekstrakcije na uzorku; traženje halucinacija |
| Digitalna humanistika (8) | Primjena modela na vlastiti korpus i strukturirani izlaz |

## Ključni pojmovi

| Pojam | Značenje |
|-------|----------|
| LLM | veliki jezični model treniran na velikim količinama teksta |
| Prompt | uputa modelu; određuje zadatak i oblik odgovora |
| Token | jedinica teksta koju model obrađuje |
| Klasifikacija | svrstavanje teksta u unaprijed zadane kategorije |
| Ekstrakcija entiteta | pronalaženje osoba, mjesta, djela i datuma |
| Structured output | dogovoreni strojno čitljiv oblik izlaza (JSON) |
| Ugovor izlaza | točna shema polja koju izlaz mora zadovoljiti |
| Halucinacija | tvrdnja modela bez osnove u izvoru |
| Pristranost | neravnomjeran prikaz pojava zbog sastava korpusa |
| RAG | dohvat dokaza iz korpusa prije generiranja odgovora |

## Provjeri razumiješ

1. Zašto je za analizu podataka bolje tražiti JSON nego slobodan tekst?
2. Što znači da je LLM „komunikacijski agent", a ne samo alat za tekst?
3. Navedi dvije vrste pogreške modela i način na koji ih provjeravate.
4. Zašto model može samouvjereno dati pogrešan broj i kako se od toga branimo?

<details><summary>Odgovori</summary>

1. Zato što se JSON može izravno učitati u program, provjeriti po poljima i ponovno dobiti na isti način. Slobodan tekst treba najprije pretvoriti u podatak, a to je dodatni i nepouzdan korak.

2. Model postaje agent kada mu pridružimo pristup podacima i alatima. Tada ne odgovara samo iz pamćenja, nego djeluje na građi — pretražuje, računa i vraća odgovor vezan na izvor.

3. Halucinacija (izmišljen podatak) provjerava se traženjem u izvorniku, a pristranost provjerava se pregledom sastava korpusa. Mogu se navesti i anakronizam te pogrešan izračun, uz odgovarajuće provjere.

4. Zato što model predviđa vjerojatan tekst, a ne računa točno. Branimo se tako da svaki broj izračunamo sami i usporedimo s modelovim odgovorom.

</details>

## Praktično

Povezana skripta i bilježnica: [`scripts/05_llm_analiza.py`](scripts/05_llm_analiza.py), [`colab/DSK_analiza_upitnika_Rijeka.ipynb`](colab/DSK_analiza_upitnika_Rijeka.ipynb).

- 🟢 Pokreni skriptu i zapiši rezultat klasifikacije triju ugrađenih tekstova. Slaže li se oznaka s tvojim čitanjem?
- 🟢 Iz teksta s entitetima izdvoji osobe, mjesta i godine; provjeri svaki entitet u izvoru.
- 🟡 Dodaj u skriptu pet novih tekstova i pusti klasifikaciju. Ručno ocijeni točnost na svih pet.
- 🟡 Zatraži sažetak na tri rečenice i uporedi ga s izvornim tekstom; zabilježi što je izostavljeno i je li što dodano.
- 🏆 Sastavi vlastiti prompt za označavanje otvorenih odgovora iz upitnika, traži JSON po zadanoj shemi, zatim provjeri dvadeset dodjela ručno i napiši kratko izvješće o pogreškama.

## Dalje

Model sada može čitati i označavati naš tekst, ali još ne umije pronaći najbliži sadržaj po značenju. Sljedeća cjelina, [09. Embedding i semantička pretraga](content/09_embedding_pretraga.md), uvodi upravo taj korak — prikaz teksta kao vektora i pretragu koja razumije temu, a ne samo riječi.

## Literatura

- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije: Razvoj velikih jezičnih modela i komunikacijskih agenata*. Rijeka: Filozofski fakultet u Rijeci. Open access: https://github.com/bperak/komunikacija_u_doba_ai
- Bommasani et al. (2021). *On the Opportunities and Risks of Foundation Models*. arXiv:2108.07258
- Grus, J. (2019). *Data Science from Scratch*. O'Reilly.
- Python za lingviste: https://github.com/nljubesi/python-for-linguists
