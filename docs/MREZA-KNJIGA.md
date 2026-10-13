# Mreža triju knjiga — mjesto ovog kolegija/materijala u njoj

Ovi materijali nisu samostalan projekt: dio su mreže triju knjiga autora.

| knjiga | pitanje na koje odgovara | vlasništvo (kanonski tamo) |
|---|---|---|
| *Komunikacija u doba umjetne inteligencije* (2025) | **što se dogodilo** | povijest komunikacije, arhitektura i obuka LLM-a, promptanje, RAG, agentura |
| **Data Science u kulturi** (ovi materijali) | **kako se mjeri** | podaci i FAIR, Python/Colab, pandas, statistika, vizualizacija, NLP, ugrađivanja, semantička pretraga, RAG, agentski sustavi |
| *Razine i entiteti: ontologija komunikacije u doba umjetne inteligencije* (u izradi) | **gdje to ontološki stoji** | sustavi i razine (OMLCC), emergencija, komunikacija kao razina, model kao novi entitet |

**Pravilo vlasništva:** tema ima jednog vlasnika — knjigu u kojoj je izložena najpotpunije. Ostale knjige ne objašnjavaju temu iznova, nego upućuju (↗).

## Gdje je što (upute iz ontološke knjige prema ovim materijalima)

| ontološka knjiga | ↗ ovdje | čemu |
|---|---|---|
| 1 (razina, svojstvo) | [05 Statistika i korelacije](../content/05_statistika.md) | kako se mjeri ono što nazivamo svojstvom razine |
| 1 (artefakt mjere) | [06 Vizualizacija](../content/06_vizualizacija.md) | zašto graf može stvoriti dojam skoka |
| 3 (mreža → vektor) | [09 Embedding i semantička pretraga](../content/09_embedding_pretraga.md) | postupak kojim se mreža prevodi u vektore |
| 6 (mreže značenja) | [07 NLP obrada teksta](../content/07_nlp_tekst.md) | priprema korpusa i osnovne mjere |
| 10 (mjere i njihove granice) | [12 Etika i kritičko vrednovanje AI](../content/12_etika_ai.md) | kako se mjere čitaju i gdje zavaravaju |
| 13–14 (agenti) | [11 Agentski sustavi](../content/11_agenti.md) | praktični agentski sustavi kao građa za analizu |

## Kako je ovaj repozitorij složen

| Razina | Gdje | Čemu služi |
|---|---|---|
| nastavna jedinica (45 min) | [`content/`](../content/) | čitanje, provjera znanja, zadaci 🟢🟡🏆 |
| kod koji se pokreće | [`scripts/`](../scripts/), [`colab/`](../colab/) | isti postupak u skripti i u bilježnici |
| kolegij kao cjelina | [`docs/IZVEDBENI-PLAN.md`](IZVEDBENI-PLAN.md) | moduli, ishodi, tjedni, ocjenjivanje |
| studentsko istraživanje | [`projekt/`](../projekt/) | od teme do seminarskog rada |
| knjiga | [`book/`](../book/KNJIGA_PLAN.md) | cjelovit tekst koji raste iz kolegija |

Ista tema postoji na dvije razine dubine: **cjelina** je nastavna jedinica s ishodima i zadacima, **poglavlje knjige** je cjelovit tekst s teorijskim okvirom i raspravom. Cjeline ne prepisuju knjigu — najavljuju je i upućuju na nju.

## Kanonski izvori mreže

- **Registar pojmova za sve tri knjige** (jedan izvor istine): https://github.com/bperak/OntologijaKomunikacijeUDobaAI/blob/main/pojmovnik/koncepti.yaml
- **Formati citiranja sve tri knjige** (APA 7, Chicago, MLA, BibTeX): https://github.com/bperak/OntologijaKomunikacijeUDobaAI/blob/main/docs/CITIRANJE.md
- **Podjela posla i pravila mreže**: https://github.com/bperak/OntologijaKomunikacijeUDobaAI/blob/main/docs/MREZA-KNJIGA.md

## Kako citirati ove materijale

> Perak, B. (2026). *Data Science u kulturi — materijali kolegija* (Sveučilišni prijediplomski studij Kulturologija, Filozofski fakultet u Rijeci). https://github.com/bperak/dsk

```bibtex
@misc{perak_dsk_materijali,
  author = {Perak, Benedikt},
  title  = {Data Science u kulturi — materijali kolegija},
  year   = {2026},
  note   = {Sveučilišni prijediplomski studij Kulturologija, Filozofski fakultet u Rijeci},
  url    = {https://github.com/bperak/dsk}
}
```

Kad knjiga *Data Science u kulturi* bude objavljena, citat se dopunjuje izdavačem, godinom i ISBN-om.
