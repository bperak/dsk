# Upute za projekt — Data Science u kulturi 2026./2027.

**Vrijednost:** 70 bodova (kontinuirana provjera znanja 2, svi ishodi DSK-1 … DSK-8)
**Ishod:** seminarski rad + prezentacija + analiza u Colabu

## Cilj projekta

Projektno istraživanje u kojem svaki student:

1. definira temu (Domena / Problem / Cilj),
2. izrađuje anketu (Google Forms),
3. prikuplja i analizira podatke (Colab + Pandas),
4. piše seminarski rad i prezentira rezultate.

Projekt nije „zadatak iz statistike" — to je malo istraživanje u kojem moraš moći reći **što si htio saznati, kako si to mjerio, što si dobio i gdje su granice tvojih nalaza**.

---

## Faze projekta

### Faza 1: Definicija teme (rok: 2. tjedan nastave)

- Upisuje se u Google Sheet kolegija (kolona **Definicija teme**)
- Format: **Domena / Problem / Cilj** (vidi [`PRIJEDLOG_TEMPLATE.md`](PRIJEDLOG_TEMPLATE.md))
- Primjeri iz prethodnih godina: [`PRIMJERI_IZ_PROSLIH_GODINA.md`](PRIMJERI_IZ_PROSLIH_GODINA.md)

Provjera kvalitete teme — tri pitanja koja moraš moći odgovoriti u jednoj rečenici:

| Pitanje | Loše | Dobro |
|---|---|---|
| Što proučavam? | „društvene mreže" | „utjecaj društvenih mreža na sliku o vlastitom tijelu kod studentica" |
| Zašto je to važno? | „zato što je zanimljivo" | „zato što se o posljedicama mnogo govori, a malo mjeri na lokalnoj populaciji" |
| Što ću doznati? | „saznat ću mišljenja" | „koliki se dio ispitanika izjašnjava kao nezadovoljan, i razlikuje li se to po dobi" |

### Faza 2: Anketa (Google Forms)

- Minimalno 10 pitanja
- Mješavina: demografija (dob, spol), stavovi (Likert skala 1–5), ponašanje (frekvencije), otvorena pitanja
- Ciljana publika: minimalno 20 ispitanika
- Link na anketu unosi se u Google Sheet (kolona **ANKETA**)

Što pomaže pri izradi ankete:

