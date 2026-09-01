# Poglavlje 1: Uvod u data science u kulturi

**Data Science u kulturi: metode, podaci i umjetna inteligencija u digitalnoj humanistici**

---

## Sažetak poglavlja

U ovom poglavlju upoznajemo podatkovnu znanost kao pristup istraživanju
kulturnih fenomena. Polazimo od pitanja što je uopće "data science u kulturi",
kako je nastao na sjecištu digitalne humanistike, društvenih znanosti i
računalne znanosti, te zašto je umjetna inteligencija — posebice veliki
jezični modeli — promijenila pravila igre. Uvodimo i znanost o znanosti:
kako se gradi znanstveno istraživanje od pitanja do izvješća. Poglavlje
zatvaramo mapom knjige koja čitatelja vodi od temelja preko metoda do
suvremenoga AI-stoga (LLM, embedding, RAG, agenti) i etičke refleksije.

---

## 1.1 Što je data science u kulturi?

Podatkovna znanost (engl. *data science*) često se definira kao
"znanost o podacima" — ali ta definicija kruži oko praznine. Bolje je
reći da je podatkovna znanost **praksa pretvaranja podataka u znanje**:
prikupljanje, čišćenje, analiza, vizualizacija i interpretacija podataka
s ciljem odgovora na istraživačka pitanja.

Kada se ta praksa primijeni na **kulturne fenomene** — kulturne prakse,
medijske sadržaje, kulturnu baštinu, jezik, umjetnost, društvene mreže —
govorimo o podatkovnoj znanosti u kulturi (engl. *cultural data science*)
ili, šire, o **digitalnoj humanistici** (*digital humanities*).

Podatkovna znanost u kulturi nije jedna disciplina nego **sjecište**:

| Polje | Doprinos |
|-------|----------|
| Digitalna humanistika | Istraživačka pitanja o kulturi, baštini, jeziku |
| Društvene znanosti | Metode: ankete, statistika, kvalitativna analiza |
| Računalna znanost | Alati: programiranje, obrada podataka, strojno učenje |
| Umjetna inteligencija | Veliki jezični modeli, semantička pretraga, agenti |
| Znanost o informacijama | Klasifikacija, metapodaci, repozitoriji |

Ključno je shvatiti da podatkovna znanost u kulturi **ne zamjenjuje**
humanističku interpretaciju — ona je **produžetak** istraživačkih mogućnosti.
Tamo gdje je tradicionalni humanist čitao desetak romana, podatkovno
usmjeren istraživač može analizirati deset tisuća. No podatak sam po sebi
ne govori: potrebna je teorija koja će postaviti pitanja i interpretacija
koja će rezultate pretvoriti u znanje.

> **Teorijski okvir — digitalna humanistika.**
> Gold i Klein (2016) opisuju digitalnu humanistiku kao polje koje
> "pregovara" o tome što znači raditi humanistiku s računalima. Dva su
> stajališta: prvo, računala kao *alat* koji ubrzava postojeće metode;
> drugo, računala kao *medij* koji mijenja sama pitanja koja možemo postaviti.
> Ova knjiga zauzima treće, suvremeno stajalište: AI modeli nisu ni alat ni
> medij nego **komunikacijski partneri** — sučelja koja razumiju namjeru,
> izvršavaju zadatke i razgovaraju o rezultatima (Perak 2025).

### Primjeri podatkovne znanosti u kulturi

- **Analiza društvenih mreža:** kako se govori o kulturi na X-u (bivšem
  Twitteru)? Koje metafore dominiraju u raspravama o muzejima?
- **Digitalizirana baština:** milijuni digitaliziranih knjiga, novina i
  fotografija traže pretragu, klasifikaciju i povezivanje (Europeana,
  Croatian Web Archive).
- **Kulturni konzum:** tko posjećuje kazališta, što sluša, kako se mijenjaju
  glazbene navike s digitalnim platformama?
- **Jezik i kultura:** kako se kroz korpuse otkrivaju kulturalni modeli,
  metafore i ideologije?
- **Muzejska analitika:** koje zbirke privlače pažnju, kako posjetitelji
  prolaze kroz izložbe?

Svaki od ovih primjera ima zajedničku strukturu: **pitanje → podaci →
analiza → interpretacija**. Upravo tu strukturu uči ova knjiga.

---

## 1.2 AI revolucija u humanistici

U posljednjih nekoliko godina podatkovna znanost doživjela je temeljitu
promjenu. Do 2022. godine analiza teksta značila je uglavnom statistiku
frekvencija, tokenizaciju i klasično strojno učenje. Pojava široko
dostupnih velikih jezičnih modela (GPT, Gemini, Llama, Claude) promijenila
je pravila igre: modeli koji razumiju i generiraju prirodni jezik dostupni
su svakome s preglednikom.

Što to znači za podatkovnu znanost u kulturi?

