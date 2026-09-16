# Account

- Broker: Alpaca, **paper trading**
- Capitale iniziale: 500 USD (da impostare alla creazione del conto paper)
- Data di partenza: da definire (la scrive il proprietario al primo avvio)
- Opzioni: livello 3 (default nei conti paper: acquisti, spread, multi-leg)
- Dati: piano Basic gratuito (azioni IEX in tempo reale, opzioni con feed "indicative", crypto)
- Credenziali: variabili d'ambiente `APCA_API_KEY_ID` e `APCA_API_SECRET_KEY` dell'ambiente cloud `ai-trading` (la sezione API credentials non è disponibile sull'account). Le chiavi sono solo paper.

## Benchmark di confronto
- SPY buy & hold, dalla data di partenza
- "Finestra di apertura" di SPY: rendimento 9:30-10:30 ET (misura se c'è un vantaggio nel momento, non solo nel mercato)
- I bot Python del proprietario, se ne verranno condivisi i risultati
