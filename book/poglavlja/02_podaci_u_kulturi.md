# Poglavlje 2: Podaci u kulturi

---

## Sažetak poglavlja

Podaci su sirovina podatkovne znanosti — ali u kulturi podaci imaju
poseban status: oni su **uvijek već interpretirani**, proizvedeni ljudima
u društvenim kontekstima. Ovo poglavlje uvodi vrste podataka u kulturnim
istraživanjima, problem pouzdanosti i uzoraka, FAIR principe upravljanja
podacima, metapodatke i pojam **AI-spremnih podataka** — ključan za
suvremeni rad s velikim jezičnim modelima i agentima.

---

## 2.1 Vrste podataka u kulturi

Podatke u kulturi možemo razvrstati na više načina. Najkorisnija
podjela za naše potrebe polazi od **prirode mjerenja** i **formata**:

### Prema prirodi

| Vrsta | Opis | Primjeri u kulturi | Analiza |
|-------|------|--------------------|---------|
| **Kvantitativni** | Numerički, mjerljivi | Broj posjetitelja, ocjene 1-5, frekvencije | Statistika, korelacije |
| **Kvalitativni** | Opisni, značenjski | Intervjui, otvorena pitanja, tekstovi | NLP, tematska analiza |
| **Kategorijski** | Nominalni/ordinalni | Žanr, zbirka, dobna skupina | Frekvencije, hi-kvadrat |
| **Vremenski nizovi** | Vrijednosti kroz vrijeme | Posjećenost po mjesecima | Trendovi, sezonalnost |
| **Prostorni** | Geografske lokacije | Lokacije kulturnih ustanova | Mape, prostorna analiza |
| **Mrežni** | Veze među entitetima | Suradnje, citiranja, mreže sljedbenika | Analiza mreža (SNA) |
| **Multimodalni** | Više medija | Slike, video, zvuk, govor | Računalni vid, STT, audio analiza |

### Prema izvoru

- **Primarni podaci** — prikupljeni za vaše istraživanje (anketa, intervju)
- **Sekundarni podaci** — postoje, netko ih je prikupio (popis, katalog, korpus)
- **Digitalni tragovi** (*digital traces*) — podaci nastali kao nusprodukt
  upotrebe digitalnih platformi (lajkovi, pregledi, komentari)

> **Teorijski okvir — podatak kao konstrukt.**
> U humanistici podaci nisu "sirovi" nego **uvijek već oblikovani**:
> katalog muzeja odražava odluke kustosa, anketa odražava konstrukt
> istraživača, korpus odražava odabir urednika. Kao što kaže Bowker
> (2000), podaci su "očišćena" verzija stvarnosti — a svako čišćenje
> uključuje odluke. Zato je dokumentiranje podrijetla podataka
> (provenancija) sastavni dio analize.

---

## 2.2 Pouzdanost, uzorci i pristranost

### Populacija i uzorak

- **Populacija** — sve jedinke koje želimo opisati (npr. svi studenti FFRI-ja)
- **Uzorak** — dio populacije koji stvarno analiziramo (npr. 40 studenata
  koji su ispunili anketu)

Cilj je da uzorak **reprezentira** populaciju. Ako je uzorak pristran,
zaključci se ne mogu generalizirati.

### Vrste uzorkovanja

| Vrsta | Opis | Prednost | Rizik |
|-------|------|----------|-------|
| Prigodni (convenience) | Tko je dostupan | Brz, jeftin | Jaka pristranost |
| Kvotni | Proporcionalno po grupama | Bolja reprezentacija | Ne nasumičan |
| Nasumični (random) | Slučajni odabir | Generalizacija | Teško u praksi |
| Lančani (snowball) | Ispitanici preporučuju | Pristup teškim grupama | Slični ispitanici |

> **Primjer pristranosti:** anketa o "mladima" provedena isključivo na
> vlastitom studiju ne opisuje mlade općenito — opisuje studente toga
> studija. U izvješću to mora biti jasno rečeno.

### Pouzdanost i valjanost

- **Pouzdanost (reliability):** instrument daje stabilne rezultate
  (ista osoba dva puta → sličan odgovor)
- **Valjanost (validity):** instrument mjeri ono što tvrdimo da mjeri
  (pitanje "koliko često idete u kino" mjeri ponašanje, ne stav)

