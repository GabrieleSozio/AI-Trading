# Registro delle decisioni di progetto

| Data | Decisione | Motivo |
|---|---|---|
| 16/09/2026 | Routine cloud (non locali), piano Pro (5 run al giorno) | nessuna dipendenza dal PC; limite giornaliero di run |
| 16/09/2026 | Flusso completamente AI: il codice solo come calcolatrice e fonte dati | requisito del proprietario |
| 16/09/2026 | Ricerca e trading su Opus 5 (CIO, Trader, Position Manager, Risk Officer) | qualità del ragionamento |
| 16/09/2026 | Multi-asset: azioni, ETF, opzioni, crypto | l'AI sceglie lo strumento migliore |
| 16/09/2026 | Rischio per trade variabile, deciso dall'AI, con tetti tecnici larghi e circuit breaker a livelli | requisito del proprietario più protezione da errori gravi |
| 16/09/2026 | Nessuna posizione overnight o nel weekend, **tranne le crypto** | requisito del proprietario |
| 16/09/2026 | Desk crypto leggero sabato e domenica | gestire le crypto rimaste aperte |
| 16/09/2026 | Repo GitHub `AI-Trading` come memoria condivisa e storico | le routine cloud non vedono il PC |
| 16/09/2026 | Mezze giornate: il Position Manager chiude l'intraday | il Closer delle 15:45 arriverebbe dopo la chiusura delle 13:00 |
| 16/09/2026 | Blocco a −25% dal massimo con riduzioni progressive a −10% e −15% (vedi simulazioni) | distingue un sistema buono da uno cattivo senza fermare quello buono per puro rumore |

## Da fare prima del primo avvio
- [ ] Nuovo conto paper Alpaca da 500 USD e chiavi API
- [ ] Ambiente cloud dedicato: API credentials (header Alpaca) + rete Custom (domini in `knowledge/dati/fonti-dati.md`) + setup script
- [x] Prompt delle routine (`routines/`, 16/09/2026)
- [x] Guida di setup (`docs/04-setup-ambiente-e-routine.md`)
- [ ] Creazione delle routine con il repo `AI-Trading` come fonte, modello Opus 5 dove previsto
- [ ] Prima run manuale di test ("Run now") a mercato chiuso, poi una a mercato aperto
