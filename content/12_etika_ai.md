# 12. Etika i kritičko vrednovanje AI rezultata

**Kolegij:** Data Science u kulturi | 2026./2027.

> **U ovoj cjelini.** Zatvaramo krug. Nakon prikupljanja i analize podataka, RAG asistenta i agenata, ostaje najvažnije pitanje: kada vjerovati modelu. Učimo prepoznati halucinacije, pristranost korpusa i neprovjerene brojke te ispravno navesti upotrebu AI alata u seminarskom radu.
>
> **Ishodi:** DSK-6
> - Kritički vrednovati rezultate, metode i tehnike analize podataka,
>   uključujući rezultate AI alata.
>
> **Uz ovu cjelinu idu:** bilježnica `colab/DSK_analiza_upitnika_Rijeka.ipynb` (AI sloj i sažetak) i upute za projekt `projekt/UPUTE_PROJEKT.md`.

## Ključna vještina 2026.: kada vjerovati modelu?

Model ne griješi uvijek na isti način: neke pogreške dolaze iz toga kako je model nastao, neke iz korpusa, a neke iz izostale provjere. Tablica daje pet glavnih rizika s primjerom iz kulture i načinom ublažavanja.

| Rizik | Primjer u kulturi | Mitigacija |
|-------|-------------------|------------|
| Halucinacije | Izmišljeni podatak o autoru | RAG s dokazima, provjera izvora |
| Pristranost korpusa | Zbirke favoriziraju zapadne autore | Auditi reprezentacije |
| Anakronizmi | Moderni koncepti projicirani na prošlost | Kontekstualizacija |
| Privatnost | Digitalizirani osobni podaci | Anonimizacija, etički okviri |
| Autorska prava | Trening na zaštićenim djelima | Transparentnost, licence |

**Mali primjer.** Muzejska dokumentacija navodi da je slika naslikana „u prvoj polovini 20. stoljeća". Model to u sažetku pretvori u „1923. godine" — halucinacija s lažnom preciznošću. Takva tvrdnja ne smije ući u izvješće bez provjere.

## Halucinacije i pristranost korpusa

**Halucinacija** je tvrdnja koju model iznosi tečno i uvjerljivo, a koja nema osnove u izvorima. Nastaje zato što model predviđa sljedeću riječ, a ne provjerava činjenice. Opasnija je od očite pogreške jer je stilski besprijekorna.

**Pristranost korpusa** je druga vrsta problema: tvrdnja može biti točna, ali je slika iskrivljena jer u korpusu prevladava jedan glas. Digitaliziramo li samo novine jednoga političkog opredjeljenja, asistent će taj pogled prenositi kao cjelinu lokalne povijesti.

| Pojava | Kako se prepoznaje | Što učiniti |
|--------|--------------------|-------------|
| Izmišljeni podatak | Detalj je precizniji od izvora | Vratiti se na izvor i prepisati njegovu formulaciju |
| Izmišljeni izvor | Citirana jedinica ne postoji u katalogu | Provjeriti signaturu u katalogu |
| Sablasni citat | Izvor postoji, ali tvrdi nešto drugo | Pročitati cijeli ulomak, ne samo citiranu rečenicu |
| Neuravnotežen korpus | Jedan glas prevladava bez objašnjenja | Navesti sastav korpusa i njegove slijepe točke |

**Mali primjer.** Etnografska zbirka sadrži deset zapisa o jednoj seoskoj svetkovini, a svi su zabilježeni istoga sakupljača. Asistent će običaj opisati dosljedno, ali to je pogled jednoga kazivača. Zato u izvješću navodimo tko je bilježio, kada i koje glasove korpus ne zastupa.

## Kako provjeriti brojku iz teksta modela

Modeli loše računaju: brojka u odgovoru češće je procjena iz jezika nego rezultat izračuna. Svaka brojka koja ulazi u rad prolazi kroz isti postupak.

1. **Zapiši tvrdnju** onako kako je model izrekao, bez dorade.
2. **Nađi izvor** iz kojega brojka navodno dolazi.
3. **Izračunaj sam** u Colabu, nad podacima koje možeš pokazati.
4. **Usporedi** izračun s tvrdnjom modela i u radu navedi vlastitu brojku, ne onu koju je model izrekao.

