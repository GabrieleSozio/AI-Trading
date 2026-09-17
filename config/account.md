# Account

- Broker: Alpaca, **paper trading**
- Capitale iniziale: 500 USD (da impostare alla creazione del conto paper)
- Data di partenza: da definire (la scrive il proprietario al primo avvio)
- Opzioni: livello 3 (default nei conti paper: acquisti, spread, multi-leg)
- Dati: piano Basic gratuito (azioni IEX in tempo reale, opzioni con feed "indicative", crypto)
- Credenziali: variabili d'ambiente `APCA_API_KEY_ID` e `APCA_API_SECRET_KEY` dell'ambiente cloud `ai-trading` (la sezione API credentials non è disponibile sull'account). Le chiavi sono solo paper.

## Cosa permette il conto oggi (17/09/2026)
- **Short su azioni ed ETF: no.** Serve un'equity di almeno 2.000 USD. Il lato ribassista si esprime con ETF inversi long o put.
- **Leva: no** (1x), per lo stesso motivo.
- **Day trading: libero.** La regola PDT non esiste più dal 4 giugno 2026 e il conto non ha vincoli di regolamento T+1: lo stesso capitale si riusa più volte al giorno.
- **Opzioni: livello 3** (acquisti e spread a rischio definito). **Crypto: solo long.**
- Vincolo reale: il **capitale nominale**. Con ~550 USD e titoli sopra i 100 USD si tiene in pratica una posizione per volta.
- Scheda completa con le fonti: `knowledge/dati/alpaca-conto-e-limiti.md`.

## Benchmark di confronto
- SPY buy & hold, dalla data di partenza
- "Finestra di apertura" di SPY: rendimento 9:30-10:30 ET (misura se c'è un vantaggio nel momento, non solo nel mercato)
- I bot Python del proprietario, se ne verranno condivisi i risultati
