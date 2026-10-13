# 11. Agentski sustavi — automatizirani istraživač

**Kolegij:** Data Science u kulturi | 2026./2027.

> **U ovoj cjelini.** Iz RAG asistenta (cjelina 10) prelazimo na agenta: model koji sam bira alate, izvodi ih u petlji i prilagođava postupak dok ne dođe do odgovora. Umjesto jednoga pitanja i jednoga odgovora, agent radi niz koraka — pretraži katalog, izračunaj statistiku, interpretiraj, predloži dalje.
>
> **Ishodi:** DSK-8
> - Koristiti praktične vještine znanstvenih metoda digitalne humanistike.
>
> **Uz ovu cjelinu idu:** skripta `scripts/08_agent_istrazivac.py`, bilježnica `colab/DS_KULT_Podatkovna_znanost_u_kulturi.ipynb` i cjelina 12 (Etika i kritičko vrednovanje AI rezultata).

## Što je agent?

**Agent** je veliki jezični model spojen s alatima i smješten u petlju. Model ne odgovara odmah, nego najprije odluči što mu treba, zatim to zatraži od alata i na kraju interpretira dobiveno. Petlja ima četiri koraka:

1. **REASON** — razmisli što treba
2. **ACT** — pozovi alat (pretraga, račun, vizualizacija)
3. **OBSERVE** — promatraj rezultat
4. **ADJUST** — prilagodi i ponovi

Ovaj obrazac se zove **ReAct** (Reasoning + Acting, Yao et al. 2022). Ključna razlika prema običnom upitu jest u tome što model ne mora sve znati unaprijed: rezultat jednoga alata određuje koji će se alat pozvati sljedeći.

| Korak | Što model čini | Primjer u istraživanju baštine |
|-------|----------------|-------------------------------|
| REASON | Odlučuje koju informaciju mu nedostaje | „Trebam vidjeti koje su zbirke u katalogu" |
| ACT | Poziva alat s konkretnim parametrima | `raspodjela("zbirka")` |
| OBSERVE | Čita vraćeni rezultat | Tablica s brojem djela po zbirci |
| ADJUST | Odlučuje sljedeći korak ili zaključuje | „Grafika je najmanja zbirka — provjerimo raspon godina" |

**Mali primjer.** Na upit „Kakva je raspodjela djela po zbirkama?" agent ne pogađa iz pamćenja, nego poziva alat `raspodjela("zbirka")`, dobiva tablicu frekvencija i tek je onda tumači u kontekstu povijesti umjetnosti.

## Primjer: istraživač baštine

Agent ima alate, a svaki alat je obična Python funkcija s jasnim ulazom i izlazom. Model ne vidi kod, vidi samo opis funkcije i njezin rezultat.

- `pretrazi(upit)` — muzejski katalog
- `statistika(stupac)` — deskriptivna analiza
- `raspodjela(stupac)` — frekvencije

| Alat | Ulaz | Izlaz | Kada ga agent koristi |
|------|------|-------|-----------------------|
| `pretrazi` | riječ ili naziv zbirke | zapisi iz kataloga | kad treba pronaći pojedina djela |
| `statistika` | naziv brojčanog stupca | srednja vrijednost, raspon, kvartili | kad pita o starosti ili rasponu godina |
| `raspodjela` | naziv kategoričkog stupca | frekvencije po kategoriji | kad pita o sastavu zbirke |

Upit: „Kakva je raspodjela djela po zbirkama?" → agent poziva `raspodjela("zbirka")` → interpretira rezultat.

```python
def pretrazi(upit: str) -> str:
    """Pretražuje katalog po nazivu djela ili zbirci."""
    zapisi = [
        {"naziv": "Pejzaž Kvarnera", "zbirka": "Grafika", "godina": 1915},
        {"naziv": "Luka Rijeka", "zbirka": "Fotografija", "godina": 1900},
        {"naziv": "Portret ribara", "zbirka": "Moderna", "godina": 1920},
    ]
    rezultat = [z for z in zapisi if upit.lower() in z["naziv"].lower()
                or upit.lower() in z["zbirka"].lower()]
    if not rezultat:
        return "Nema rezultata u katalogu."
    return "\n".join(f"{z['naziv']} ({z['zbirka']}, {z['godina']})" for z in rezultat)


def raspodjela(zapisi, stupac: str = "zbirka") -> str:
    """Frekvencije kategoričkog stupca."""
    brojevi = {}
    for zapis in zapisi:
        brojevi[zapis[stupac]] = brojevi.get(zapis[stupac], 0) + 1
    return "\n".join(f"{k}: {v}" for k, v in sorted(brojevi.items()))
```

