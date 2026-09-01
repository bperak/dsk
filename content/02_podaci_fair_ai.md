# 02. Podaci u kulturi: vrste, FAIR principi, AI-spremnost

**Kolegij:** Data Science u kulturi | 2026./2027.

## Vrste podataka

| Vrsta | Primjeri u kulturi | Analiza |
|-------|-------------------|---------|
| Kvantitativni | Broj posjetitelja, ocjene, frekvencije | Statistika, korelacije |
| Kvalitativni | Intervjui, otvorena pitanja, tekstovi | NLP, tematska analiza |
| Vremenski nizovi | Posjećenost kroz godine | Trendovi |
| Prostorni | Lokacije kulturnih ustanova | Geografska analiza |
| Mrežni | Suradnje, citiranja, društvene mreže | Analiza mreža |
| Multimodalni | Slike, video, govor | Računalni vid, STT |

## Pouzdanost i uzorci

- **Populacija** = sve jedinke koje istražujemo
- **Uzorak** = dio populacije koji analiziramo
- **Reprezentativnost** — uzorak mora odražavati populaciju
- **Pristranost uzorka** — npr. anketa samo među studentima ne opisuje "mlade" općenito

## FAIR principi

Kulturni podaci (katalozi, metapodaci, digitalizirana baština) trebaju biti:

- **F**indable — pronalazivi (metapodaci, perzistentni identifikatori)
- **A**ccessible — dostupni (otvoreni API-ji, licence)
- **I**nteroperable — interoperabilni (standardni formati: CSV, JSON, JSON-LD)
- **R**eusable — ponovno upotrebljivi (dokumentacija, licenciranje)

## AI-spremni podaci

**AI-spremni podaci** = čisti, označeni, dokumentirani podaci koje LLM ili
agent može direktno koristiti:

- Čistoća: bez duplikata, konzistentne vrijednosti
- Označenost: metapodaci o značenju polja
- Dokumentiranost: data dictionary, README
- Strukturiranost: CSV/JSON umjesto PDF-a
- Licenciranje: jasno za strojnu obradu

## Metapodaci

Metapodaci su "podaci o podacima":

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

Dobar metapodatak omogućuje pronalaženje, kontekstualizaciju i ponovnu upotrebu.

## Ishodi učenja (3-4)

- Prepoznati, pretražiti i koristiti javne data-science alate i podatkovne resurse.
- Objasniti i primijeniti tehnike dohvaćanja, pripreme i pohrane podataka.

## Praktično

Skripta: `scripts/01_pandas_osnove.py` (FAIR provjera kataloga)
