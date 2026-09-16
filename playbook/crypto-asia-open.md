# crypto-asia-open — Trend di domenica sera e lunedì (effetto apertura dell'Asia)
- **stato:** sperimentale | **asset:** BTC/USD (ETH/USD) | **finestra:** domenica 19:00 ET → lunedì
- **evidenza:** Concretum (2018-2025): il trend-following intraday su BTC rende soprattutto da domenica 19:00 ET per circa 24 ore (vedi `knowledge/strategie/crypto.md`).
- **condizioni:** trend rialzista in formazione domenica pomeriggio o sera (rottura del range del weekend con volume). Solo long.
- **ingresso:** il desk della domenica piazza uno stop_limit di acquisto GTC sopra il massimo del range del weekend, se la tesi regge.
- **stop:** protezione stop_limit GTC da inviare **subito dopo il fill**: la run del lunedì (CIO) verifica che il fill ci sia e invia lo stop se manca. Per ridurre il rischio, la dimensione va calcolata come se lo stop mancasse per alcune ore.
- **uscita:** lunedì sera o martedì (Closer o Coach) oppure al target.
- **nota:** un ingresso lasciato "in attesa" senza protezione automatica è un rischio. Se non si può gestire, meglio non usare questo setup.
