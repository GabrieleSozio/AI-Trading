# Playbook fase 2 (dal 12/10/2026)
Obiettivo: P&L fase 2 > 0 entro 06/11 (ora -49.23 dopo 4 gg), senza bruciare. Saldo 49953.63, minimo 48290.44, margine 1663.19.
Rischio: 100-200 $/trade, perdita max giornaliera ~350 $ (poi stop giornata). Max 3 trade/giorno.
ORDINE DI LAVORO PER OGNI TRADE: 1) stop strutturale (oltre swing/sweep/retest + 0.30 per IEX) 2) distanza 3) taglia 4) se non sta nel budget -> niente trade. MAI stringere lo stop (né all'ingresso né durante il trade).
TAGLIA: stop ≤1.2 $ + chiusura 5m -> 2 MNQ. Stop 1.2-2.5 $ -> 1 MNQ (vincolante). A+ (SPY/SMH allineati + livello chiave) con stop ≤0.8 -> 3 MNQ.
Check prima di place_trade: stop_price == stop della tesi? taglia == regola? SPY/SMH confermano la direzione?
PROTEZIONE GIORNATA: se ≥ +300 a 10:30 -> max 1 altro trade, solo A+, rischio ≤ 1/3 del profitto. Dopo 2 perdite: pausa 15 min, poi solo setup a favore del gap/trend.
Ordini: aprire SENZA target; uscita con modify_stop/close.

## GESTIONE (rivista 15/10)
- Niente pareggio puro. A +1R: nulla. A +2R (su chiusura 5m): stop a +0.5R o oltre l'ultimo swing 5m (il più protettivo dei due che non sia a pareggio).
- Con 2+ MNQ: chiudere 1 a +2R, resto in trail.
- Livello strutturale opposto raggiunto (estremo del range, min/max chiave) + rallentamento -> chiudere tutto. In un range di 6 $ il target è l'altro lato del range, non "lasciar correre".
- Trail oltre swing 5m, mai su 1m. Lasciar correre fino a 11:30 se HH/HL (o LH/LL) regge e c'è trend.

## Setup (in ordine di resa)
2/C. Sweep & reclaim (min/max pre, ieri, OR): bucata + CHIUSURA 5m oltre il livello -> ingresso; stop 0.30 oltre estremo sweep. Mai anticipare su 1m. (13/10 +474; 14/10 -102 stop stretto)
5. Rottura range 1h (dopo 10:30): chiusura 5m oltre estremo del range + SPY a nuovi max/min + SMH allineato -> ingresso; stop sotto minimo barra di rottura -0.30; trail sotto minimi 5m crescenti. (15/10 +164)
A. Gap&go: chiusura 5m oltre estremo OR15 nella direzione del gap + lato giusto VWAP. Preferito nei giorni macro con gap medio (14/10). Con gap >1.2% dopo più giorni di calo: rischio rimbalzo, ridurre/aspettare.
3. Trappola -> reverse: reclaim fallito -> rottura nell'altro verso, ingresso su retest rifiutato, stop SOPRA il max del retest +0.30. SOLO al 1° test del livello. Al 2° test dello stesso estremo con SPY più forte = NON fare il fade (15/10 -111).
1. ORB15 + VWAP: chiusura 5m oltre estremo 9:30-9:45. Contro gap in giorno macro: evitare o 1 MNQ. Barra di rottura >1.5 $: aspettare retest.
4. Trend 2a ora: SOLO con HH/HL (o LH/LL) + pullback a VWAP con rifiuto. Long VWAP con massimi decrescenti VIETATO.
Nota: mossa principale 9:35-10:30 (13,14/10); 15/10 la mossa vera è arrivata dopo 10:40. Non usare zona di rumore.

## Venerdì 16/10
Fase 2 -49.23: basta un trade buono. Priorità: setup 2/C e 5, conferma SPY/SMH. 2 MNQ solo con stop ≤1.2. Perdita max giornata 350.