> **Rubrika "Što ako ne radi?"**
> Ako vam svi odgovori na Likertovoj skali izgledaju isti (npr. sve 3),
> provjerite: (a) jesu li pitanja jasna, (b) je li skala ujednačena,
> (c) nije li došlo do *response seta* — mehaničkog označavanja.
> Pilotska anketa (5-10 ispitanika) prije glavne spašava puno muke.

---

## 2.3 FAIR principi upravljanja podacima

FAIR principi (Wilkinson et al. 2016) definiraju kako podaci trebaju biti
organizirani da bi bili upotrebljivi ljudima i strojevima:

### F — Findable (pronalazivi)
- Podaci imaju jedinstveni i trajni identifikator (DOI, URN)
- Bogati metapodaci
- Indeksirani u pretraživim repozitorijima

### A — Accessible (dostupni)
- Dohvatljivi preko standardiziranog protokola (HTTP, API)
- Jasna pravila pristupa (otvoreno / uz uvjete)

### I — Interoperable (interoperabilni)
- Standardni formati (CSV, JSON, JSON-LD, XML/TEI)
- Kontrolirani rječnici (LCSH, UDC, Wikidata)

### R — Reusable (ponovno upotrebljivi)
- Jasna licenca (CC-BY, CC0...)
- Dokumentacija (data dictionary, README)
- Podrijetlo (provenance)

> **Zašto FAIR za humaniste?** Kultura je područje golemih zbirki koje
> prikupljaju ustanove (arhivi, knjižnice, muzeji) desetljećima. Bez FAIR
> načela, te zbirke ostaju "digitalne gomile" — s FAIR načelima postaju
> **podatkovna infrastruktura** koju istraživači i AI sustavi mogu koristiti.
> Europske inicijative (Europeana, DARIAH-EU, CLARIN) grade upravo takvu
> infrastrukturu.

---

## 2.4 Metapodaci: podaci o podacima

**Metapodaci** opisuju podatke: tko ih je stvorio, kada, što znače, kojeg
su formata. U kulturi su metapodaci često **vrijedniji od samog sadržaja**
— bez njih digitalizirana slika u arhivu je samo "slika".

### Struktura metapodataka (primjer muzejskog zapisa)

```json
{
  "id": "M-0001",
  "naziv": "Portret ribara",
  "autor": "Kralj",
  "godina": 1920,
  "materijal": "ulje/platno",
  "dimenzije_cm": 80,
  "zbirka": "Moderna",
  "lokacija": "Moderna galerija",
  "licenca": "CC-BY-SA",
  "opis": "Portret starijeg muškarca s mrežama..."
}
```

### Standardi metapodataka u kulturi

- **Dublin Core** — 15 osnovnih polja (naslov, autor, datum, tip...)
- **TEI (Text Encoding Initiative)** — označavanje tekstova
- **CIDOC-CRM** — ontologija za muzejsku baštinu
- **Schema.org / JSON-LD** — strukturirani podaci za web
- **IIIF** — interoperabilnost digitalnih slika

> **Metapodaci i LLM-ovi.** Za velike jezične modele metapodaci su ključni:
> RAG sustav koji odgovara o zbirci zapravo pretražuje metapodatke.
> Dobar metapodatak = dobar AI asistent; loš metapodatak = halucinacije.

---

## 2.5 AI-spremni podaci

**AI-spremni podaci** (engl. *AI-ready data*) su podaci organizirani tako
da ih veliki jezični modeli, embedding modeli i agenti mogu izravno koristiti.
Šest zahtjeva:

1. **Čistoća** — bez duplikata, konzistentne vrijednosti, bez tipfelera
2. **Strukturiranost** — CSV/JSON umjesto PDF-a i skeniranih tablica
3. **Označenost** — jasna imena polja, kontrolirane kategorije
4. **Dokumentiranost** — data dictionary, README, primjeri
5. **Dovoljnost konteksta** — svaki zapis nosi kontekst (što, gdje, kada)
6. **Licenciranje** — jasno dopuštenje za strojnu obradu

### Primjer: od ne-urednog do AI-spremnog

**Prije (loše):**
```
Autor: Kralj | Nasl: Portret ribara | 1920 | 80x65
Autor: kralj | Portret ribara, 1920, 80 x 65 cm
```
Nedosljedna imena, miješani formati, bez ID-a.

