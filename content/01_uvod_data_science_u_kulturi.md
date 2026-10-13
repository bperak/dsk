# 01. Uvod: Data Science u kulturi

> **U ovoj cjelini.** Naučit ćete što je podatkovna znanost u kulturi, s kojim se disciplinama
preklapa i zašto su veliki jezični modeli promijenili rad humanista s
podacima. Nakon cjeline moći ćete sami sastaviti istraživačko pitanje i
hipotezu.
> **Ishodi:** DSK-1 Opisati osnovne teorijske postavke znanosti o znanosti i procese planiranja znanstvenog istraživanja u društveno-humanističkim znanostima. DSK-2 Razumjeti teorijske pretpostavke kulturološki usmjerenih metoda data-science.
> **Uz ovu cjelinu idu:** poglavlje 1 knjige kolegija [Komunikacija u doba umjetne inteligencije](https://github.com/bperak/komunikacija_u_doba_ai) i [cjelina 02: Podaci u kulturi](02_podaci_fair_ai.md).

**Kolegij:** Data Science u kulturi | 2026./2027. | izv. prof. dr. sc. Benedikt Perak

## Što je data science u kulturi?

Data science u kulturi primjenjuje metode podatkovne znanosti (prikupljanje,
čišćenje, analiza, vizualizacija, interpretacija podataka) na istraživanja
kulturnih fenomena: kulturne prakse, medijski sadržaji, kulturna baština,
društvene mreže, jezik i komunikacija.

Tu definiciju treba proširiti: podatkovna znanost nije samo skup alata nego
**praksa pretvaranja podataka u znanje**. Zato se na kraju svake analize
postavlja isto pitanje — što ovi brojevi i tekstovi govore o kulturi
iz koje su nastali? Bez tog koraka analiza ostaje popis, a ne rezultat.

Ovo je interdisciplinarno polje na sjecištu:

- **digitalne humanistike** (primjena računalnih metoda u humanistici)
- **društvenih znanosti** (ankete, statističke metode)
- **računalne znanosti** (programiranje, obrada podataka)
- **umjetne inteligencije** (veliki jezični modeli, strojno učenje)

Smjer odnosa treba zapamtiti: podatkovna znanost **ne zamjenjuje**
humanističku interpretaciju, nego je **proširuje**. Gdje je tradicionalni
istraživač pročitao desetak romana, podatkovno usmjeren istraživač pregledava
deset tisuća — ali podatak ne govori ništa bez teorije koja postavlja pitanje
i interpretacije koja rezultat pretvara u znanje. 
Svi ti primjeri imaju istu strukturu: **pitanje → podaci → analiza → interpretacija**.

Od popisa zapisa do prve mjere put je vrlo kratak:

```python
# Kulturni podaci kao tablica: zapisi kataloga
import pandas as pd

katalog = pd.DataFrame({
    "id": ["M-0001", "M-0002", "M-0003"],
    "naziv": ["Portret ribara", "Riječki prolaz", "Bez naslova"],
    "godina": [1920, 1934, 1928],
    "zbirka": ["Moderna", "Moderna", "Grafika"],
})

print(katalog.head())
print(katalog["godina"].mean())
```

## AI revolucija u humanistici

Data science u kulturi više nije samo statistika i tablice. Do 2022. analiza
teksta uglavnom je značila frekvencije, tokenizaciju i klasično strojno
učenje. Pojava široko dostupnih velikih jezičnih modela (GPT, Gemini, Llama,
Claude) promijenila je pravila igre: model koji razumije i generira prirodni
jezik dostupan je svakome s preglednikom. Suvremeni istraživač zato koristi
**cijeli AI stack**:

| Tradicionalno | Suvremeno (AI-first) |
|---------------|---------------------|
| Ručno kodiranje varijabli | Automatsko označavanje LLM-om |
| Pretraga po ključnim riječima | Semantička pretraga (embedding) |
| Statički izvještaj | Interaktivni RAG asistent |
| Analiza odvojeno od interpretacije | Agent koji analizira I interpretira |
| Jedan format podataka | Multimodalno (tekst, slika, govor) |

Važno je vidjeti i što se **nije** promijenilo: istraživačko pitanje,
teorijski okvir, kritička provjera i etička odgovornost ostaju na istraživaču.
Knjiga kolegija
*Komunikacija u doba umjetne inteligencije* (Perak 2025) zato veliki jezični
model opisuje kao **komunikacijskog agenta**: entitet koji sudjeluje u
komunikaciji s ciljem razumijevanja i izvršavanja namjere izražene jezikom.
Praktična posljedica: kada modelu kažemo "označi temu u ovim recenzijama", model ne traži nego **izvršava zadatak** — a naš je posao
provjeriti je li izvršio ono što smo mislili.

## Znanost o znanosti

Kolegij počiva na razumijevanju **znanosti o znanosti** (science of science):
proučavanju toga kako znanost funkcionira — kako nastaju pitanja, kako se
gradi dokaz, kako se rezultati provjeravaju i komuniciraju.

- Kako se planira i provodi znanstveno istraživanje?
- Koje su faze istraživačkog procesa?
- Kako se postavlja istraživačko pitanje i hipoteza?
- Kako se bira metoda obzirom na vrstu podataka?
- Kako se prezentiraju rezultati?

U humanistici je proces fleksibilniji nego u eksperimentalnim znanostima:
pitanje se često preoblikuje tijekom analize, a interpretacija je uvijek
teorijski opterećena. Zajednička svim znanostima ostaje **disciplina
procesa**: dokumentirani koraci, provjerljivost i ponovljivost. Dvije su
vrijednosti pritom nezaobilazne:

- **Ponovljivost (reproducibility)** — drugi istraživač mora s istim
  podacima i kodom dobiti iste rezultate.
- **Otvorenost (open science)** — podaci, kod i metode dostupni su javnosti
  kad god je to etički i pravno moguće.

Zato su skripte i bilježnice kolegija u javnom repozitoriju: kod je
istovremeno alat i dokumentacija postupka. Ni negativan rezultat nije
neuspjeh: znanost napreduje i kroz opovrgavanje pretpostavki.

## Istraživački proces

1. **Istraživačko pitanje** — što želim saznati?
2. **Pregled literature** — što se već zna?
3. **Hipoteza** — što pretpostavljam?
4. **Dizajn istraživanja** — koja metoda odgovara pitanju?
5. **Prikupljanje podataka** — anketa, korpus, API, arhiv
6. **Analiza** — statistička, algoritamska, LLM
7. **Interpretacija** — što rezultati znače?
8. **Izvješće** — kako prezentirati rezultate?

Svaki korak ostavlja konkretan artefakt: iz pitanja nastaje provjerljiva
rečenica, iz dizajna nacrt instrumenta, iz prikupljanja sirovi podaci, a iz
analize skripta. Dobro je pitanje
**specifično**, **istraživo** i **relevantno**. Umjesto "Kakvi su mladi
danas?" bolje je pitati: "Kako vrijeme provedeno na TikToku korelira s
percepcijom brzine vremena?" Iz drugog pitanja proizlaze dvije mjerljive
varijable, hipoteza koju podaci mogu opovrgnuti i jasan plan dizajna.

## Ishodi učenja (1-2)

- Opisati osnovne teorijske postavke znanosti o znanosti i procese planiranja
  znanstvenog istraživanja u društveno-humanističkim znanostima.
- Razumjeti teorijske pretpostavke kulturološki usmjerenih metoda data-science.

## Ključni pojmovi

| Pojam | Značenje u jednoj rečenici |
|-------|----------------------------|
| Podatkovna znanost | Praksa pretvaranja podataka u znanje: od prikupljanja do interpretacije. |
| Digitalna humanistika | Primjena računalnih metoda na humanistička pitanja i tekstove. |
| Kulturni podaci | Podaci o kulturnim praksama, baštini, medijima i jeziku. |
| AI-stack | Niz AI metoda (LLM, embedding, RAG, agenti) uz klasične metode. |
| Komunikacijski agent | Model koji razumije i izvršava namjeru izraženu prirodnim jezikom. |
| Znanost o znanosti | Proučavanje toga kako znanost funkcionira i kako nastaju dokazi. |
| Istraživačko pitanje | Provjerljiva rečenica koja određuje na što istraživanje odgovara. |
| Hipoteza | Provjerljiva pretpostavka o odnosu dviju varijabli. |
| Ponovljivost | Druga osoba s istim podacima i kodom dobiva iste rezultate. |
| Otvorena znanost | Podaci, kod i metode javno su dostupni kad je to moguće. |

## Provjeri razumiješ

1. Čime se bavi podatkovna znanost u kulturi i po čemu se razlikuje od klasične humanističke interpretacije?
2. Navedi tri discipline koje se sijeku u ovom polju i objasni što svaka donosi.
3. Što znači da je istraživačko pitanje specifično, istraživo i relevantno?
4. Zašto je ponovljivost važna i što u ovom kolegiju omogućuje provjeru postupka?

<details><summary>Odgovori</summary>

1. Primjenjuje metode podatkovne znanosti na kulturne fenomene (prakse, medije, baštinu, jezik). Interpretaciju ne zamjenjuje, nego proširuje: omogućuje rad na mnogo većem
broju jedinica, dok tumačenje ostaje ljudski posao.
2. Digitalna humanistika (istraživačka pitanja o kulturi i jeziku), društvene znanosti (ankete i statistika) i računalne znanosti (programiranje i obrada podataka); uz njih umjetna inteligencija (LLM, embedding, agenti).
3. Specifično znači suženo na jasan fenomen i populaciju, istraživo da se na njega može odgovoriti podacima, a relevantno da je znanstveno ili društveno važno.
4. Ponovljivost omogućuje da drugi istraživač provjeri nalaz, pa je kod u javnom
repozitoriju ujedno dokumentacija analize.

</details>

## Praktično

- 🟢 Odaberite kulturni fenomen i napišite istraživačko pitanje koje je
  specifično, istraživo i relevantno. Pitanje mora stati u jednu rečenicu.
- 🟢 Nabrojite pet vrsta podataka koje biste za svoju temu mogli prikupiti i
  označite koje su kvantitativne, a koje kvalitativne.
- 🟡 Napišite hipotezu u obliku "X korelira s Y", imenujte neovisnu i zavisnu
  varijablu te dodajte kako biste svaku izmjerili.
- 🟡 Ispunite tablicu od osam koraka za svoju temu tako da u svaki korak
  upišete očekivani artefakt (npr. "anketa s 12 pitanja"). Tablicu predajte
  kao pripremu za projekt.
- 🏆 Neka vam LLM predloži pet referenci za vaše pitanje. Provjerite svaku na
  primarnom izvoru (Google Scholar, CROSBI, ARCA) i zapišite koliko ih je
  točno, a koliko halucinirano.

## Dalje

U [cjelini 02](02_podaci_fair_ai.md) prelazimo s pitanja na materijal: koje
vrste podataka postoje u kulturi, kako se prikupljaju, kako se procjenjuje
njihova pouzdanost i kako ih pripremiti da budu pronađivi, dostupni i
upotrebljivi — ljudima i strojevima.

## Literatura

- Grus, J. (2019). *Data Science from Scratch*. O'Reilly. (1. poglavlje)
- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije*. FFRI Rijeka.
  https://github.com/bperak/komunikacija_u_doba_ai
