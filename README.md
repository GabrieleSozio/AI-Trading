# AI-Trading

Una piccola "trading firm" composta solo da agenti AI (Claude, routine cloud), che opera su un conto **paper** Alpaca con capitale iniziale di circa 500 USD.
Nessuna logica deterministica decide i trade: le decisioni le prendono gli agenti. Il codice serve solo come calcolatrice e per recuperare i dati.

## Come funziona

| Ruolo | Quando (ET) | Cosa fa |
|---|---|---|
| CIO / Stratega | 08:40 | Legge macro, notizie e memoria; scrive il piano del giorno in `state/plans/` |
| Trader (+ Risk Officer) | 09:20-10:10 | Verifica le tesi con i dati live, sceglie lo strumento, esegue e protegge le posizioni |
| Position Manager | 11:30 | Gestisce le posizioni aperte e valuta nuove opportunità |
| Closer + Coach | 15:45-16:15 | Porta flat azioni, ETF e opzioni; scrive diario, metriche e lezioni |
| Desk crypto weekend | sab/dom | Gestisce le posizioni crypto (le uniche ammesse overnight e nel weekend) |

Gli orari e i fusi aggiornati sono in `config/schedule.md`.

## Mappa del repo

```
CLAUDE.md            regole operative comuni, lette automaticamente da ogni run
config/              limiti di rischio non negoziabili, orari, account
knowledge/           knowledge base di trading (per ruolo: vedi knowledge/00-indice.md)
playbook/            schede dei setup (vivi: il coach li promuove e li boccia)
state/               memoria e storico scritti dagli agenti
  ledger/            registri append-only (trade, equity, decisioni, previsioni, run)
  plans/ logs/       piano e log di ogni giornata
  journal/           consuntivo giornaliero
  reviews/           revisioni settimanali e mensili
  memory/            lezioni, fonti, statistiche del playbook
  risk-state.json    stato del rischio (livello di drawdown, blocco)
docs/                documenti di progetto e ricerca
```

## Principi

1. **Il mandato di rischio** (`config/risk-limits.md`) è l'unica cosa fissa. Lo modifica solo il proprietario.
2. **Tutto il resto lo decidono gli agenti**: asset, strumento, setup, timing, dimensione (entro i limiti), e anche se non tradare.
3. **Ogni decisione viene registrata** con motivazione e probabilità stimata, così si può misurare se il sistema migliora.
4. **Solo paper trading**: nessuna run chiama l'endpoint live.
