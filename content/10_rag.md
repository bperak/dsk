# 10. RAG — razgovor s kulturnom baštinom

**Kolegij:** Data Science u kulturi | 2026./2027.

> **U ovoj cjelini.** Povezujemo dvije prethodne teme — semantičku pretragu (cjelina 09) i veliki jezični model (cjelina 08) — u jedan sustav koji na pitanje o kulturnoj baštini odgovara na temelju vaših dokumenata i uz svaku tvrdnju navodi izvor. To je RAG (*Retrieval-Augmented Generation*): najprije dohvat dokaza, zatim generiranje odgovora.
>
> **Ishodi:** DSK-6, DSK-8
> - Kritički vrednovati AI rezultate (RAG kao mitigacija halucinacija).
> - Koristiti praktične vještine digitalne humanistike.
>
> **Uz ovu cjelinu idu:** skripta `scripts/07_rag_kulturna_bastina.py`, bilježnica `colab/DSK_analiza_upitnika_Rijeka.ipynb` i cjelina 11 (Agentski sustavi).

## Što je RAG?

RAG je skraćenica od engleskoga *Retrieval-Augmented Generation*, što se prevodi kao „dohvatom potpomognuto generiranje". Umjesto da model odgovara iz onoga što je zapamtio tijekom treniranja, sustav najprije pronađe relevantne dijelove vašega korpusa, a zatim modelu preda pitanje zajedno s tim ulomcima. Model tako piše odgovor „gledajući u dokumente", slično studentu koji na ispitu smije koristiti literaturu. Postupak ima tri jasno odvojena koraka:

1. Korisnik postavi pitanje
2. Sustav pronađe najrelevantnije dijelove korpusa (embedding pretraga)
3. LLM generira odgovor **temeljen na dohvaćenim dokazima**

```
Pitanje → Embedding upita → Pretraga korpusa → Top-k dokaza
       → LLM (dokazi + pitanje) → Odgovor s citatima
```

| Korak | Što se događa | Čime se radi u kolegiju |
|-------|---------------|-------------------------|
| Dohvat | Upit se pretvara u vektor i uspoređuje sa vektorima korpusa | model `gemini-embedding-2`, kosinusna sličnost |
| Rangiranje | Bira se *k* najbližih ulomaka | `numpy` sortiranje po sličnosti |
| Generiranje | Model dobiva dokaze i pitanje te piše odgovor s citatima | model `gemini-3.5-flash` |

Razlika prema klasičnoj pretrazi je u tome što tražilica vraća popis dokumenata, a RAG vraća **rečenicu odgovora s navedenim izvorom** — za muzejsku dokumentaciju tvrdnju i inventarni broj uz nju.

**Mali primjer.** Kustos pita: „Koji su predmeti u zbirci vezani uz riječko brodogradilište?" Pretraga po riječi „brodogradilište" promašuje zapise u kojima piše „brod", „škver" ili „navoz". Embedding pretraga ih pronalazi jer uspoređuje značenje, a generativni dio pretvara pronađene ulomke u odgovor s citatima.

```python
from google import genai

MODEL = "gemini-3.5-flash"
client = genai.Client()

# Dokazi dolaze iz dohvata (cjelina 09 i skripta 07); ovdje je skraćen prikaz.
dokazi = [
    "Kazalište HNK Ivan pl. Zajc sagrađeno je 1885. godine u neorenesansnom stilu.",
    "Guvernerova palača sagrađena je 1896. godine.",
]
pitanje = "Kada je sagrađeno riječko kazalište?"
prompt = "Dokazi:\n" + "\n".join(dokazi) + "\n\nPitanje: " + pitanje
odgovor = client.models.generate_content(model=MODEL, contents=prompt)
print(odgovor.text)
```

## Zašto RAG?

RAG je odgovor na četiri praktična problema rada s jezičnim modelima u kulturnim ustanovama: model sam po sebi ne zna što piše u vašim inventarnim knjigama, terenskim bilješkama ili prošlogodišnjem godištu lokalnih novina.

| Problem | Što RAG čini | Primjer u kulturi |
|---------|--------------|-------------------|
| Halucinacije | Odgovor je vezan na priložene dokaze; ako dokaza nema, model to mora reći | Model ne može izmisliti godinu gradnje ako je u dokumentaciji nema |
| Ažurnost | Korpus se mijenja bez ponovnog treniranja modela | Novi godišnjak novina doda se u korpus isti dan |
| Transparentnost | Svaka tvrdnja ima izvor koji se može provjeriti | Citat nosi signaturu, inventarni broj ili godište |
| Privatnost | Dokumenti ostaju u vašem sustavu i ne ulaze u obuku modela | Neobjavljeni rukopisi i transkripti usmenih kazivanja |

