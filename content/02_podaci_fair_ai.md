# 02. Podaci u kulturi: vrste, FAIR principi, AI-spremnost

> **U ovoj cjelini.** Naučit ćete koje vrste podataka postoje u kulturnim istraživanjima, kako se
procjenjuje pouzdanost uzorka te što znače FAIR načela i AI-spremni podaci.
Nakon cjeline moći ćete procijeniti je li zbirka upotrebljiva za analizu.
> **Ishodi:** DSK-3 Prepoznati, pretražiti i koristiti javne data-science alate i podatkovne resurse. DSK-4 Objasniti i primijeniti tehnike dohvaćanja, pripreme i pohrane podataka.
> **Uz ovu cjelinu idu:** skripta [`scripts/01_pandas_osnove.py`](../scripts/01_pandas_osnove.py) i [cjelina 03: Python i Google Colab](03_python_colab.md).

**Kolegij:** Data Science u kulturi | 2026./2027.

## Vrste podataka

Podaci u kulturi nastali su ljudskim odlukama, pa su **uvijek već
interpretirani**: katalog odražava odluke kustosa, anketa konstrukt
istraživača, a korpus odabir urednika. Dokumentiranje podrijetla (provenancija)
zato je dio metode.

| Vrsta | Primjeri u kulturi | Analiza |
|-------|-------------------|---------|
| Kvantitativni | Broj posjetitelja, ocjene, frekvencije | Statistika, korelacije |
| Kvalitativni | Intervjui, otvorena pitanja, tekstovi | NLP, tematska analiza |
| Vremenski nizovi | Posjećenost kroz godine | Trendovi |
| Prostorni | Lokacije kulturnih ustanova | Geografska analiza |
| Mrežni | Suradnje, citiranja, društvene mreže | Analiza mreža |
| Multimodalni | Slike, video, govor | Računalni vid, STT |

Prema izvoru razlikujemo:

- **Primarni podaci** — prikupljeni za ovo istraživanje (anketa, intervju).
- **Sekundarni podaci** — postoje prije istraživanja (katalog, popis, korpus).
- **Digitalni tragovi** (*digital traces*) — nusproizvod platformi: pregledi,
  lajkovi, komentari, recenzije.

Kod digitalnih tragova naslijeđujete tuđe odluke o tome što se mjeri, pa u
izvješću treba navesti što je mjereno, a što nije.

### Vrsta podatka određuje analizu

Nije svaka metoda smislena za svaki podatak — nad kategorijama se računaju
frekvencije, a ne prosjek:

```python
# Vrsta podatka određuje koja je analiza smislena
import pandas as pd

zapis = pd.DataFrame({
    "zbirka": ["Moderna", "Grafika", "Moderna", "Moderna"],
    "posjetitelji": [1200, 340, 980, 1500],
    "datum": pd.to_datetime(
        ["2026-01-15", "2026-02-03", "2026-02-20", "2026-03-11"]
    ),
})

print(zapis.dtypes)
print(zapis["zbirka"].value_counts())
print(zapis["posjetitelji"].mean())
print(zapis["datum"].dt.month.value_counts().sort_index())
```

Ispisi pokazuju tipove stupaca, frekvencije i prosjek.

## Pouzdanost i uzorci

- **Populacija** = sve jedinke koje istražujemo
- **Uzorak** = dio populacije koji analiziramo
- **Reprezentativnost** — uzorak mora odražavati populaciju
- **Pristranost uzorka** — npr. anketa samo među studentima ne opisuje "mlade" općenito

Način odabira ispitanika određuje koliko daleko smijemo generalizirati:
prigodni uzorak je brz, ali pristran; nasumični dopušta generalizaciju, no
teško ga je izvesti.

Treba razlikovati dvije osobine instrumenta:

- **Pouzdanost (reliability)** — instrument daje stabilne rezultate: ista
  osoba dva puta daje sličan odgovor.
- **Valjanost (validity)** — instrument mjeri ono što tvrdimo da mjeri:
  pitanje o čestini odlaska u kino mjeri ponašanje, a ne stav prema kinu.

Ako svi odgovori na ljestvici 1–5 izgledaju jednako, provjerite jesu li
pitanja jasna i nije li nastupio *response set* — mehaničko označavanje istog
broja.

