# 📕 KNJIGA: Data Science u kulturi
## Prvi lejer — kostur knjige (v0.1, rujan 2026.)

> **Temelj:** kolegij Data Science u kulturi (FFRI) + knjiga *Komunikacija u doba
> umjetne inteligencije* (Perak 2025) kao teorijska podloga.
> **Status:** prvi lejer (struktura + prošireni sadržaj). Sljedeći lejer:
> raspisivanje poglavlja u puni tekst.

---

## 0. KONCEPT KNJIGE

### Radni naslov (opcije)
1. **Data Science u kulturi: metode, podaci i umjetna inteligencija u digitalnoj humanistici**
2. **Kultura u doba podataka: priručnik digitalne humanistike**
3. **Podaci, kultura i umjetna inteligencija: praktična digitalna humanistika**

### Ciljana publika
- Studenti preddiplomskih i diplomskih studija kulturalnih studija, digitalne
  humanistike, informacijskih znanosti
- Istraživači u humanistici koji ulaze u podatkovnu znanost
- Praktičari u kulturnim institucijama (muzeji, arhivi, knjižnice) — AI spremnost

### Pozicioniranje
- **Prva hrvatska knjiga** koja povezuje podatkovnu znanost, kulturu i
  umjetnu inteligenciju (LLM, RAG, agente) u praktičnom, nastavno utemeljenom formatu
- Nastavak/komplement knjige *Komunikacija u doba umjetne inteligencije*
  (Perak 2025): tamo teorija komunikacijskih agenata, ovdje **praktične metode**
- Open access + otvoreni kod (GitHub repozitorij uz knjigu)

### Format
- ~250 stranica (prosječno 12-15 str. po poglavlju)
- Poglavlja: teorija + primjeri + kod + vježbe (🟢🟡🏆)
- Kod izvršiv u Colabu (svi primjeri verificirani)
- Izdanje: FFRI (Biblioteka Filozofskih fakulteta) ili komercijalni izdavač

---

## 1. STRUKTURA KNJIGE (4 dijela, 14 poglavlja)

### UVOD (predgovor + uvod)
- Predgovor: zašto ova knjiga, kako je nastala iz nastave
- Uvod: čitatelj na putu od pitanja do podatka

---

### DIO I — TEMELJI (pogl. 1-3)
**"Što je podatkovna znanost u kulturi i zašto je trebamo?"**

#### Poglavlje 1: Uvod u data science u kulturi
*Status: ✅ postoji skica (content/01)*
- 1.1 Što je data science u kulturi? (definicije, sjecište disciplina)
- 1.2 AI revolucija u humanistici: od tablica do agenata
- 1.3 Znanost o znanosti: kako se gradi istraživanje
- 1.4 Istraživački proces u 8 koraka
- 1.5 Pregled knjige (mapa poglavlja)

#### Poglavlje 2: Podaci u kulturi
*Status: ✅ postoji skica (content/02)*
- 2.1 Vrste podataka u kulturi (kvantitativni, kvalitativni, mrežni, multimodalni)
- 2.2 Pouzdanost, uzorci i pristranost
- 2.3 FAIR principi upravljanja podacima
- 2.4 Metapodaci: podaci o podacima
- 2.5 AI-spremni podaci (što LLM/agent treba od podatka)
- 2.6 Javni resursi i repozitoriji (Croatian Web Archive, Europeana, DARIAH, CLARIN, CroRIS)

#### Poglavlje 3: Python i Google Colab za humaniste
*Status: ✅ postoji skica (content/03)*
- 3.1 Zašto Python (a ne Excel)?
- 3.2 Google Colab kao kolaborativno okruženje
- 3.3 Osnove jezika: varijable, liste, rječnici, petlje, funkcije
- 3.4 Struktura Colab bilježnice (Markdown + kod + @title + userdata)
- 3.5 Postavljanje okruženja i API ključeva
- 3.6 Vježbe 🟢🟡🏆

---

### DIO II — METODE (pogl. 4-7)
**"Kako analizirati kulturne podatke"**