**Mali primjer.** Digitalizirani novinski arhiv jedne lokalne redakcije raste svake godine. Ponovno treniranje modela na novim godištima bilo bi skupo i sporo, a za redakciju nedostupno. Ako se novi tekstovi samo dodaju u korpus i ponovno se izračunaju njihovi vektori, asistent odmah odgovara i na pitanja o najnovijem godištu.

## Primjena u kulturi

Isti obrazac vrijedi u svim baštinskim ustanovama; razlikuje se samo korpus iz kojega se dohvaćaju dokazi.

| Ustanova | Tipično pitanje | Gdje su dokazi |
|----------|-----------------|----------------|
| Muzej | „Što se nalazi u Guvernerovoj palači?" | muzejska dokumentacija, inventarne knjige |
| Arhiv | „Kada je sagrađeno kazalište?" | arhivska grada, građevna dokumentacija |
| Digitalna knjižnica | razgovor sa zbirkom dokumenata | katalog i digitalizirani tekst |
| Etnografska zbirka | „Koje su se igre igrale u ovom selu?" | terenske bilješke, zapisi kazivača |
| Lokalna povijest | „Što se pisalo o luci te godine?" | novinski arhiv, kronike |

**Mali primjer (priprema korpusa).** Za muzejsku dokumentaciju jedan ulomak odgovara jednom inventarnom zapisu, jer je zapis zaokružena cjelina; za novinski arhiv ulomak je članak ili nekoliko odlomaka s preklapanjem od jedne rečenice. Uz svaki ulomak čuvaju se metapodaci (signatura, godina, zbirka), jer bez njih citat nije provjerljiv.

## Prompt za RAG

Prompt je ugovor između istraživača i modela. U njemu se ne opisuje samo zadatak, nego i dopušteni izvori i ponašanje u slučaju nedostatka dokaza. Ako se to izostavi, model popunjava praznine iz vlastitoga pamćenja.

```
Odgovori ISKLJUČIVO na temelju dokaza.
Ako odgovor nije u dokazima, reci: "Nije navedeno u izvorima."
Citiraj izvor: (izvor [N])

Dokazi:
[1] ...
[2] ...

Pitanje: ...
```

| Uputa u promptu | Zašto je tu | Što sprečava |
|-----------------|-------------|--------------|
| „ISKLJUČIVO na temelju dokaza" | sužava izvor istine na priloženi korpus | odgovor iz pamćenja modela |
| „Ako odgovor nije u dokazima…" | daje modelu dopušten izlaz iz neznanja | nagađanje i izmišljanje |
| „Citiraj izvor (izvor [N])" | omogućuje provjeru svake tvrdnje | neprovjerljive tvrdnje |

```python
def sastavi_prompt(pitanje, dokazi):
    """Slijedi propisani obrazac; brojevi u uglatim zagradama su oznake izvora."""
    kontekst = "\n".join(f"[{i + 1}] {tekst}" for i, tekst in enumerate(dokazi))
    return (
        "Odgovori ISKLJUČIVO na temelju priloženih dokaza.\n"
        'Ako odgovor nije u dokazima, reci: "Nije navedeno u izvorima."\n'
        "Citiraj izvor: (izvor [N]).\n\n"
        f"Dokazi:\n{kontekst}\n\nPitanje: {pitanje}\n"
    )
```

## Granice RAG-a

RAG smanjuje halucinacije, ali ih ne uklanja: model i dalje može pogrešno pročitati ulomak, a može i spojiti dvije nespojive tvrdnje. Kvaliteta odgovora nikada nije veća od kvalitete korpusa i dohvata.

| Granica | Kako se očituje | Kako se provjerava |
|---------|-----------------|--------------------|
| Prazan dohvat | U korpusu nema odgovora, a pitanje je široko | Provjeri popis dohvaćenih ulomaka i njihove sličnosti |
| Pristran korpus | Zbirka zastupa samo jedan dio pojava | Usporedi sastav korpusa s istraživačkim pitanjem |

## NotebookLM (od srpnja 2026. Gemini Notebook) — RAG koji već koristiš

Postoji alat koji radi upravo ono što smo u ovoj cjelini sastavljali ručno, i vjerojatno ga već koristiš: **NotebookLM**. Google ga je 16. srpnja 2026. preimenovao u **Gemini Notebook** — isti proizvod, isti linkovi i iste bilježnice, novo ime i logo ([Google Workspace Updates](https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html), [blog.google](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook)). U nastavi ga zovemo starim imenom jer se pod njim udomaćio, a ako u sučelju vidiš novo ime, to je isti alat.

