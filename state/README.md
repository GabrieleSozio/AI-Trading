# Stato e storico

Qui scrivono gli agenti. Tutto è versionato su git, quindi ogni modifica resta nello storico dei commit.

- `ledger/`: registri append-only (schemi in `ledger/SCHEMA.md`)
- `plans/YYYY-MM-DD.md`: piano del CIO
- `logs/YYYY-MM-DD.md`: log operativo di Trader, Position Manager e Closer (in append, una sezione per run)
- `journal/YYYY-MM-DD.md`: diario del Coach
- `reviews/weekly/`, `reviews/monthly/`: revisioni periodiche
- `memory/`: lezioni, statistiche del playbook, valutazione delle fonti
- `risk-state.json`: stato dei circuit breaker (aggiornato dal Coach; il reset da `shadow` è solo manuale)
