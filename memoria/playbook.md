# Playbook fase 2 (dal 12/10/2026)
Obiettivo: P&L fase 2 > 0 entro 06/11 (ora -97.52), senza bruciare. Margine 1614.90 (min 48290.44).
Rischio: 100-200 $/trade, perdita max giornaliera ~350 $ (poi stop giornata). Max 3 trade/giorno.
ORDINE DI LAVORO PER OGNI TRADE: 1) stop strutturale (oltre swing/sweep/retest + 0.30 per IEX) 2) distanza 3) taglia 4) se non sta nel budget -> niente trade. MAI stringere lo stop.
TAGLIA: stop ≤1.2 $ + chiusura 5m -> 2 MNQ. Stop 1.2-2.5 $ -> 1 MNQ (vincolante). A+ (SPY/SMH allineati + livello chiave) con stop ≤0.8 -> 3 MNQ.
Check prima di place_trade: stop_price == stop della tesi? taglia == regola?
PROTEZIONE GIORNATA: se ≥ +300 a 10:30 -> max 1 altro trade, solo A+, rischio ≤ 1/3 del profitto. Dopo 2 perdite: pausa 15 min, poi solo setup a favore del gap/trend.
Ordini: aprire SENZA target; uscita con modify_stop/close.
Gestione: a +1R pareggio (solo dopo chiusura 5m a +1R, non su spike 1m); trailing oltre swing 5m; lasciar correre fino a 11:30 se LH/LL (o HH/HL) regge.

## Setup (in ordine di resa)
2/C. Sweep & reclaim (min/max pre, ieri, OR): bucata + CHIUSURA 5m oltre il livello -> ingresso; stop 0.30 oltre estremo sweep. Mai anticipare su 1m. (13/10 +474; 14/10 -102 per stop troppo stretto)
A. Gap&go: chiusura 5m oltre estremo OR15 nella direzione del gap + lato giusto VWAP. Preferito nei giorni macro (14/10 era il trade del giorno: 736.8 -> 733.4).
1. ORB15 + VWAP: chiusura 5m oltre estremo range 9:30-9:45. Contro la direzione del gap in giorno di dato macro: evitare o 1 MNQ. Se barra di rottura >1.5 $: aspettare retest.
3. Trappola -> reverse: reclaim fallito -> rottura nell'altro verso, ingresso su retest rifiutato, stop SOPRA il massimo del retest +0.30. (12/10 +71; 13/10 e 14/10 persi per stop stretto)
4. Trend 2a ora: SOLO con HH/HL (o LH/LL) + pullback a VWAP con rifiuto. Long VWAP con massimi decrescenti VIETATO.
Nota: mossa principale 9:35-10:30; giorni di trend (14/10) continuano fino 11:30. Non usare zona di rumore.
