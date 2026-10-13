# 06. Vizualizacija podataka

**Kolegij:** Data Science u kulturi | 2026./2027.

> **U ovoj cjelini.** Nalaze iz anketa, kataloga i evidencija posjećenosti pretvaramo u grafove koji pošteno i čitljivo prenose podatak. Učimo pravila dobre vizualizacije, koji graf odgovara kojem pitanju, kako se koriste Matplotlib i Seaborn te koje pogreške u grafovima zavaravaju čitatelja.
>
> **Ishodi:** **DSK-6** Kritički vrednovati rezultate, metode i tehnike analize podataka.
>
> **Uz ovu cjelinu idu:** skripta [`scripts/03_vizualizacija.py`](../scripts/03_vizualizacija.py), bilježnica [`colab/DSK_analiza_upitnika_jednostavno.ipynb`](../colab/DSK_analiza_upitnika_jednostavno.ipynb) i sljedeća cjelina [07. NLP — obrada tekstualnih podataka](07_nlp_tekst.md).

Vizualizacija je dio istraživačkog postupka, a ne ukras na kraju. Graf nam najprije služi da sami vidimo podatke — raspodjelu ocjena, razlike među žanrovima, odnos čitanja i odlazaka u kino — a potom ide u izvješće, gdje mora prenijeti nalaz čitatelju koji podatke nije vidio.

## Zašto vizualizacija?

"Grafikon vrijedi 1000 riječi" — dobra vizualizacija:

- otkriva obrasce koje tablice skrivaju
- komunicira rezultate publici
- je dio znanstvenog izvješća

Ljudsko oko brzo uočava razlike u dužini, položaju i obliku, a mnogo slabije uspoređuje desetke brojeva u tablici. Zato graf otkriva obrasce koje tablica skriva: dva vrha u raspodjeli ocjena, sezonski skok posjećenosti u vrijeme festivala ili skupinu ispitanika koja se ponaša posve drukčije od ostalih. Isti graf zatim služi komunikaciji — u seminarskom radu, na posteru ili u prezentaciji — a kao dio znanstvenog izvješća mora biti ponovljiv.

## Pravila dobre vizualizacije

1. **Jasne oznake** — naslov, osi, legenda
2. **Čitljiv font** — dovoljno velik
3. **Poštena skala** — ne zavaravaj osima
4. **Kontekst** — jedinice, izvori, broj opažanja
5. **Pravi tip grafa** — histogram za raspodjelu, scatter za odnos,
   bar za usporedbu, box za raspršenost

Uz tih pet pravila držimo se još tri navike. Prva je štedljivost: element koji ne nosi podatak (mreža, sjene, trodimenzionalni stupci) otežava čitanje. Druga je pristupačnost: crveno-zeleni par ne razlikuje oko pet do osam posto muškaraca, pa biramo paletu čitljivu i bez razlikovanja boja. Treća je potpunost: uz graf navodimo broj opažanja i izvor, a kod prosjeka pokažemo i raspršenost, jer prosjek sam ne otkriva koliko je podataka ni koliko su vrijednosti razbacane.

| Pogreška | Kako izgleda | Ispravak |
|----------|--------------|----------|
| Skraćena os | y-os počinje od 90 pa razlika izgleda deset puta veća | os počinje od nule ili je prekid označen |
| Preklopljene kategorije | stupci bez naziva i legende | čitljive oznake i sortiranje po vrijednosti |
| Graf bez konteksta | „posjećenost“ bez jedinice i razdoblja | naslov, jedinica i razdoblje mjerenja |
| Samo prosjek | jedan stupac bez raspršenosti | prikaz pojedinih opažanja ili raspodjele |
| Previše boja | sedam nijansi za sedam kategorija | do tri do četiri boje, ostalo oblikom ili redom |

## Vrste grafova

| Graf | Kada |
|------|------|
| Histogram | Raspodjela jedne varijable |
| Scatter | Odnos dviju numeričkih varijabli |
| Bar chart | Usporedba kategorija |
| Box plot | Raspršenost po grupama |
| Line chart | Trendovi kroz vrijeme |

