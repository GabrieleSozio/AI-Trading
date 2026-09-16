# etf-noise — Uscita dalla "noise area" su ETF indice
- **stato:** sperimentale | **asset:** SPY/QQQ/IWM (o equivalenti a basso prezzo), ETF settoriali | **finestra:** dopo le 10:00 ET
- **evidenza:** Zarattini-Aziz-Barbon 2024, "Beat the Market" (vedi `knowledge/strategie/etf.md` §1).
- **calcolo:** per ogni minuto dall'apertura, media degli ultimi 14 giorni di |prezzo/apertura − 1| → banda = apertura × (1 ± quel valore); il lato superiore usa max(apertura, chiusura di ieri), quello inferiore min(apertura, chiusura di ieri). (Formulazione ripresa dal paper: da verificare sul testo originale prima di passare il setup a `in_prova`.)
- **ingresso:** prezzo fuori dalla banda a uno dei controlli (il paper controlla a intervalli regolari; per noi durante le run), nella direzione dell'uscita.
- **stop:** VWAP o bordo opposto della banda (il più vicino).
- **uscita:** trailing sul VWAP, flat entro le 15:50.
- **nota:** si calcola con le barre a 1 minuto (storico SIP) e con python. È anche un **filtro di regime** per gli altri setup.