## Google ADK

**Google ADK** (*Agent Development Kit*) je okvir koji od navedenih dijelova sastavlja agenta: model, alati, uputa i petlja. U nastavi se koristi paket `google-adk`.

```python
from google.adk.agents import LlmAgent, LoopAgent
from google.adk.tools import FunctionTool

MODEL = "gemini-3.5-flash"
agent = LlmAgent(
    name="istrazivac",
    model=MODEL,
    tools=[FunctionTool(pretrazi), FunctionTool(statistika)],
    instruction="Pretraži katalog pa interpretiraj.",
)
petlja = LoopAgent(name="petlja", sub_agents=[agent], max_iterations=5)
```

| Dio | Čemu služi | Napomena za nastavu |
|-----|------------|---------------------|
| `LlmAgent` | Agent s modelom, alatima i uputom | Ime agenta i `instruction` određuju ponašanje |
| `FunctionTool` | Pretvara Python funkciju u alat koji model može pozvati | Dokstring funkcije postaje opis alata |
| `LoopAgent` | Ponavlja korake do ispunjenja ili do granice | `max_iterations` sprečava beskonačnu petlju |
| `MODEL` | Naziv modela | `gemini-3.5-flash`, uz provjeru popisa aktualnih modela |

Ako paket `google-adk` nije dostupan, isti se obrazac može zapisati pseudokodom, bez poziva modela:

```
ponovi najviše 5 puta:
    odluka = model(upit, povijest_koraka, popis_alata)
    ako je odluka "gotovo": prekini
    rezultat = izvrsi(odluka.alat, odluka.parametri)
    povijest_koraka.dodaj(odluka, rezultat)
```

## MCP (Model Context Protocol)