- svako pitanje treba imati **svrhu povezanu s ciljem** — ako odgovor ne možeš upotrijebiti u raspravi, pitanje je suvišno;
- kod pitanja s više odgovora jasno napiši uputu („odaberite najmanje dva") i **koristi kvačice, ne slobodan tekst**;
- kod stavova koristi skalu 1–5 i napiši što znači 1, a što 5;
- otvorena pitanja: jedno ili dva, i to ona na koja se odgovor ne može ponuditi;
- **ne prikupljaj imena ni adrese** — anonimnost je dio metode i olakšava iskrene odgovore;
- probaj anketu na dvoje ljudi prije nego je pustiš dalje.

> **Poveži odgovore s tablicom odmah** (*Responses → Link to Sheets*) — tako podaci ne mogu nestati, a kasnije samo objaviš tablicu kao CSV i bilježnica ih sama povuče.

### Faza 3: Analiza u Colabu

- Učitavanje odgovora (objavljena tablica kao CSV ili izvoz iz Google Formsa)
- Čišćenje podataka (Pandas)
- Deskriptivna statistika
- Vizualizacija (Matplotlib/Seaborn)
- (Opcionalno) LLM analiza otvorenih odgovora

Predložak za rad: [**analiza upitnika — jednostavna verzija**](https://colab.research.google.com/github/bperak/dsk/blob/main/colab/DSK_analiza_upitnika_jednostavno.ipynb).

Postupak u šest poteza:

1. **File → Save a copy in Drive** (radiš u svojoj kopiji).
2. U prvom koraku upiši poveznicu svoje objavljene tablice.
3. U trećem koraku prilagodi ključne riječi svojim pitanjima i provjeri ispis — mora prepoznati sve stupce.
4. Pokreni *Run all*.
5. Pogledaj brojke i slike; sve što ne razumiješ, provjeri u cjelinama [04](../content/04_pandas_tablice.md), [05](../content/05_statistika.md) i [06](../content/06_vizualizacija.md).
6. Sažetak iz zadnjeg koraka iskoristi kao kostur za poglavlje *Rezultati* — rečenice prepiši svojim riječima i dodaj tumačenje.

Ako želiš i AI sloj (kategorizacija odgovora, semantička sličnost, sažetak koji piše model), koristi [punu verziju bilježnice](https://colab.research.google.com/github/bperak/dsk/blob/main/colab/DSK_analiza_upitnika_Rijeka.ipynb) — i obavezno navedi u metodologiji da si je koristio.

### Faza 4: Seminarski rad

Struktura:

1. **Uvod** — domena, problem, cilj, istraživačka pitanja
2. **Pregled literature** — što se već zna
3. **Metodologija** — uzorak, instrument (anketa), postupak
4. **Rezultati** — tablice, grafovi, ključni nalazi
5. **Rasprava** — interpretacija, ograničenja, buduća istraživanja
6. **Zaključak**
7. **Literatura**

Dodatno, u metodologiji mora stajati **izjava o upotrebi AI alata** (vidi pravila niže): koji alat, za koji dio posla, s kojim zadatkom.

Kontrolna lista prije predaje:

- [ ] uzorak je opisan (koliko ispitanika, kako prikupljen, koja ograničenja)
- [ ] svaki graf ima naslov, označene osi i objašnjenje u tekstu
- [ ] svaka brojka u tekstu postoji u tablici ili na slici
- [ ] prazni odgovori i neobične vrijednosti su spomenuti, ne prešućeni
- [ ] navedena su ograničenja istraživanja (mali uzorak, prigodan uzorak, samoprocjena)
- [ ] literatura je navedena dosljedno (APA 7)
- [ ] izjava o upotrebi AI alata je uključena

### Faza 5: Prezentacija

- Kratko izlaganje (5–10 min)
- Ključni rezultati + vizualizacije
- Odgovori na pitanja

Preporuka: jedna slika koja nosi glavni nalaz, jedna tablica s brojkama i jedna rečenica o ograničenju. Sve ostalo su detalji za pitanja.

---

## Što se gleda pri ocjenjivanju

| Kriterij | Na što se gleda |
|---|---|
| Definirana tema | je li domena uska, problem obrazložen, cilj mjerljiv |
| Instrument (anketa) | jesu li pitanja povezana s ciljem i pravilno oblikovana |
| Prikupljanje i podaci | je li uzorak opisan i je li tablica uredna (bez duplih unosa, s objašnjenim prazninama) |
| Analiza | je li metoda primjerena podacima, jesu li izračuni ispravni i provjerljivi |
| Vizualizacija | čitljivost, poštena skala, oznake i kontekst |
| Kritičnost | jesu li ograničenja prepoznata i je li korelacija tretirana kao korelacija, ne kao uzrok |
| Izvještaj i prezentacija | struktura, jasnoća, dosljednost brojki i navoda |

## Ocjenjivanje

| Aktivnost | ECTS | Max bodova |
|-----------|------|------------|
| Pohađanje nastave | 1,5 | 0 |
| Kontinuirana provjera znanja 1 | 1 | 30 |
| Kontinuirana provjera znanja 2 (projekt) | 2,5 | 70 |
| Završni ispit | 0 | 0 |
| **UKUPNO** | **5** | **100** |

Riječ je o varijanti bez završnog ispita.

---

## AI alati u projektu — pravila

- ✅ Dopušteno: LLM za pomoć pri generiranju anketnih pitanja, čišćenju
  podataka, analizi otvorenih odgovora, interpretaciji rezultata
- ✅ Dopušteno: semantička pretraga, RAG, agenti za analizu
- ⛔ Obavezno: **jasno navesti svaku upotrebu AI alata** (u metodologiji)
- ⛔ Zabranjeno: predstavljanje AI-generiranog teksta kao vlastitog bez navoda
- ⛔ Zabranjeno: izmišljanje podataka (fabriciranje anketnih odgovora)

**Tri provjere koje svatko može napraviti sam:**

1. Svaka brojka u tekstu koju je predložio model mora postojati u tvojoj tablici.
2. Ako model navodi izvor, provjeri da izvor postoji i da u njemu to doista piše.
3. Ako zaključak zvuči previše uredno („dokazano je da…"), provjeri radi li se o korelaciji na malom uzorku.

---

## Prijašnji workflow (za referencu)

| Godina | Proces |
|--------|--------|
| 2021/22 | Link na anketu + Colab analiza + zadani podaci (Covid, Sabor, Spotify) |
| 2022/23 | Colab analiza upitnika + seminarski rad + završni test |
| 2023/24 | DS_Form_1 (9.10.) + Definicija teme (16.10.) + Colab 1 + Colab 2 |
| 2024/25 | Prvi GForms + Seminarski rad preko GFORMS + Definicija teme + prezentacija |
| 2025/26 | ANKETA + Colab za anketu + GFORMS + Definicija teme + prezentacija |

Iz svih godina isti zaključak: **najviše bodova gubi se na nedefiniranoj temi i na neurednim podacima**, a ne na nedostatku naprednih metoda.
