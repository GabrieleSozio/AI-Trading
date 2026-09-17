# Lezioni (memoria di lungo periodo)

Curata dal Coach. **Al massimo ~30 regole**: ogni nuova lezione ne sostituisce o ne accorpa una vecchia.
Formato: `- [L##] regola concreta — prova: n casi, date o trade_id — aggiunta YYYY-MM-DD`

## Esecuzione
- [L01] Le gambe di protezione di azioni ed ETF si inviano con `time_in_force: gtc`: con `day` scadono alla chiusura e la posizione resta scoperta se una routine salta — prova: Closer del 16/09/2026 interrotto a metà — aggiunta 2026-09-17
- [L02] Il nome del setup nei registri è l'id esatto della scheda di `playbook/`; le varianti vanno nelle note — prova: `vwap-reclaim-pullback` del 17/09/2026 — aggiunta 2026-09-17

## Selezione
_(vuoto)_

## Rischio
- [L03] Sotto i 2.000 USD di equity Alpaca rifiuta ogni short (403): le tesi ribassiste si eseguono con ETF inversi long (SH, PSQ, RWM) o put/put spread, altrimenti si rinuncia — prova: Trader del 17/09/2026, 2 tesi su 4 invalidate — aggiunta 2026-09-17
- [L04] Il conto NON ha vincolo di regolamento T+1 (è limited margin, e la PDT è stata abolita il 04/06/2026): lo stesso capitale si riusa più volte nello stesso giorno. Il limite è il capitale nominale, non il regolamento — prova: correzione dell'assunzione errata nel log del 17/09/2026 — aggiunta 2026-09-17

## Asset specifici
_(vuoto)_