**MCP** = standard za povezivanje modela s alatima („HTTP za AI alate"). Umjesto da svaki program ima vlastiti način povezivanja alata, MCP propisuje zajednički jezik: model traži alat, server ga izvršava i vraća rezultat.

```
Model → MCP klijent → MCP server (korpus, baza, API)
```

| MCP komponenta | Uloga | Primjer u baštini |
|----------------|-------|-------------------|
| Klijent | Šalje zahtjev za poziv alata | Program u kojem radi agent |
| Server | Izvršava alat nad stvarnim podacima | Poslužitelj nad muzejskim katalogom |
| Resurs | Podatak koji se može čitati | Inventarni zapis, transkript, snimka |
| Alat | Radnja s parametrima | Pretraga, statistika, izrada grafa |

**Mali primjer.** Ustanova izlaže jedan MCP server nad svojim katalogom i bazom fotografija. Ista ta veza tada služi svakome agentu — istraživačkom, izložbenom i onome za odgovore publici. Alat se ne prepisuje, nego se dijeli.

## Što agent može u kulturi?

- Automatski prikupiti podatke (API) → analizirati → izvijestiti
- Kombinirati katalog + statistiku + vizualizaciju u jednom tijeku
- Generirati nacrt istraživačkog izvješća

| Zadatak | Tijek rada agenta | Ljudska provjera koja ostaje |
|---------|-------------------|------------------------------|
| Prikupljanje | Dohvat zapisa iz API-ja i spremanje u tablicu | Jesu li polja ispravno prepoznata? |
| Analiza | Statistika i grafovi nad podacima | Je li odabrana mjera primjerena? |
| Izvješće | Nacrt teksta s nalazima | Jesu li tvrdnje potkrijepljene podacima? |

**Mali primjer.** Agent dobije zadatak „pripremi pregled zastupljenosti zbirki". Sam pozove `raspodjela("zbirka")`, zatim `statistika("godina")`, sastavi kratki nacrt i predloži izradu grafa. Istraživač potom provjerava je li zbirka „Fotografija" doista najmlađa i piše završno tumačenje.

**⚠️ Uvijek provjeriti agentske rezultate — agent nije neovisan istraživač.**

Agentski sustav može pogriješiti u svakom koraku: odabrati pogrešan alat, poslati pogrešan parametar, pročitati rezultat kao da govori nešto što ne govori, ili ponavljati isti korak dok ne potroši vrijeme. Zato se u izvješću uvijek navodi koji su alati pozvani i s kojim parametrima, a svaka brojka provjerava se izvan agenta.

## Ishodi učenja (8)

- Koristiti praktične vještine znanstvenih metoda digitalne humanistike.

| Ishod | Kako se ostvaruje u ovoj cjelini |
|-------|----------------------------------|
| Znanstvene metode (8) | Definiranje alata, vođenje zapisa o pozivima i provjera rezultata izvan agenta |

## Ključni pojmovi

| Pojam | Značenje |
|-------|----------|
| Agent | Model s alatima u petlji koji sam bira sljedeći korak |
| Alat | Funkcija s jasnim ulazom i izlazom koju model može pozvati |
| ReAct | Obrazac razmisli — djeluj — promatraj — prilagodi |
| Petlja | Ponavljanje koraka do rješenja ili do zadane granice |
| Uputa (instruction) | Tekst koji određuje ulogu i pravila ponašanja agenta |
| ADK | Okvir za sastavljanje agenata (model, alati, petlja) |
| MCP | Standard za povezivanje modela s alatima i podacima |
| Trag izvršavanja | Zapis pozvanih alata i parametara, osnova za provjeru |
| Nacrt izvješća | Prvi tekst koji agent predlaže, a istraživač provjerava |

## Provjeri razumiješ

**1. Koja je razlika između RAG asistenta i agenta?**

<details><summary>Odgovori</summary>

RAG asistent na jedno pitanje dohvati dokaze i napiše odgovor; tijek je unaprijed zadan. Agent sam odlučuje koji će alat pozvati, u kojem redoslijedu i kada je završio, pa se broj koraka razlikuje od upita do upita.

</details>

**2. Zašto `FunctionTool` traži funkciju s jasnim ulazom i izlazom?**

<details><summary>Odgovori</summary>

Zato što model bira alat prema njegovu opisu i zadaje parametre, a rezultat mora moći pročitati kao tekst. Ako funkcija vraća nestrukturiran ili višeznačan izlaz, model ga pogrešno tumači i pogrešno nastavlja petlju.

</details>

**3. Čemu služi `max_iterations` u `LoopAgent`?**

<details><summary>Odgovori</summary>

To je gornja granica broja koraka. Bez nje agent može ponavljati isti alat ili izmjenjivati dva alata bez napretka, trošeći vrijeme i kvotu poziva modela.

</details>

**4. Zašto se u izvješću navodi trag izvršavanja agenta?**

<details><summary>Odgovori</summary>

Da bi čitatelj mogao provjeriti odakle svaka brojka dolazi: koji je alat pozvan, s kojim parametrima i što je vratio. Bez traga izvršavanja agentski je rezultat neprovjerljiv, a time i znanstveno neupotrebljiv.

</details>

## Praktično

- 🟢 Pokreni `scripts/08_agent_istrazivac.py` i pročitaj izlaz demonstracije alata bez modela. Zatim u bilježnici `colab/DS_KULT_Podatkovna_znanost_u_kulturi.ipynb` ponovi iste pozive nad katalogom.
- 🟡 Dodaj četvrti alat (na primjer `raspon_godina(zbirka)`) i napiši njegov opis u dokstringu. Provjeri u trag izvršavanja poziva li ga agent kada je pitanje o starosti zbirke.
- 🏆 Zamisli agenta za svoju projektnu domenu: navedi tri do pet alata s ulazima i izlazima, uputu agenta i pravila provjere rezultata. Nacrt prenesi u metodologiju seminarskoga rada i jasno navedi što je radio agent, a što istraživač.

## Dalje

Sljedeća cjelina, **12. Etika i kritičko vrednovanje AI rezultata**, zatvara krug: kako prepoznati halucinaciju, pristranost korpusa i neprovjerenu brojku, te kako se u seminarskom radu navodi upotreba AI alata.

## Literatura

- Perak, B. (2025). *Komunikacija u doba umjetne inteligencije: Razvoj velikih jezičnih modela i komunikacijskih agenata*. Rijeka: Filozofski fakultet u Rijeci. https://github.com/bperak/komunikacija_u_doba_ai
- Yao, S. et al. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv:2210.03629
- Google ADK: https://adk.dev
- Grus, J. (2019). *Data Science from Scratch*. O'Reilly.