```python
import pandas as pd

df = pd.DataFrame({
    "zbirka": ["Moderna", "Moderna", "Grafika", "Fotografija", "Moderna", "Grafika"],
})

# Tvrdnja modela: "Moderna zbirka cini 66 % fundusa."
tvrdnja_modela = 0.66

udio = df["zbirka"].value_counts(normalize=True)["Moderna"]
print(f"Izracun: {udio:.0%}  (n = {len(df)})")
print(f"Tvrdnja modela: {tvrdnja_modela:.0%}")
print("Tvrdnja se poklapa s izracunom:", abs(tvrdnja_modela - udio) < 0.01)
```

| Situacija | Što to znači | Kako postupiti |
|-----------|--------------|----------------|
| Brojka se poklapa | Izračun potvrđuje tvrdnju | Navedi vlastiti izračun i veličinu uzorka |
| Brojka se razlikuje | Model je procijenio ili pogriješio | U radu navedi točan izračun i zabilježi razliku |
| Brojke nema u podacima | Tvrdnja je neprovjerljiva | Ispusti tvrdnju ili je izričito označi kao neutemeljenu |

## Pravila odgovorne upotrebe

1. **LLM = asistent za prvi nacrt** — ne za konačno tumačenje
2. **Navodi AI upotrebu** — akademska čestitost zahtijeva transparentnost
3. **Provjeri svaki broj** — modeli loše računaju
4. **Kontekstualiziraj** — podaci bez konteksta lažu
5. **Ne izmišljaj izvore** — svaka tvrdnja mora imati provjerljiv izvor

| Pravilo | Što znači u radu | Kako se krši |
|---------|------------------|--------------|
| Navođenje | U metodologiji je opisano što je AI radio | Korištenje bez ijedne napomene |
| Kontekst | Uz podatak ide vrijeme, mjesto i izvor | Postotak bez veličine uzorka |
| Provjera brojeva | Svaka brojka ima svoj izračun | Prepisivanje brojke iz odgovora modela |

**Mali primjer (navod u metodologiji).** Dovoljna je jedna rečenica: „Kodiranje otvorenih odgovora provedeno je uz pomoć modela `gemini-3.5-flash`; model je predložio kategorije, a autor je svaki odgovor ručno provjerio." Čitatelju je tada jasno što je stroj, a što istraživač.

## Povreda akademske čestitosti

> Svaka upotreba tuđeg teksta ili drugog oblika autorskog djela, kao i upotreba
> ChatGPT ili bilo kojeg drugog alata čija se funkcionalnost temelji na umjetnoj
> inteligenciji, **bez jasnog i nedvosmislenog navođenja izvora**, smatra se
> povredom tuđeg autorskog prava i načela akademske čestitosti te predstavlja
> tešku povredu studentskih obveza.

Iz navedenoga proizlazi obveza: upotreba AI alata nije zabranjena, ali je **navođenje obvezno**. Kad je navod potpun, upotreba je dio metodologije; kad navoda nema, isti je postupak povreda studentskih obveza.

| Razina upotrebe | Kako se navodi | Primjer iz projekta |
|-----------------|----------------|---------------------|
| Priprema | Kratko u metodologiji | Model predložio anketna pitanja, autor ih preuredio |
| Obrada | Uz opis metode | Model predložio kategorije, autor ih potvrdio |
| Tekst | Uz pojedini dio teksta | Model jezično uredio odlomak, sadržaj je autorov |

## Ishodi učenja (6)

- Kritički vrednovati rezultate, metode i tehnike analize podataka,
  uključujući rezultate AI alata.

| Ishod | Kako se ostvaruje u ovoj cjelini |
|-------|----------------------------------|
| Kritičko vrednovanje (6) | Pet rizika, postupak provjere brojke i pravila navođenja upotrebe AI alata |

## Ključni pojmovi

