# Pokazni podaci (`data/`)

Ova mapa sadrži **pokazne odgovore** na upitnik kolegija „Gdje se izlazi van u Rijeci".

| Datoteka | Što je |
|---|---|
| `demo_odgovori.csv` | 38 generiranih odgovora iste strukture kao pravi izvoz iz Google obrasca |

**Zašto pokazni podaci.** Bilježnice moraju raditi i prije nego što je itko ispunio obrazac (i kad nema interneta do prave tablice). Zato prvo pokušavaju dohvatiti **prave odgovore** iz objavljene tablice, pa `demo_odgovori.csv`, pa lokalnu datoteku, a na kraju sama generiraju pokazne odgovore. U svakom ispisu jasno piše odakle su podaci došli.

**Struktura stupaca** (isto kao izvoz iz obrasca):

| Stupac | Tip | Napomena |
|---|---|---|
| `Vremenska oznaka` | tekst | vrijeme ispunjavanja |
| `Gdje izlazite u Rijeci` | tekst | više odgovora u jednoj ćeliji, razdvojeni zarezom |
| `Dob` | broj kao tekst | u obrascu je zapisana kao tekst |
| `Koju glazbu slušate` | tekst | slobodan unos, razdvojen zarezima i točkama sa zarezom |
| `Uživam slušati narodnjake …` | 1–5 | tvrdnja iz mreže (grid) |
| `Slušam u slobodno vrijeme glazbu Jochana Sebastiana Bacha` | 1–5 | druga tvrdnja iz mreže |

**Pravi podaci.** Kad voditelj kolegija objavi tablicu s pravim odgovorima (*Responses → Link to Sheets* → *Publish to web* → CSV), u bilježnici se upiše samo ta poveznica i analiza se izvodi na stvarnim odgovorima. Pokazne podatke tada ne treba ni brisati — oni ostaju kao sigurnosna kopija za vježbu.

**Napomena o privatnosti.** Ovi pokazni podaci su generirani programski, ne sadrže ničije odgovore, imena ni adrese. Prave tablice i izvozi ostaju u vlasništvu kolegija i objavljuju se samo zbirno ili anonimizirano.