| Graf | Pitanje na koje odgovara | Primjer iz kulture |
|------|--------------------------|--------------------|
| Histogram | kako su vrijednosti raspoređene | broj kino posjeta godišnje |
| Scatter | kreću li se dvije varijable zajedno | posjet muzeju i posjet kazalištu |
| Bar chart | koja je kategorija veća | broj programa po žanru |
| Box plot | koliko se skupine razlikuju | ocjena programa po dobi ispitanika |
| Line chart | raste li ili pada tijekom vremena | mjesečna posjećenost izložbe |

## Matplotlib + Seaborn

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.histplot(df["kino"], bins=8, color="#4fc3f7")
plt.title("Kino posjeti godišnje")
plt.xlabel("broj posjeta")
plt.show()
```

Matplotlib je osnovni sloj za crtanje, a Seaborn ga nadograđuje gotovim stilovima i funkcijama za statističke grafove. U jednom liku prikazujemo nekoliko pogleda na iste podatke.

```python
sns.set_theme(style="whitegrid", palette="colorblind")

fig, osi = plt.subplots(1, 2, figsize=(11, 4))

sns.scatterplot(x="posjeti_muzej", y="posjeti_kazaliste", data=df, ax=osi[0])
osi[0].set_title(f"Muzej i kazalište (n = {len(df)})")
osi[0].set_xlabel("posjeti muzeju godišnje")
osi[0].set_ylabel("posjeti kazalištu godišnje")

srednje = df.groupby("dobna_skupina")["ocjena_programa"].mean().sort_values()
osi[1].bar(srednje.index, srednje.values, color="#4fc3f7")
osi[1].set_title("Ocjena programa po dobnoj skupini")
osi[1].set_ylabel("prosječna ocjena (1–5)")

