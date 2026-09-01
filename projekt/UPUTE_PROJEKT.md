# Upute za projekt — Data Science u kulturi 2026./2027.

## Cilj projekta

Projektno istraživanje u kojem svaki student:
1. definira temu (Domena/Problem/Cilj),
2. izrađuje anketu (Google Forms),
3. prikuplja i analizira podatke (Colab + Pandas),
4. piše seminarski rad i prezentira rezultate.

## Faze projekta

### Faza 1: Definicija teme (rok: 2. tjedan nastave)
- Upisuje se u Google Sheet (kolona **Definicija teme**)
- Format: **Domena / Problem / Cilj** (vidi `PRIJEDLOG_TEMPLATE.md`)
- Primjeri iz prethodnih godina: vidi `PRIMJERI_IZ_PROSLIH_GODINA.md`

### Faza 2: Anketa (Google Forms)
- Minimalno 10 pitanja
- Mješavina: demografija (dob, spol), stavovi (Likert skala 1-5),
  ponašanje (frekvencije), otvorena pitanja
- Ciljana publika: minimalno 20 ispitanika
- Link na anketu unosi se u Google Sheet (kolona **ANKETA**)

### Faza 3: Analiza u Colabu
- Učitavanje odgovora (CSV export iz Google Forms)
- Čišćenje podataka (Pandas)
- Deskriptivna statistika
- Vizualizacija (Matplotlib/Seaborn)
- (Opcionalno) LLM analiza otvorenih odgovora

### Faza 4: Seminarski rad
Struktura:
1. **Uvod** — domena, problem, cilj, istraživačka pitanja
2. **Pregled literature** — što se već zna
3. **Metodologija** — uzorak, instrument (anketa), postupak
4. **Rezultati** — tablice, grafovi, ključni nalazi
5. **Rasprava** — interpretacija, ograničenja, buduća istraživanja
6. **Zaključak**
7. **Literatura**

### Faza 5: Prezentacija
- Kratko izlaganje (5-10 min)
- Ključni rezultati + vizualizacije
- Odgovori na pitanja

## Ocjenjivanje

| Aktivnost | ECTS | Maks. bodova |
|-----------|------|--------------|
| Pohađanje nastave | 1,5 | - |
| Kontinuirana provjera znanja 1 | 1 | 20 |
| Kontinuirana provjera znanja 2 (projekt) | 2,5 | 50 |
| Završni ispit | 0 | 0 |
| **UKUPNO** | **5** | **100** |

(Bez završnog ispita — kontinuirano vrednovanje tijekom nastave.)

## AI alati u projektu — pravila

- ✅ Dopušteno: LLM za pomoć pri generiranju anketnih pitanja, čišćenju
  podataka, analizi otvorenih odgovora, interpretaciji rezultata
- ✅ Dopušteno: semantička pretraga, RAG, agenti za analizu
- ⛔ Obavezno: **jasno navesti svaku upotrebu AI alata** (u metodologiji)
- ⛔ Zabranjeno: predstavljanje AI-generiranog teksta kao vlastitog bez navoda
- ⛔ Zabranjeno: izmišljanje podataka (fabriciranje anketnih odgovora)

## Prijašnji workflow (za referencu)

| Godina | Proces |
|--------|--------|
| 2021/22 | Link na anketu + Colab analiza + zadani podaci (Covid, Sabor, Spotify) |
| 2022/23 | Colab analiza upitnika + seminarski rad + završni test |
| 2023/24 | DS_Form_1 (9.10.) + Definicija teme (16.10.) + Colab 1 + Colab 2 |
| 2024/25 | Prvi GForms + Seminarski rad preko GFORMS + Definicija teme + prezentacija |
| 2025/26 | ANKETA + Colab za anketu + GFORMS + Definicija teme + prezentacija |