**Poslije (AI-spremno):**
```json
[{"id": "M-0001", "autor": "Kralj", "naziv": "Portret ribara", "godina": 1920, "dimenzije_cm": 80}]
```

### Provjera kvalitete (praktikum)

```python
import pandas as pd

katalog = pd.DataFrame({...})   # učitaj katalog
print(katalog.isnull().sum())   # null vrijednosti
print(katalog.duplicated().sum())  # duplikati
print(katalog["autor"].value_counts().head())  # konzistentnost
```

> **AI-spremnost kao kompetencija.** U digitalnoj humanistici sposobnost
> pripreme podataka za AI sustave postaje jednako važna kao sposobnost
> njihove analize. Muzeji i arhivi traže upravo takve profile.

---

## 2.6 Javni resursi i repozitoriji

Za kulturna istraživanja danas su dostupni brojni otvoreni izvori:

### Europska i nacionalna infrastruktura

| Resurs | Što sadrži | URL |
|--------|-----------|-----|
| **Europeana** | Milijuni digitaliziranih kulturnih dobara EU | europeana.eu |
| **Croatian Web Archive (HAW)** | Arhiv hrvatskog weba | haw.nsk.hr |
| **DARIAH-EU** | Digitalna istraživačka infrastruktura | dariah.eu |
| **CLARIN** | Jezični resursi i alati | clarin.eu |
| **CROSBI / CroRIS** | Hrvatska znanstvena bibliografija | croris.hr |
| **Wikidata / Wikipedia** | Strukturirano znanje, API | wikidata.org |
| **Voyant Tools** | Analiza teksta u pregledniku | voyant-tools.org |
| **Sketch Engine** | Korpusna analiza | ske.fi |

### API-ji za kulturu

- **Wikipedia API** — članci, povijest, kategorije
- **Europeana API** — pretraga zbirki
- **Open Library API** — knjižni katalozi
- **YouTube Data API** — video sadržaji i komentari
- **X API** — društveni sadržaj (uz uvjete)

> **Praktična napomena.** API-ji često zahtijevaju ključ (API key) i
> poštovanje limita. Uvijek provjerite uvjete korištenja i citirajte izvor.

---

## Vježbe

### 🟢 Osnovna
1. U Google Forms napravite anketu od 10 pitanja o kulturnim navikama
   (5 zatvorenih + 3 Likert + 2 otvorena). Ispunite je s 5-10 ispitanika.
2. Izvezite odgovore u CSV i pregledajte strukturu: koliko stupaca, koji tipovi?

### 🟡 Srednja
3. Pronađite na Europeani ili Haw-u 20 zapisa o jednoj temi (npr. "Rijeka").
   Izvezite metapodatke i procijenite FAIR-ost: imaju li ID, licencu, opis?
4. Očistite svoj anketni CSV: duplikati, null vrijednosti, konzistentnost
   kategorija. Dokumentirajte svaku promjenu u README.

### 🏆 Napredna
5. Izgradite mali JSON-LD "AI-spremni" opis svoje zbirke (10 zapisa) prema
   Dublin Core poljima. Zatim ga dajte LLM-u (Gemini) i pitajte tri pitanja
   o zbirci. Provjerite točnost odgovora.

---

## Sažetak i ključni pojmovi

- Podaci u kulturi su viševrsni: kvantitativni, kvalitativni, mrežni, multimodalni.
- Podaci su uvijek već interpretirani — dokumentiranje podrijetla je nužno.
- Uzorak mora reprezentirati populaciju; pristranost se priznaje, ne skriva.
- FAIR: Findable, Accessible, Interoperable, Reusable.
- Metapodaci opisuju podatke; u kulturi su često ključni.
- AI-spremni podaci: čisti, strukturirani, označeni, dokumentirani, licencirani.
- Javna infrastruktura: Europeana, HAW, DARIAH, CLARIN, CROSBI, Wikidata.

**Ključni pojmovi:** populacija, uzorak, pouzdanost, valjanost, FAIR,
metapodaci, Dublin Core, TEI, AI-ready data, provenancija.

---

## Literatura

- Bowker, G. C. (2000). Biodiversity datadiversity. *Social Studies of Science*, 30(5), 643-683.
- Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, 160018.
- Grus, J. (2019). *Data Science from Scratch* (2. izd.). O'Reilly. (pogl. 3-5)
- DARIAH-EU: https://dariah.eu | CLARIN: https://clarin.eu | Europeana: https://europeana.eu