#### Poglavlje 4: Tablični podaci s Pandas
*Status: ✅ postoji skica (content/04)*
- 4.1 DataFrame: retci, stupci, varijable
- 4.2 Učitavanje podataka (CSV, Excel, JSON, API)
- 4.3 Čišćenje podataka (duplikati, null, formati)
- 4.4 Grupiranje i agregacije
- 4.5 Spajanje tablica
- 4.6 FAIR priprema za AI (JSON eksport)
- 4.7 Vježbe 🟢🟡🏆

#### Poglavlje 5: Statistika za kulturologa
*Status: ✅ postoji skica (content/05)*
- 5.1 Deskriptivna statistika (mean, medijan, mod, SD)
- 5.2 Raspodjele i percentili
- 5.3 Korelacije (Pearson, Spearman) — korelacija ≠ uzročnost
- 5.4 Statistička značajnost i p-vrijednosti
- 5.5 LLM u statistici: generiranje koda, interpretacija, provjera
- 5.6 Vježbe 🟢🟡🏆

#### Poglavlje 6: Vizualizacija podataka
*Status: ✅ postoji skica (content/06)*
- 6.1 Zašto vizualizacija: graf vrijedi 1000 riječi
- 6.2 Pravila poštene vizualizacije
- 6.3 Matplotlib i Seaborn (histogram, scatter, bar, box, line)
- 6.4 Vizualizacija mreža i mapa (dodatak)
- 6.5 LLM generira i interpretira grafove
- 6.6 Vježbe 🟢🟡🏆

#### Poglavlje 7: Tekst i NLP
*Status: ✅ postoji skica (content/07)*
- 7.1 Tekst kao podatak u kulturi
- 7.2 Tokenizacija, čišćenje, stop-riječi
- 7.3 Frekvencije, kolokacije, n-grami
- 7.4 Od frekvencija do značenja: embedding, sentiment, teme
- 7.5 Kritički pristup tekstualnoj analizi
- 7.6 Vježbe 🟢🟡🏆

---

### DIO III — UMJETNA INTELIGENCIJA (pogl. 8-11)
**"Suvremeni AI stack za kulturu"** ← jezgra knjige

#### Poglavlje 8: Veliki jezični modeli u podatkovnoj znanosti
*Status: ✅ postoji skica (content/08)*
- 8.1 Što je LLM: kratka povijest i arhitektura (Transformer, pozornost)
- 8.2 LLM kao komunikacijski agent (veza s Perak 2025)
- 8.3 Primjene: klasifikacija, ekstrakcija, sažimanje, kod
- 8.4 Strukturirani izlaz (JSON)
- 8.5 Ograničenja: halucinacije, pristranost, provjera
- 8.6 Vježbe 🟢🟡🏆

#### Poglavlje 9: Embedding i semantička pretraga
*Status: ✅ postoji skica (content/09)*
- 9.1 Distribucijska semantika: riječi kao vektori
- 9.2 Embedding modeli i kosinusna sličnost
- 9.3 Semantička pretraga kulturnih zbirki (primjeri)
- 9.4 Preporuke, deduplikacija, klasteriranje
- 9.5 Vježbe 🟢🟡🏆

#### Poglavlje 10: RAG — razgovor s kulturnom baštinom
*Status: ✅ postoji skica (content/10)*
- 10.1 Što je RAG i zašto rješava halucinacije
- 10.2 Arhitektura: dohvat → generiranje → citiranje
- 10.3 Izgradnja korpusa (muzeji, arhivi, knjižnice)
- 10.4 Prompt inženjering za RAG (dokazi, citati)
- 10.5 Vrednovanje RAG sustava
- 10.6 Vježbe 🟢🟡🏆

#### Poglavlje 11: Agenti i automatizirano istraživanje
*Status: ✅ postoji skica (content/11)*
- 11.1 Od LLM-a do agenta: ReAct obrazac
- 11.2 Agenti u istraživanju kulture (katalog + statistika + vizualizacija)
- 11.3 Google ADK (LlmAgent, LoopAgent, FunctionTool)
- 11.4 MCP: modeli i alati (korpus, baza, API)
- 11.5 Granice: agent nije neovisan istraživač
- 11.6 Vježbe 🟢🟡🏆

---

### DIO IV — PRAKSA I ETIKA (pogl. 12-14)
**"Od projekta do znanja"**

