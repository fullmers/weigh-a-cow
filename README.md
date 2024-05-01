# weigh-a-cow

## Installasjon
Vi anbefaler å bruke et virtuelt miljø for å installere bibliotekene som trengs for å kjøre koden.
Dette kan gjøres ved å kjøre følgende kommandoer:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Bytt eventuelt ut python3 med navnet på python-programmet (antageligvis `py` eller `python`) som er installert.


## Kjøring
For å kjøre koden, kjør følgende kommando:

```bash
flask --app hello run --debug
```

hvor hello er navn av fil hvor Flask appen er laget.

## Etter kjøring
For å gå ut av det virtuelle miljøet, kjør følgende kommando:

```bash
deactivate
```