plt.tight_layout()
plt.savefig("kulturne_navike.png", dpi=200, bbox_inches="tight")
plt.show()
```

Graf u izvješću spremamo u datoteku visoke razlučivosti, a u tekstu ga popratimo opisom: što prikazuje, na kojem uzorku i iz kojeg izvora. Kod usporedbe skupina prikazujemo i nesigurnost procjene.

```python
sns.barplot(x="žanr", y="ocjena_programa", data=df, errorbar="ci", color="#81c784")
plt.xticks(rotation=45, ha="right")
plt.title("Ocjena programa po žanru (95% interval pouzdanosti)")
plt.ylabel("prosječna ocjena (1–5)")
plt.tight_layout()
plt.show()
```

Kod malih skupina interval pouzdanosti je širok, pa dva stupca koja izgledaju različito mogu biti posve podjednaka. Box plot istu informaciju pokazuje izravnije: kutija obuhvaća srednjih pedeset posto opažanja, a točke izvan nje upozoravaju na neobične vrijednosti.

```python
sns.boxplot(x="dobna_skupina", y="posjeti_muzej", data=df)
plt.title("Posjeti muzeju po dobnoj skupini")
plt.ylabel("broj posjeta godišnje")
plt.show()
```

## LLM u vizualizaciji

- LLM generira kod za graf iz opisa
- LLM interpretira graf (što vidimo?)
- LLM predlaže bolji tip grafa
- Uvijek provjeri: je li graf pošten?

Model dobro prevodi opis u kod, predlaže prikladniji tip grafa i opisuje što se na grafu vidi. Njegov opis ne zamjenjuje pogled na podatke: model ne provjerava je li os skraćena, je li uzorak malen ni je li naslov u skladu s prikazanim. Kod koji generira pročitaj prije pokretanja, provjeri na koje se stupce poziva i u izvješću navedi da je pomoćni alat korišten.

## Ishodi učenja (6)

- Kritički vrednovati rezultate, metode i tehnike analize podataka.

## Ključni pojmovi

| Pojam | Značenje |
|-------|----------|
| Histogram | raspodjela jedne numeričke varijable u razredima |
| Scatter | odnos dviju numeričkih varijabli |
| Bar chart | usporedba vrijednosti po kategorijama |
| Box plot | raspodjela po skupinama s medijanom i raspršenošću |
| Line chart | promjena kroz vrijeme |
| Poštena skala | os koja ne pretjeruje u prikazu razlika |
| Interval pouzdanosti | raspon unutar kojeg očekujemo pravu vrijednost |
| Čitljivost | font, oznake, kontrast i redoslijed kategorija |
| Pristupačnost | paleta i oblik čitljivi i osobama koje ne razlikuju boje |
| Kontekst | jedinice, razdoblje, broj opažanja i izvor podataka |

## Provjeri razumiješ

1. Zašto je graf s y-osom koja počinje od 90 zavaravajuć?
2. Kada ćemo za odnos dviju varijabli koristiti scatter, a kada bar chart?
3. Što nam graf sa samo prosječnim vrijednostima ne pokazuje?
4. Kako provjeravamo je li graf pošten prije nego ga uvrstimo u izvješće?

<details><summary>Odgovori</summary>

1. Oko procjenjuje razlike prema duljini stupca. Ako os počinje od 90, stupac s vrijednošću 92 izgleda mnogo viši od stupca s 91, iako je razlika jedan posjet. Poštena os počinje od nule ili je prekid skale jasno označen.

2. Scatter koristimo kada na obje osi imamo brojčane vrijednosti i zanima nas kreću li se zajedno, primjerice posjeti muzeju i posjeti kazalištu. Bar chart koristimo za usporedbu kategorija, primjerice broja programa po žanru, gdje kategorije nisu brojčane vrijednosti.

3. Ne pokazuje raspršenost. Dvije skupine mogu imati jednak prosjek, a posve različite raspodjele — jedna ujednačenu, druga s mnogo izrazito aktivnih i izrazito neaktivnih ispitanika.

4. Provjeravamo pet stvari: ima li graf naslov i označene osi s jedinicama, počinje li skala od nule, je li naveden broj opažanja i izvor, je li tip grafa primjeren pitanju i je li graf čitljiv i bez razlikovanja boja.

</details>

## Praktično

Povezana skripta i bilježnica: [`scripts/03_vizualizacija.py`](../scripts/03_vizualizacija.py), [`colab/DSK_analiza_upitnika_jednostavno.ipynb`](../colab/DSK_analiza_upitnika_jednostavno.ipynb).

- 🟢 Nacrtaj histogram broja kino posjeta iz ankete i u naslovu navedi broj opažanja.
- 🟢 Nacrtaj bar chart prosječne ocjene programa po žanru i sortiraj kategorije po vrijednosti.
- 🟡 Nacrtaj scatter posjeta muzeju i posjeta kazalištu, dodaj regresijsku liniju i u dvije rečenice opiši što se vidi.
- 🟡 Nacrtaj box plot ocjena po dobnoj skupini i provjeri postoje li skupine s premalenim uzorkom za zaključak.
- 🏆 Uzmi graf iz medijskog izvješća, procijeni je li pošten prema pet pravila dobre vizualizacije i nacrtaj ispravljenu verziju na istim podacima.

## Dalje

Tablične i brojčane podatke sada umijemo pripremiti, provjeriti i prikazati. U kulturi, međutim, najveći dio građe nije brojčan, nego tekstualan — članci, transkripti, arhivski opisi i kataloški zapisi. U cjelini [07. NLP — obrada tekstualnih podataka](07_nlp_tekst.md) prelazimo na sustavnu analizu teksta.

## Literatura

- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije: Razvoj velikih jezičnih modela i komunikacijskih agenata*. Rijeka: Filozofski fakultet u Rijeci. Open access: https://github.com/bperak/komunikacija_u_doba_ai
- Grus, J. (2019). *Data Science from Scratch*. O'Reilly.
- Bommasani et al. (2021). *On the Opportunities and Risks of Foundation Models*. arXiv:2108.07258
- Python za lingviste: https://github.com/nljubesi/python-for-linguists
- Matplotlib: https://matplotlib.org | Seaborn: https://seaborn.pydata.org
