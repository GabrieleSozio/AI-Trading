# Fonti: valutazione empirica (Coach)

| fonte | uso | voto (+/−) | esempi (data, cosa) |
|---|---|---|---|
| Alpaca news | catalizzatori | – | – |
| Ricerca web premarket movers | scanner | – | – |
| Alpaca dati SIP (barre storiche) | prezzi di riferimento per il ledger | + | 2026-09-16: alle 16:16 ET le barre 1 min `feed=sip` coprivano l'intera sessione (391 barre 13:30Z-20:00Z) e la barra giornaliera era già chiusa. Attendibile per R, MAE/MFE e confronto con SPY. |
| Alpaca snapshots (`dailyBar`) | prezzo di chiusura | − | 2026-09-16: `GET /v2/stocks/snapshots?feed=sip` ha restituito `dailyBar` e `prevDailyBar` **null** dopo la chiusura. Usare `/v2/stocks/bars?timeframe=1Day` (affidabile) invece degli snapshot per i dati di fine giornata. |

**Nota.** Oggi non sono state usate né Alpaca news né ricerche web: nessuna run operativa ha girato, quindi i due voti restano vuoti in attesa del primo uso reale.
