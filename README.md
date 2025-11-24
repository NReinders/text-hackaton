# Text Hackathon Project

Dit project is de basis voor onze 8-uur hackathon waarin we een gecombineerde oplossing bouwen met:

- Regex-gebaseerde rules
- Neuraal netwerk + embeddings
- LLM-API classificatie
- Ensemble/Orchestrator die deze drie samenvoegt

We gebruiken **uv** als package manager.

## Installatie

```bash
git clone https://github.com/NReinders/text-hackaton.git
cd text-hackathon
uv sync
```

## Projectstructuur

```text
text-hackathon/
├── data/
│   ├── raw/            # originele data (gedeeld in team)
│   └── processed/      # voorbewerkte data die anderen kunnen hergebruiken
├── models/             # gedeelde model-bestanden / weights
├── notebooks/          # exploratie en experimenten
├── src/
│   └── hackathon_text/
│       ├── regex_rules.py    # rule-based classifier
│       ├── nn_model.py       # embedding + klein neuraal netwerk
│       ├── llm_client.py     # LLM-api classificatie
│       ├── ensemble.py       # combineert regex + nn + llm
│       ├── data.py           # dataloading / preprocessing
│       ├── config.py         # instellingen per developer/experiment
│       └── run_experiment.py # hoofdcscript om alles bij elkaar te brengen
├── tests/              # basic tests (smoke tests)
├── main.py             # standaard uv entrypoint (niet essentieel)
└── pyproject.toml      # uv project configuratie
```
