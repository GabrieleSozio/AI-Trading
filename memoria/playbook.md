# Playbook fase 2 (dal 12/10/2026)
Obiettivo: P&L fase 2 > 0 entro 06/11, senza bruciare. Margine 2000 $ (min 48290.44).
Rischio: 100-250 $/trade, perdita max giornaliera ~400 $ (poi stop giornata). Max 3 trade/giorno.
TAGLIA: stop ≤1.2 $ QQQ + conferma chiusura 5m -> 2 MNQ. Stop 1.2-2.5 $ -> 1 MNQ. A+ (SPY/SMH allineati + livello chiave) con stop ≤0.8 -> 3 MNQ.
PROTEZIONE GIORNATA: se ≥ +300 a 10:30 -> max 1 altro trade, solo A+, rischio ≤ 1/3 del profitto del giorno. Non restituire più del 30%.
Ordini: aprire SENZA target (stop bracket non modificabile); uscita con modify_stop/close.
Stop: quello scritto nella tesi = quello inviato. Sempre strutturale (oltre swing 5m/VWAP/sweep), mai "di comodo" più stretto.
Gestione: a +1R pareggio; trailing solo oltre swing 5m; lasciar correre fino a 11:30 se struttura 5m regge.

## Setup (in ordine di resa)
2/C. Sweep & reclaim (min/max pre, ieri, OR): bucata e CHIUSURA 5m oltre il livello -> ingresso; stop oltre estremo sweep. Mai anticipare su 1m. (13/10: +474 con 2 MNQ)
1. ORB15 + VWAP: chiusura 5m oltre estremo range 9:30-9:45, lato giusto del VWAP. Stop oltre swing 5m interno.
3. Trappola -> reverse: reclaim fallito -> rottura nell'altro verso. Stop SOPRA VWAP/swing, non a ridosso della barra di rottura. Se la barra di rottura è estesa (>1 $), aspettare il retest. (12/10 +71; 13/10 -46 per stop stretto)
4. Trend 2a ora: SOLO se HH/HL a 5m in corso (o LH/LL per short) + pullback a VWAP con rifiuto. Con massimi decrescenti il long su VWAP è VIETATO. (13/10 -118 violando questa condizione)
Nota: mossa principale 9:35-10:30 (2/2 giorni). Dopo 10:30: meno taglia, solo struttura chiara.
Non usare zona di rumore.
