# opt-catalyst — Opzioni direzionali a rischio definito su catalizzatore
- **stato:** sperimentale | **asset:** opzioni (long call/put, debit spread verticali) | **finestra:** 09:45-11:00 ET (dopo che gli spread si sono stretti)
- **quando:** tesi da `orb-sip`, `gap-go` o `etf-noise`, ma l'azione costa troppo o lo stop tecnico è troppo largo.
- **scelta:** scadenza 0-7 DTE (0DTE solo su SPY/QQQ/IWM); delta della gamba lunga 0,40-0,60; debit spread con la gamba corta vicina al target del sottostante.
- **filtri:** spread bid/ask ≤ 10% (meglio ≤ 5%); open interest ≥ 500; IV non in fase di crush (evitare gli acquisti secchi il giorno dopo gli utili).
- **ingresso:** limit al mid, avvicinandosi al massimo di 2 tick.
- **rischio:** premio ≤ 8% dell'equity (mandato); la perdita massima è il premio.
- **uscita:** +50/+100% sul premio oppure alla condizione di invalidazione del sottostante (Position Manager); tutto chiuso entro le 15:50 (0DTE entro le 15:30).
- **da registrare:** DTE, delta, IV, spread %, prezzo eseguito rispetto al mid, R (sul premio).