#### Poglavlje 12: Projektno istraživanje od A do Ž
*Status: 🆕 treba napisati (temelj: projekt/ folder)*
- 12.1 Projektni prijedlog: Domena / Problem / Cilj
- 12.2 Dizajn ankete (Google Forms: demografija, Likert, otvorena)
- 12.3 Prikupljanje i priprema odgovora
- 12.4 Analiza: statistika + vizualizacija + LLM
- 12.5 Seminarski rad: struktura i pisanje
- 12.6 Prezentacija rezultata
- 12.7 Studija slučaja: "Utjecaj društvenih mreža na body image" (prošle godine)

#### Poglavlje 13: Etika, AI i akademska čestitost
*Status: ✅ postoji skica (content/12)*
- 13.1 Rizici AI-a: halucinacije, pristranost, anakronizmi, privatnost
- 13.2 Pravila odgovorne upotrebe AI u istraživanju
- 13.3 AI i akademska čestitost (navođenje izvora)
- 13.4 Podaci i autorska prava
- 13.5 Budućnost: kultura, podaci i agenti

#### Poglavlje 14: Zaključak — kultura u doba umjetne inteligencije
*Status: 🆕 treba napisati*
- 14.1 Što smo naučili (mapiranje na ishode)
- 14.2 Put naprijed: od podataka do znanja
- 14.3 Poziv na praksu

---

## 2. DODACI (A-F)

- **Dodatak A:** Postavljanje okruženja (pip, API ključevi, Colab)
- **Dodatak B:** Rječnik pojmova (token, embedding, RAG, FAIR, agent...)
- **Dodatak C:** Rješenja vježbi (🟢🟡)
- **Dodatak D:** Predlošci (anketa, projektni prijedlog, seminarski rad)
- **Dodatak E:** Resursi i literatura (komentirani popis)
- **Dodatak F:** Repozitorij koda (veza na GitHub + sve skripte)

---

## 3. STATUS SADRŽAJA

| Dio | Poglavlje | Status | Opseg |
|-----|-----------|--------|-------|
| I | 1. Uvod | ✅ skica (2.5k) | 12-15 str |
| I | 2. Podaci | ✅ skica (2.2k) | 12-15 str |
| I | 3. Python/Colab | ✅ skica (1.6k) | 12-15 str |
| II | 4. Pandas | ✅ skica (1.4k) | 12-15 str |
| II | 5. Statistika | ✅ skica (1.4k) | 12-15 str |
| II | 6. Vizualizacija | ✅ skica (1.4k) | 12-15 str |
| II | 7. NLP | ✅ skica (1.3k) | 12-15 str |
| III | 8. LLM | ✅ skica (1.5k) | 15-18 str |
| III | 9. Embedding | ✅ skica (1.2k) | 12-15 str |
| III | 10. RAG | ✅ skica (1.4k) | 15-18 str |
| III | 11. Agenti | ✅ skica (1.6k) | 15-18 str |
| IV | 12. Projekt | 🆕 temelj u projekt/ | 15-20 str |
| IV | 13. Etika | ✅ skica (1.6k) | 12-15 str |
| IV | 14. Zaključak | 🆕 | 6-8 str |
| | Dodaci A-F | 🆕 | 25-30 str |

**Ukupno procijenjeno: ~200-250 stranica**

---

## 4. SLJEDEĆI KORACI (lejer 2)

1. **Odobriti strukturu** (naslov, dijelovi, poglavlja)
2. **Raspisati DIO I** (pogl. 1-3) u puni tekst kao pilot — potvrditi ton i dubinu
3. **Definirati ton:** priručnik (praktično, korak-po-korak) vs udžbenik (teorijski)
4. **Odlučiti o izdavaču:** FFRI Biblioteka (open access) / komercijalni
5. **Pripremiti poglavlja za recenziju** (2 recenzenta)
6. **Prikupljanje stvarnih primjera** — studentski projekti (uz suglasnost)
7. **Verifikacija koda** — svi primjeri izvršivi u Colabu

---

## 5. POVEZNICE

- **Sadržaj kolegija:** https://github.com/bperak/dsk (content/, scripts/, projekt/)
- **Teorijska knjiga:** *Komunikacija u doba umjetne inteligencije* (Perak 2025),
  https://github.com/bperak/komunikacija_u_doba_ai
- **Colab:** https://colab.research.google.com
