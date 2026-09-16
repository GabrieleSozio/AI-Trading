# Account

- Broker: Alpaca, **paper trading**
- Capitale iniziale: 500 USD (da impostare alla creazione del conto paper)
- Data di partenza: da definire (la scrive il proprietario al primo avvio)
- Opzioni: livello 3 (default nei conti paper: acquisti, spread, multi-leg)
- Dati: piano Basic gratuito (azioni IEX in tempo reale, opzioni con feed "indicative", crypto)
- Credenziali: iniettate dal proxy dell'ambiente cloud (header `APCA-API-KEY-ID` e `APCA-API-SECRET-KEY`) per `paper-api.alpaca.markets` e `data.alpaca.markets`

## Benchmark di confronto
- SPY buy & hold, dalla data di partenza
- "Finestra di apertura" di SPY: rendimento 9:30-10:30 ET (misura se c'è un vantaggio nel momento, non solo nel mercato)
- I bot Python del proprietario, se ne verranno condivisi i risultati
