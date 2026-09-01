# 11. Agentski sustavi — automatizirani istraživač

**Kolegij:** Data Science u kulturi | 2026./2027.

## Što je agent?

**Agent** = LLM + alati + petlja:

1. **REASON** — razmisli što treba
2. **ACT** — pozovi alat (pretraga, račun, vizualizacija)
3. **OBSERVE** — promatraj rezultat
4. **ADJUST** — prilagodi i ponovi

Ovaj obrazac se zove **ReAct** (Reasoning + Acting, Yao et al. 2022).

## Primjer: istraživač baštine

Agent ima alate:
- `pretrazi(upit)` — muzejski katalog
- `statistika(stupac)` — deskriptivna analiza
- `raspodjela(stupac)` — frekvencije

Upit: "Kakva je raspodjela djela po zbirkama?" →
agent poziva `raspodjela("zbirka")` → interpretira rezultat.

## Google ADK

```python
from google.adk.agents import LlmAgent, LoopAgent
from google.adk.tools import FunctionTool

agent = LlmAgent(
    name="istrazivac",
    model="gemini-2.0-flash",
    tools=[FunctionTool(pretrazi), FunctionTool(statistika)],
    instruction="Pretraži katalog pa interpretiraj.",
)
petlja = LoopAgent(sub_agents=[agent], max_iterations=5)
```

## MCP (Model Context Protocol)

**MCP** = standard za povezivanje modela s alatima ("HTTP za AI alate").

```
Model → MCP klijent → MCP server (korpus, baza, API)
```

## Što agent može u kulturi?

- Automatski prikupiti podatke (API) → analizirati → izvijestiti
- Kombinirati katalog + statistiku + vizualizaciju u jednom tijeku
- Generirati nacrt istraživačkog izvješća

**⚠️ Uvijek provjeriti agentske rezultate — agent nije neovisan istraživač.**

## Ishodi učenja (8)

- Koristiti praktične vještine znanstvenih metoda digitalne humanistike.

## Praktično

Skripta: `scripts/08_agent_istrazivac.py`