| Tradicionalno | Suvremeno (AI-first) |
|---------------|---------------------|
| Ručno kodiranje varijabli | Automatsko označavanje LLM-om |
| Pretraga po ključnim riječima | Semantička pretraga (embedding) |
| Statički izvještaj | Interaktivni RAG asistent |
| Analiza odvojena od interpretacije | Agent koji analizira i interpretira |
| Jedan format podataka | Multimodalno (tekst, slika, govor) |
| Mjeseci analize | Sati analize uz provjeru |

Važno je naglasiti što se **nije** promijenilo: istraživačko pitanje,
teorijski okvir, kritička provjera i etička odgovornost ostaju u središtu.
AI ubrzava i proširuje analizu, ali ne postavlja pitanja umjesto nas —
barem ne bi trebao.

### Veliki jezični model kao komunikacijski agent

U knjizi *Komunikacija u doba umjetne inteligencije* (Perak 2025) predlaže
se pojam **komunikacijskog agenta** za razumijevanje LLM-ova. Model nije
"tražilica" ni "uredski alat": on je **agencija koja razumije namjeru,
planira i izvršava zadatke izražene prirodnim jezikom**. Kada modelu
kažemo "analiziraj sentiment ovih recenzija i vrati mi JSON", on ne
"traži" — on **izvršava** zadatak.

Ta razlika ima duboke posljedice: LLM-ovi nisu samo alati za pisanje
nego **sučelja prema podacima i alatima**. U ovoj knjizi koristimo ih
upravo tako: za označavanje, ekstrakciju, semantičku pretragu, izgradnju
RAG sustava i agentskih tokova.

> **Definicija — komunikacijski agent** (Perak 2025): entitet (ljudski ili
> strojni) koji sudjeluje u komunikacijskom procesu s ciljem razumijevanja
> i/ili izvršavanja namjere izražene jezikom. U suvremenom kontekstu,
> komunikacijski agenti su umjetni sustavi koji kombiniraju LLM s alatima
> i petljom planiranja.

---

## 1.3 Znanost o znanosti: kako se gradi istraživanje

Podatkovna znanost u kulturi je **znanost** — i kao takva počiva na
razumijevanju onoga što se naziva *znanošću o znanosti* (engl. *science of
science*): proučavanju toga kako znanost funkcionira, kako se postavljaju
pitanja, kako se gradi dokaz, kako se komuniciraju rezultati.

### Znanstvena metoda u humanistici

Tradicionalna shema znanstvene metode:

