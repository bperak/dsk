"""Provjera da praktikum koristi aktualni Gemini SDK i bodovnik izvedbenog plana."""

import ast
import json
import os
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = os.environ.get(
    "DSK_PYTHON",
    "/home/bperak/development/jezikmisljenjekultura/.venv/bin/python",
)


def _oznaka(*dijelovi):
    """Spaja dijelove u izvođenju da se ugašeni naziv ne pojavi u bajtkodu."""
    return "".join(dijelovi)


# Sastavljeno da sama provjera ne sadrži ugašene identifikatore kao cjelinu.
ZABRANJENO = (
    _oznaka("google.", "generativeai"),
    _oznaka("gemini-2.0-", "flash"),
    _oznaka("text-embedding-", "004"),
)
PRAKTIKUM = [
    ROOT / "colab" / "DS_KULT_Podatkovna_znanost_u_kulturi.ipynb",
    ROOT / "README.md",
    ROOT / "projekt" / "UPUTE_PROJEKT.md",
    *sorted((ROOT / "scripts").glob("*.py")),
]
PORUKA_KLJUC = (
    "Ključ nije postavljen. Izradi ga na https://aistudio.google.com "
    "→ Get API key i zalijepi ga ovdje."
)
PORUKA_KVOTA = "Prekoračena kvota za minutu — pričekaj pa ponovi"


class MigracijaGeminiTest(unittest.TestCase):
    def test_praktikum_nema_ugasene_modele(self):
        pogoci = []
        for putanja in PRAKTIKUM:
            tekst = putanja.read_text(encoding="utf-8")
            for oznaka in ZABRANJENO:
                if oznaka in tekst:
                    pogoci.append(f"{putanja.relative_to(ROOT)}: {oznaka}")
        self.assertEqual(pogoci, [])

    def test_biljeznica_zadrzava_osam_cjelina(self):
        nb = json.loads(
            (ROOT / "colab" / "DS_KULT_Podatkovna_znanost_u_kulturi.ipynb").read_text()
        )
        self.assertEqual(len(nb["cells"]), 16)
        naslovi = []
        for celija in nb["cells"]:
            if celija["cell_type"] != "markdown":
                continue
            for redak in "".join(celija["source"]).splitlines():
                if redak.startswith("## ") and not redak.startswith("## Sadržaj"):
                    naslovi.append(redak)
        self.assertEqual(
            naslovi,
            [
                "## 0. Postavljanje",
                "## 1. AI revolucija u humanistici",
                "## 2. Podaci u kulturi: FAIR principi",
                "## 3. Pandas + LLM: razgovor s podacima",
                "## 4. Embedding: semantička pretraga kulturnih zbirki",
                "## 5. RAG: razgovor s kulturnom baštinom",
                "## 6. Agentski sustavi: automatizirani istraživač",
                "## 7. Etika i kritičko vrednovanje AI rezultata",
                "## 8. Vježbe",
            ],
        )
        uvod = "".join(nb["cells"][0]["source"])
        self.assertIn("vlastiti", uvod)
        self.assertIn("prije nastave", uvod)
        setup = "".join(nb["cells"][2]["source"])
        self.assertIn('MODEL = "gemini-3.5-flash"', setup)
        self.assertIn('EMB_MODEL = "gemini-embedding-2"', setup)
        self.assertIn("from google import genai", setup)
        self.assertIn("google-genai", setup)

    def test_ocjenjivanje_odgovara_izvedbenom_planu(self):
        tekst = (ROOT / "projekt" / "UPUTE_PROJEKT.md").read_text(encoding="utf-8")
        self.assertIn("| Pohađanje nastave | 1,5 | 0 |", tekst)
        self.assertIn("| Kontinuirana provjera znanja 1 | 1 | 30 |", tekst)
        self.assertIn("| Kontinuirana provjera znanja 2 (projekt) | 2,5 | 70 |", tekst)
        self.assertIn("| Završni ispit | 0 | 0 |", tekst)
        self.assertIn("| **UKUPNO** | **5** | **100** |", tekst)
        self.assertIn("varijanti bez završnog ispita", tekst)
        self.assertNotIn("| 1 | 20 |", tekst)
        self.assertNotIn("| 2,5 | 50 |", tekst)

    def test_readme_studij_i_sdk(self):
        tekst = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(
            "Sveučilišni prijediplomski studij Kulturologija (jednopredmetni)",
            tekst,
        )
        self.assertIn("google-genai", tekst)
        self.assertIn("google-adk", tekst)
        self.assertIn("po projektu", tekst)
        self.assertNotIn("Kulturalni studiji", tekst)

    def test_biljeznica_bez_kljuca_ispisuje_uputu(self):
        nb = json.loads(
            (ROOT / "colab" / "DS_KULT_Podatkovna_znanost_u_kulturi.ipynb").read_text()
        )
        izvor = "".join(nb["cells"][2]["source"])
        linije = [
            redak
            for redak in izvor.splitlines()
            if not redak.startswith("!") and not redak.startswith("postavi_kljuc()")
        ]
        # Stani na provjeri ključa: ne uvozi pandas ni ne zove API.
        odrezano = []
        for redak in linije:
            if redak.startswith("import pandas") or redak.startswith("from google import"):
                break
            odrezano.append(redak)
        program = "\n".join(odrezano) + "\npostavi_kljuc()\n"
        env = os.environ.copy()
        env.pop("GEMINI_API_KEY", None)
        rezultat = subprocess.run(
            [PY, "-c", program],
            input="",
            capture_output=True,
            text=True,
            env=env,
            cwd=ROOT,
        )
        self.assertIn(PORUKA_KLJUC, rezultat.stdout)
        self.assertNotIn("Traceback", rezultat.stderr)
        self.assertNotEqual(rezultat.returncode, 0)

    def test_kvota_429_ceka_i_ponavlja_najvise_dvaput(self):
        import importlib.util

        putanja = ROOT / "scripts" / "05_llm_analiza.py"
        spec = importlib.util.spec_from_file_location("llm_analiza", putanja)
        modul = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modul)

        pozivi = {"n": 0}
        spavanja = []

        class Kvota(Exception):
            code = 429

        def poziv():
            pozivi["n"] += 1
            raise Kvota("429")

        original = modul.time.sleep
        modul.time.sleep = lambda sekunde: spavanja.append(sekunde)
        try:
            with self.assertRaises(Kvota):
                modul.pozovi_model(poziv)
        finally:
            modul.time.sleep = original
        self.assertEqual(pozivi["n"], 3)
        self.assertEqual(spavanja, [5, 5])

    def test_skripte_se_sintaksno_prevode(self):
        for putanja in sorted((ROOT / "scripts").glob("*.py")):
            stablo = ast.parse(putanja.read_text(encoding="utf-8"), filename=str(putanja))
            self.assertIsInstance(stablo, ast.Module)
            tekst = putanja.read_text(encoding="utf-8")
            if putanja.name in {"05_llm_analiza.py", "06_semanticka_pretraga.py", "07_rag_kulturna_bastina.py"}:
                self.assertIn("def pozovi_model", tekst)
                self.assertIn(PORUKA_KVOTA, tekst)
            if putanja.name == "08_agent_istrazivac.py":
                self.assertIn('MODEL = "gemini-3.5-flash"', tekst)
                self.assertIn("LlmAgent", tekst)


if __name__ == "__main__":
    unittest.main()