Radi po jednom pravilu: **odgovara isključivo iz dokumenata koje si mu predao** i uz svaku tvrdnju daje poveznicu na mjesto u izvoru. Zato je on **RAG u gotovom obliku** — i najbrži način da vidiš kako RAG izgleda izvana, prije nego što ga sam sastaviš.

| Korak RAG-a (naš kod u `scripts/07_rag_kulturna_bastina.py`) | Što to znači u NotebookLM-u |
|---|---|
| Korpus | ploča *Sources*: PDF-ovi, dokumenti, mrežne stranice, YouTube, Google Drive |
| Usitnjavanje i embedding | alat to radi u pozadini, korisnik to ne vidi |
| Dohvat po značenju | tvoje pitanje u razgovoru |
| Generiranje uz dokaze | odgovor s numeriranim citatima na ulomke izvora |
| „Nema u korpusu" | kad u izvorima nema pokrića, alat kaže da odgovora nema |

**Duboko istraživanje (Deep Research).** Uz dodavanje vlastitih izvora alat ima funkciju *Deep Research*: iz tvog pitanja složi plan istraživanja, pregleda stotine mrežnih stranica i vrati organizirano izvješće **sa svojim popisom izvora**, koje zatim možeš uvesti u bilježnicu ([Googleov opis](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-deep-research-file-types)). Time se mijenja jedna važna stvar: nakon dubokog istraživanja korpus **nije više samo ono što si ti odabrao** — u njega su ušli izvori koje je alat pronašao. Zato vrijedi pravilo: kad uvoziš izvore iz dubokog istraživanja, **prođi ih jedan po jedan** i zadrži samo one koje bi i sam citirao.

**Zašto je to dobro za učenje RAG-a.** Kod ručno građenog asistenta korak dohvata ostaje nevidljiv, a ovdje je vidljiv na tri mjesta: u ploči izvora (što je uopće u korpusu), u citatima (odakle tvrdnja dolazi) i u odbijanju (kad odgovora u korpusu nema). Razumiješ li ta tri mjesta, razumiješ i RAG.

**Radni postupak za seminarski rad:**

1. Za svaku temu otvori **zasebnu bilježnicu** — bilježnice ne razgovaraju jedna s drugom, pa se građa ne miješa.
2. Ubaci **primarne izvore**: znanstvene radove, muzejsku dokumentaciju, novinske članke, vlastite transkripte.
3. Postavljaj konkretna pitanja i **klikni na svaki citat** — provjeri da ulomak doista tvrdi ono što odgovor kaže.
4. Zabilježi **koje si izvore upotrijebio, a koje odbacio i zašto** — to je građa za poglavlje o metodologiji.
5. Ako si koristio duboko istraživanje, u metodologiji napiši **koje je izvore alat predložio**, a koje si zadržao.