1. **Opažanje** — uočavamo fenomen (npr. "mladi sve više vremena provode na TikToku")
2. **Pitanje** — što želimo razumjeti? (npr. "kako TikTok oblikuje percepciju vremena?")
3. **Hipoteza** — provjerljiva pretpostavka ("korištenje TikToka korelira s
   percepcijom ubrzanog vremena")
4. **Dizajn** — kojom metodom testiramo? (anketa, analiza sadržaja, korpus)
5. **Prikupljanje podataka** — sustavno, dokumentirano, etički
6. **Analiza** — statistička, algoritamska, AI-potpomognuta
7. **Interpretacija** — što rezultati znače, koja su ograničenja
8. **Komunikacija** — izvješće, članak, prezentacija; podaci i kod otvoreni

U humanistici shema je fleksibilnija: istraživačko pitanje često se
preoblikuje tijekom analize, a interpretacija je uvijed teorijski
opterećena. No **disciplina procesa** — dokumentiranje koraka, provjerljivost,
ponovljivost — zajednička je svim znanostima i upravo je ona ono što
podatkovna znanost dodaje humanistici.

### Ponovljivost i otvorenost

Dvije su vrijednosti danas nezaobilazne:

- **Ponovljivost (reproducibility):** drugi istraživač mora moći ponoviti
  analizu s istim podacima i kodom te dobiti iste rezultate.
- **Otvorenost (open science):** podaci, kod i metode otvoreni javnosti
  (kad god je to etički i pravno moguće).

Ova knjiga promiče obje: svi primjeri koda nalaze se u javnom repozitoriju,
a vježbe pozivaju na dokumentiranje svakog koraka.

---

## 1.4 Istraživački proces u 8 koraka — praktikum

Ovdje istraživački proces prenosimo u praktični obrazac koji ćemo koristiti
kroz cijelu knjigu i u projektnom radu.

### Korak 1: Istraživačko pitanje

Dobro pitanje je:
- **specifično** ("kako društvene mreže utječu na body image mladih"
  umjesto "kakvi su mladi danas")
- **istraživo** (može se odgovoriti podacima)
- **relevantno** (društveno ili znanstveno važno)

### Korak 2: Pregled literature

Što se već zna? Koji okviri postoje? Pretraživanje: Google Scholar, CROSBI,
Scopus, ARCA (repozitorij FFRI-ja), Europeana.

### Korak 3: Hipoteza / istraživačka pitanja

Npr.:
- "Studenti koji više koriste društvene mreže izvještavaju o nižem samopouzdanju."
- "Postoji li korelacija između vremena na TikToku i percepcije vremena?"

### Korak 4: Dizajn

- **Instrument:** anketa (Google Forms), analiza korpusa, intervju, eksperiment
- **Uzorak:** tko, koliko, kako biramo
- **Etika:** informirani pristanak, anonimnost

### Korak 5: Prikupljanje

Dokumentirati: kada, gdje, kako, koliko ispitanika, koja pitanja.

### Korak 6: Analiza

Čišćenje → deskriptivna statistika → vizualizacija → (LLM analiza
otvorenih odgovora) → korelacije/testovi.

### Korak 7: Interpretacija

Što rezultati znače? Koja su ograničenja (uzorak, instrument, pristranost)?

### Korak 8: Komunikacija

Seminarski rad, izvješće, prezentacija, objava podataka i koda.

> **Rubrika "Što ako ne radi?"**
> Ako rezultati ne potvrde hipotezu, to nije neuspjeh — to je rezultat.
> Znanost napreduje i kroz falsifikaciju (Popper). Dokumentirajte što ste
> naučili i kako biste drugačije dizajnirali istraživanje.

---

## 1.5 Mapa knjige

Ova knjiga organizirana je u četiri dijela:

**Dio I — Temelji (pogl. 1-3):** Uvod u podatkovnu znanost u kulturi,
vrste podataka i FAIR principi, Python i Google Colab.

**Dio II — Metode (pogl. 4-7):** Tablični podaci (Pandas), statistika,
vizualizacija, obrada teksta (NLP).

**Dio III — Umjetna inteligencija (pogl. 8-11):** Veliki jezični modeli,
embedding i semantička pretraga, RAG, agentski sustavi. Ovo je jezgra
knjige — suvremeni AI-stog za kulturu.

**Dio IV — Praksa i etika (pogl. 12-14):** Projektno istraživanje od A do Ž,
etika i akademska čestitost, zaključak.

Svako poglavlje ima istu strukturu:

1. **Sažetak poglavlja**
2. **Teorijski okvir** (udžbenička komponenta)
3. **Metode** (kako se što radi)
4. **Praktikum** (kod, primjeri, korak-po-korak)
5. **Vježbe** (🟢 osnovne / 🟡 srednje / 🏆 napredne)
6. **Sažetak i ključni pojmovi**
7. **Literatura**

---

## Vježbe

### 🟢 Osnovna
1. Odaberite kulturni fenomen koji vas zanima (npr. "posjećenost muzeja",
   "glazbene navike", "jezik influencera"). Napišite istraživačko pitanje
   prema kriterijima iz odjeljka 1.4 (specifično, istraživo, relevantno).
2. Pretražite Google Scholar ili CROSBI za svoje pitanje i pronađite
   dva znanstvena rada. Zapišite citate u formatu APA 7.

### 🟡 Srednja
3. Za svoje istraživačko pitanje napišite hipotezu u obliku
   "što korelira sa čim" ili "kako X utječe na Y".
4. Nacrtajte dizajn: koja metoda (anketa/korpus), koji uzorak, koja pitanja?

### 🏆 Napredna
5. Pomoću LLM-a (npr. Gemini) generirajte pregled literature za svoje
   pitanje. Zatim **provjerite svaki citat** na primarnom izvoru. Zapišite
   koliko je citata bilo točno, a koliko halucinirano — i što to govori
   o korištenju LLM-a u znanosti.

---

## Sažetak i ključni pojmovi

- Podatkovna znanost u kulturi = pretvaranje kulturnih podataka u znanje.
- Digitalna humanistika: računala kao alat, medij ili komunikacijski partner.
- AI revolucija: od frekvencija do LLM-ova, embeddinga, RAG-a i agenata.
- Znanost o znanosti: pitanje → hipoteza → dizajn → podaci → analiza →
  interpretacija → komunikacija.
- Ponovljivost i otvorenost su temeljne vrijednosti.
- LLM kao komunikacijski agent (Perak 2025).

**Ključni pojmovi:** podatkovna znanost, digitalna humanistika, kulturni
podaci, AI-stog, komunikacijski agent, znanstvena metoda, ponovljivost,
otvorena znanost.

---

## Literatura

- Gold, M. K., & Klein, L. F. (ur.). (2016). *Debates in the Digital Humanities*. University of Minnesota Press.
- Grus, J. (2019). *Data Science from Scratch: First Principles with Python* (2. izd.). O'Reilly.
- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije: Razvoj velikih jezičnih modela i komunikacijskih agenata*. Filozofski fakultet u Rijeci.
- Popper, K. (2005). *Logika znanstvenog otkrića*. Jesenski i Turk.
- Shneiderman, B. (2016). *The New ABCs of Research*. Oxford University Press.