| Pojam | Značenje |
|-------|----------|
| Halucinacija | Tečno izrečena tvrdnja bez osnove u izvorima |
| Sablasni citat | Izvor postoji, ali ne tvrdi ono što mu se pripisuje |
| Pristranost korpusa | Iskrivljena slika zbog neravnomjernoga sastava izvora |
| Anakronizam | Pripisivanje sadašnjih pojmova prošlosti |
| Anonimizacija | Uklanjanje osobnih podataka iz građe prije obrade |
| Provjera brojke | Samostalan izračun u Colabu i usporedba s tvrdnjom modela |
| Akademska čestitost | Pravilo da se svaki tuđi doprinos jasno navodi |
| Navod upotrebe AI alata | Opis u metodologiji što je alat radio, a što istraživač |
| Transparentnost | Čitatelj može provjeriti svaki korak i izvor |

## Provjeri razumiješ

**1. Zašto je halucinacija opasnija od očite pogreške u odgovoru?**

<details><summary>Odgovori</summary>

Zato što je izrečena tečno i uvjerljivo, pa je čitatelj ne prepoznaje kao pogrešku. Očita se pogreška vidi odmah, a halucinacija se otkriva samo provjerom u izvoru. Zato svaka takva tvrdnja mora imati provjerljiv izvor.

</details>

**2. Kako prepoznati pristranost korpusa ako su pojedinačne tvrdnje točne?**

<details><summary>Odgovori</summary>

Pristranost se ne vidi u pojedinoj tvrdnji, nego u sastavu korpusa: tko je izvore zabilježio, kada i kojega glasa nema. Ako jedna skupina ili razdoblje prevladava bez objašnjenja, slika je iskrivljena iako su citati točni.

</details>

**3. Objasnite postupak provjere brojke koju je izrekao model.**

<details><summary>Odgovori</summary>

Tvrdnja se zapiše kako je izrečena, pronađe se izvor, brojka se samostalno izračuna u Colabu i usporedi s tvrdnjom. U rad ulazi vlastiti izračun, uz veličinu uzorka; ako brojke u podacima nema, tvrdnja se ispušta ili označava kao neutemeljena.

</details>

**4. Zašto upotrebu AI alata treba navesti ako je dopuštena?**

<details><summary>Odgovori</summary>

Zato što čitatelj mora znati koji je dio posla obavio alat, a koji istraživač, da bi mogao procijeniti pouzdanost rezultata. Navod nije kazna, nego dio metodologije: bez njega se rad ne može vrednovati.

</details>

## Praktično

- 🟢 Prođi kroz poglavlje „Etika i kritičko vrednovanje AI rezultata" u bilježnici `colab/DSK_analiza_upitnika_Rijeka.ipynb` i provjeri jednu tvrdnju modela u podacima.
- 🟡 Uzmi tri brojke iz AI sažetka svoje analize i za svaku provedi postupak provjere.
- 🏆 Sastavi odlomak metodologije svoga rada o upotrebi AI alata: koji model, na kojim podacima, što je predložio i što je autor provjerio. Uskladi ga s `projekt/UPUTE_PROJEKT.md`.

## Dalje

Ovdje se krug zatvara: od postavki znanosti o znanosti, preko podataka, Pythona, statistike i vizualizacije, do obrade teksta, jezičnih modela, embeddinga, RAG asistenta i agenata. Sljedeći korak nije nova cjelina, nego **projekt**: tema, anketa, analiza u Colabu, seminarski rad i prezentacija, uz pravila o AI alatima iz `projekt/UPUTE_PROJEKT.md`.

## Literatura

- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije: Razvoj velikih jezičnih modela i komunikacijskih agenata*. Rijeka: Filozofski fakultet u Rijeci. https://github.com/bperak/komunikacija_u_doba_ai
- Perak, B. (2026). *Data Science u kulturi — materijali kolegija*. Filozofski fakultet u Rijeci. https://github.com/bperak/dsk
- Bommasani, R. et al. (2021). *On the Opportunities and Risks of Foundation Models*. arXiv:2108.07258
- Grus, J. (2019). *Data Science from Scratch*. O'Reilly.
