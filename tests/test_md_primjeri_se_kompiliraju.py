"""Svaki Python blok u nastavnim markdown datotekama mora se kompilirati."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FENCE = re.compile(r"```python\n(.*?)```", re.S)


def _python_iz_bloka(sirovo):
    """Makni markdown navodnik oko ograđenog bloka i Colab naredbe.

    Redci koji počinju s ``!`` ili ``%`` jesu ljuska i magija bilježnice,
    ne Python. U tekstu ostaju za Colab; ovdje se izostavljaju da se
    ostatak bloka može provjeriti s ``compile``.
    """
    linije = []
    for linija in sirovo.splitlines():
        if linija.startswith("> "):
            linija = linija[2:]
        elif linija.startswith(">"):
            linija = linija[1:].lstrip()
        if linija.lstrip().startswith(("!", "%")):
            continue
        linije.append(linija)
    return "\n".join(linije) + "\n"


def python_blokovi():
    for mapa in ("content", "book"):
        for putanja in sorted((ROOT / mapa).rglob("*.md")):
            tekst = putanja.read_text(encoding="utf-8")
            for i, sirovo in enumerate(FENCE.findall(tekst), 1):
                yield putanja, i, _python_iz_bloka(sirovo)


class TestMdPrimjeriSeKompiliraju(unittest.TestCase):
    def test_svi_python_blokovi_se_kompiliraju(self):
        padovi = []
        broj = 0
        for putanja, i, blok in python_blokovi():
            broj += 1
            ime = f"{putanja.relative_to(ROOT)}#{i}"
            try:
                compile(blok, ime, "exec")
            except SyntaxError as greska:
                padovi.append(f"{ime}: {greska}")
        print(f"Python blokova: {broj}; padova: {len(padovi)}")
        self.assertEqual(padovi, [])
        self.assertGreater(broj, 0)


if __name__ == "__main__":
    unittest.main()