**Granice koje ostaju i kad alat radi besprijekorno.** *Pokrivenost* — nema dokumenta, nema odgovora; *pristranost* — kakvi su ti izvori, takav je i sažetak; *računanje* — alat citira rečenicu, ali ne računa umjesto tebe; *odgovornost* — za tvrdnju u radu odgovara onaj koji ga potpisuje, ne alat. Besplatna razina u pravilu drži do pedeset izvora po bilježnici, a točne granice i dnevne kvote provjeri na [službenoj stranici pomoći](https://support.google.com/notebooklm).

## Ishodi učenja (6, 8)

- Kritički vrednovati AI rezultate (RAG kao mitigacija halucinacija).
- Koristiti praktične vještine digitalne humanistike.

| Ishod | Kako se ostvaruje u ovoj cjelini |
|-------|----------------------------------|
| Kritičko vrednovanje (6) | Usporedba odgovora sa i bez dokaza; provjera popisa dohvaćenih ulomaka |
| Digitalna humanistika (8) | Izgradnja RAG asistenta nad vlastitim korpusom i njegova dokumentacija |

## Ključni pojmovi

| Pojam | Značenje |
|-------|----------|
| RAG | Dohvat dokaza iz korpusa pa generiranje odgovora na temelju njih |
| Korpus | Skup dokumenata nad kojima asistent odgovara |
| Dohvat | Pronalazak najrelevantnijih ulomaka embedding pretragom |
| Ulomak | Manja cjelina korpusa (zapis, članak, odlomak) koja se dohvaća |
| Top-k | Broj ulomaka koji se predaju modelu |
| Citiranje izvora | Oznaka izvora uz svaku tvrdnju u odgovoru |
| Halucinacija | Tvrdnja koju model iznosi bez osnove u dokazima |
| NotebookLM / Gemini Notebook | Alat koji odgovara isključivo iz tvojih izvora i citira ih — gotov RAG |
| Duboko istraživanje (Deep Research) | Automatsko pronalaženje izvora i izvješće, uz uvoz izvora u bilježnicu |
| Pridržanost izvorima (grounding) | Pravilo da svaki odgovor mora imati pokriće u korpusu |

## Provjeri razumiješ

**1. Zašto RAG smanjuje broj halucinacija, ali ih ne uklanja potpuno?**

<details><summary>Odgovori</summary>

Zato što model odgovara na temelju priloženih ulomaka, a ne iz pamćenja. No model i dalje može pogrešno pročitati ulomak, spojiti dvije nepovezane tvrdnje ili nagađati kada su dokazi nedostatni. Zato se svaka tvrdnja provjerava u izvoru na koji citat upućuje.

</details>

**2. Objasnite razliku između ažuriranja korpusa i ponovnog treniranja modela.**

<details><summary>Odgovori</summary>

Ažuriranje korpusa znači dodavanje novih dokumenata i ponovni izračun njihovih vektora; traje kratko i dostupno je svakoj ustanovi. Ponovno treniranje mijenja sam model: skupo je, sporo i izvan mogućnosti male redakcije ili muzeja. RAG zato rješava ažurnost bez treniranja.

</details>

**3. Zašto uz svaki ulomak korpusa čuvamo metapodatke?**

<details><summary>Odgovori</summary>

Bez signature, godine i zbirke citat nije provjerljiv. Metapodaci omogućuju da čitatelj ode do izvora i provjeri tvrdnju, a istraživaču da kasnije rekonstruira koji je dokument upotrijebljen u pojedinom odgovoru.

</details>

**4. Što treba odgovoriti asistent ako odgovora nema u korpusu i zašto je to važno?**

<details><summary>Odgovori</summary>

Treba odgovoriti da odgovora nije navedeno u izvorima, kako to propisuje prompt. Time se čuva razlika između „nema podatka u našoj dokumentaciji" i „podatak ne postoji". Drugo je istraživački zaključak koji model ne smije donositi sam.

</details>

## Praktično

- 🟢 Otvori bilježnicu u NotebookLM-u (Gemini Notebooku), ubaci tri izvora o istoj temi i postavi pitanje na koje odgovor već znaš. Klikni na citat i pročitaj ulomak; zatim postavi pitanje na koje u izvorima nema odgovora i pogledaj što će alat odgovoriti.
- 🟡 Usporedi odgovor NotebookLM-a i našeg RAG asistenta (`scripts/07_rag_kulturna_bastina.py`) na isto pitanje i isti korpus. Napiši tri razlike: što je bolje u alatu, što u našem kodu i što nijedan nije mogao.
- 🟢 Pokreni `scripts/07_rag_kulturna_bastina.py` i postavi četiri pripremljena pitanja. Zabilježi za svako pitanje koje je ulomke sustav dohvatio i slaže li se odgovor s njima.
- 🟡 Promijeni broj dohvaćenih ulomaka (parametar `k`) i dodaj tri nove rečenice o riječkoj baštini u korpus. Promatraj kada odgovor postaje bogatiji, a kada počinje lutati.
- 🏆 Sastavi vlastiti korpus od pet do deset zapisa (inventarni zapisi, novinski isječci, terenske bilješke) i izgradi RAG asistent nad njim. U izvješću navedi sastav korpusa, upotrijebljeni prompt i primjer odgovora s citatom, te jedan slučaj kada asistent nije imao dokaza.

## Dalje

Sljedeća cjelina, **11. Agentski sustavi — automatizirani istraživač**, nadograđuje ovaj obrazac: model više ne samo odgovara na pitanje, nego sam poziva alate, provodi analizu i ponavlja korake dok ne dođe do rezultata.

## Literatura

- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije: Razvoj velikih jezičnih modela i komunikacijskih agenata*. Rijeka: Filozofski fakultet u Rijeci. https://github.com/bperak/komunikacija_u_doba_ai
- Lewis, P. et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020. arXiv:2005.11401
- Bommasani, R. et al. (2021). *On the Opportunities and Risks of Foundation Models*. arXiv:2108.07258
- Grus, J. (2019). *Data Science from Scratch*. O'Reilly.