## FAIR principi

Kulturni podaci (katalozi, metapodaci, digitalizirana baština) trebaju biti:

- **F**indable — pronalazivi (metapodaci, perzistentni identifikatori)
- **A**ccessible — dostupni (otvoreni API-ji, licence)
- **I**nteroperable — interoperabilni (standardni formati: CSV, JSON, JSON-LD)
- **R**eusable — ponovno upotrebljivi (dokumentacija, licenciranje)

FAIR načela (Wilkinson i dr. 2016) opisuju kako podatke organizirati da budu
upotrebljivi ljudima i strojevima: trajni identifikator i metapodaci uz svaki
zapis, standardiziran pristup s jasnim pravilima, uobičajen format s
kontroliranim rječnicima te licenca, dokumentacija i podrijetlo. Bez toga
digitalizirane zbirke ostaju "digitalne gomile"; s time postaju **podatkovna
infrastruktura** za istraživače, alate i AI sustave. FAIR pritom ne znači isto što i "otvoreno": podaci mogu biti pronalazivi i uz uvjete pristupa.

## AI-spremni podaci

**AI-spremni podaci** = čisti, označeni, dokumentirani podaci koje LLM ili
agent može direktno koristiti:

- Čistoća: bez duplikata, konzistentne vrijednosti
- Označenost: metapodaci o značenju polja
- Dokumentiranost: data dictionary, README
- Strukturiranost: CSV/JSON umjesto PDF-a
- Licenciranje: jasno za strojnu obradu

Popisu treba dodati i šesti zahtjev — dovoljnost konteksta: svaki zapis mora
nositi podatak o tome što, gdje i kada opisuje, jer model bez konteksta
popunjava praznine pretpostavkama. Nedosljedni zapisi uređivanjem
dobiju isti oblik i jedinstveni ID:

```json
[{"id": "M-0001", "autor": "Kralj", "naziv": "Portret ribara", "godina": 1920, "dimenzije_cm": 80}]
```

Kvalitetu kataloga provjeravamo kodom:

```python
import pandas as pd

katalog = pd.DataFrame({
    "id": ["M-0001", "M-0001", "M-0003"],
    "autor": ["Kralj", "kralj", None],
    "godina": [1920, 1920, 1934],
})

print(katalog.isnull().sum())           # koliko vrijednosti nedostaje po stupcu
print(katalog.duplicated().sum())       # koliko je redaka duplikat
print(katalog["autor"].value_counts())  # nedosljednost: "Kralj" i "kralj"
```

Tri ispisa daju prazne vrijednosti, duplikate i neujednačene nazive.

## Metapodaci

Metapodaci su "podaci o podacima": opisuju tko je zapis stvorio, kada, što
znači i kojeg je formata. U kulturi su često **vrjedniji od samog sadržaja** —
bez metapodataka digitalizirana je slika u arhivu samo slika.

```json
{
  "id": "M-0001",
  "naziv": "Portret ribara",
  "autor": "Kralj",
  "godina": 1920,
  "materijal": "ulje/platno",
  "zbirka": "Moderna",
  "licenca": "CC-BY-SA"
}
```

Dobar metapodatak omogućuje pronalaženje i ponovnu upotrebu. U baštini su uvriježeni standardi koji određuju koja polja zapis mora
imati: **Dublin Core** (petnaest osnovnih polja poput naslova, autora i
datuma), **TEI** za označavanje tekstova, **CIDOC-CRM** kao ontologija
muzejske baštine, **Schema.org / JSON-LD** za podatke na webu i **IIIF** za
digitalne slike. Metapodaci su i ključ rada s LLM-ovima: RAG sustav pretražuje upravo
metapodatke, pa dobar metapodatak daje dobar odgovor.

## Javni resursi i repozitoriji

Dostupni su brojni otvoreni izvori (ishod DSK-3):

| Resurs | Što sadrži |
|--------|------------|
| Europeana | Milijuni digitaliziranih kulturnih dobara EU |
| Croatian Web Archive (HAW) | Arhiv hrvatskoga weba |
| DARIAH-EU i CLARIN | Istraživačka infrastruktura i jezični izvori |
| CROSBI / CroRIS | Hrvatska znanstvena bibliografija |
| Wikidata i Wikipedia | Strukturirano znanje s API-jem |
| Voyant Tools | Analiza teksta u pregledniku |

