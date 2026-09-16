# vwap-reclaim — Riconquista (o rifiuto) del VWAP
- **stato:** sperimentale | **asset:** azioni in play, ETF | **finestra:** 10:00-12:00 ET (Position Manager)
- **condizioni:** titolo in play che era sceso sotto il VWAP e lo **riconquista** con volume sopra la media (long); oppure lo **perde** e fallisce il retest (short).
- **ingresso:** chiusura di una barra a 5 minuti sopra (o sotto) il VWAP e rottura del suo massimo (o minimo).
- **stop:** dall'altra parte del VWAP, oltre il minimo o massimo dello swing.
- **uscita:** massimo o minimo del giorno, oppure 2R.
- **da registrare:** numero di tentativi sul VWAP, volume relativo della barra, R.
