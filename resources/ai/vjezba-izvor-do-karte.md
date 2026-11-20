# Od izvora do karte: provjeri prije nego ucrtaš

Veze s kolegijem: [tablice](../../content/04_pandas_tablice.md), [vizualizacija](../../content/06_vizualizacija.md), [obrada teksta](../../content/07_nlp_tekst.md), [LLM alati](../../content/08_llm_alati.md), [RAG](../../content/10_rag.md) i [etika](../../content/12_etika_ai.md).

**Cilj:** usporediti dva načina ekstrakcije i odvojiti točnost podatka od kvalitete dokaza. Radi na jednom kratkom javnom dokumentu ili na odlomku ispod. Odlomak je izmišljen i nije povijesni izvor.

> U zapisniku od 12. svibnja 1910. navodi se da je društvo u Rijeci raspravljalo o izložbi. Za izložbu u Puli predložen je srpanj, ali datum nije potvrđen. Sljedeći sastanak održan je u Opatiji 4. lipnja 1910.

1. Ručno zapiši mjesto, događaj, datum ili razinu preciznosti, status i dokazni citat. Odvoji predloženu izložbu od održanog sastanka. Ne pretvaraj mjesec u izmišljeni dan.
2. Varijanta A: zatraži tablicu mjesta, događaja i datuma. Varijanta B: zatraži ista polja i doslovni citat za svaki redak, te oznake `potvrđeno`, `predloženo` ili `nepoznato`. Usporedi na istom ulazu i modelu; bez računa možeš ručno simulirati dvije obrade i označiti da nije riječ o testu modela.
3. Za svaku varijantu prijavi broj točnih od ukupno predloženih redaka te broj pronađenih od ukupno očekivanih. Odvojeno zabilježi podupire li citat tvrdnju; citat koji postoji nije nužno dokaz.
4. Ucrtaj samo provjerena mjesta. Ako prikazuješ planiranu izložbu, vizualno je razlikuj od održanih događaja. Svaka točka treba voditi do pripadnog retka i citata.

**Predaja:** dvije tablice, karta i kratka bilješka o pogrešci koja bi promijenila zaključak. Zabilježi izvor, verziju modela ako je korišten i pravilo po kojem su prihvaćeni zapisi.

[Povratak na katalog](README.md)