Uz portale postoje i API-ji (Wikipedia, Europeana, Open Library, YouTube Data
API) za automatsko dohvaćanje; većina zahtijeva ključ, pa provjerite uvjete
korištenja i navedite izvor u izvješću.

## Ishodi učenja (3-4)

- Prepoznati, pretražiti i koristiti javne data-science alate i podatkovne resurse.
- Objasniti i primijeniti tehnike dohvaćanja, pripreme i pohrane podataka.

## Ključni pojmovi

| Pojam | Značenje u jednoj rečenici |
|-------|----------------------------|
| Populacija | Sve jedinice koje istraživanje želi opisati. |
| Uzorak | Dio populacije koji stvarno analiziramo. |
| Reprezentativnost | Uzorak odražava sastav populacije. |
| Pristranost | Sustavno odstupanje uzorka od onoga što se mjeri. |
| Pouzdanost | Stabilnost mjerenja pri ponavljanju. |
| Valjanost | Mjeri li instrument doista ono što tvrdimo da mjeri. |
| FAIR | Načela pronalazivosti, dostupnosti, interoperabilnosti i upotrebljivosti. |
| Metapodaci | Podaci o podacima: tko, kada, što i licenca. |
| Provenancija | Zapis o podrijetlu podataka. |
| AI-spremni podaci | Čisti, strukturirani, označeni i licencirani podaci za strojnu obradu. |

## Provjeri razumiješ

1. Po čemu se primarni podaci razlikuju od digitalnih tragova i zašto ta razlika utječe na zaključke?
2. Objasni razliku između pouzdanosti i valjanosti na primjeru pitanja o odlasku u kino.
3. Što znači svako slovo kratice FAIR i navedi jedan konkretan zahtjev za svako načelo.
4. Zašto su metapodaci posebno važni za rad s velikim jezičnim modelima?

<details><summary>Odgovori</summary>

1. Primarne podatke prikupljamo sami, pa kontroliramo pitanja i uzorak; digitalni
tragovi nastaju kao nusproizvod platformi.
2. Pouzdanost znači da ista osoba u dva navrata odgovara slično; valjanost da
pitanje mjeri ponašanje, a ne stav prema kinu.
3. F — pronalazivi (identifikator i metapodaci), A — dostupni (standardiziran protokol), I — interoperabilni (CSV, JSON-LD), R — ponovno upotrebljivi (licenca, dokumentacija).
4. Jer RAG sustav pretražuje upravo metapodatke, pa prazna ili nedosljedna polja
model popunjava pretpostavkama.

</details>

## Praktično

- Skripta: `scripts/01_pandas_osnove.py` (FAIR provjera kataloga)
- 🟢 Izvezite deset zapisa iz svoje teme u CSV. Zapišite koliko ima stupaca,
  kojeg su tipa i koliko vrijednosti nedostaje.
- 🟢 Napravite tri provjere kvalitete: duplikate, prazne vrijednosti i
  frekvencije najvažnijeg kategorijskog stupca. Rezultate zapišite u README.
- 🟡 Pronađite na Europeani ili arhivu weba dvadeset zapisa o istoj temi i
procijenite FAIR-ost: identifikator, licenca, opis, format.

- 🏆 Izradite JSON-LD zapis svoje zbirke od deset jedinica po poljima Dublin
  Corea i dajte ga LLM-u. Postavite tri pitanja, provjerite točnost na izvornim
  zapisima i zapišite što je u metapodacima nedostajalo.

## Dalje

Sljedeći je korak alat kojim podatke obrađujemo: u
[cjelini 03](03_python_colab.md) postavit ćemo Google Colab i napisati prve
naredbe u bilježnici.

## Literatura

- Bowker, G. C. (2000). Biodiversity datadiversity. *Social Studies of Science*, 30(5), 643-683.
- Grus, J. (2019). *Data Science from Scratch*. O'Reilly.
- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije*. FFRI Rijeka.
  https://github.com/bperak/komunikacija_u_doba_ai
- Wilkinson, M. D. i dr. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, 160018.
