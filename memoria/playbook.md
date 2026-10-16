# Playbook fase 2 (dal 12/10/2026)
Obiettivo: P&L fase 2 > 0 entro 06/11 (ora -196.48 dopo 5 gg). Saldo 49806.38, minimo 48290.44, margine 1515.94.
Rischio: 100-200 $/trade, perdita max giornaliera ~300 $ (poi stop giornata). Max 3 trade/giorno.
ORDINE DI LAVORO PER OGNI TRADE: 1) stop strutturale (oltre swing/sweep/retest + 0.30 per IEX) 2) distanza 3) taglia 4) se non sta nel budget -> niente trade. MAI stringere lo stop (né all'ingresso né durante il trade).
TAGLIA: stop ≤1.2 $ + chiusura 5m -> 2 MNQ. Stop 1.2-2.5 $ -> 1 MNQ (vincolante). A+ (SPY/SMH allineati + livello chiave) con stop ≤0.8 -> 3 MNQ.
Check prima di place_trade: stop_price == stop della tesi? taglia == regola? SPY/SMH confermano la direzione? È a favore della direzione del gap/trend del giorno?
PROTEZIONE GIORNATA: se ≥ +300 a 10:30 -> max 1 altro trade, solo A+, rischio ≤ 1/3 del profitto. Dopo 2 perdite: stop giornata se perdita ≥ 250, altrimenti solo setup a favore del gap/trend.
Ordini: aprire SENZA target; uscita con modify_stop/close.

## GESTIONE (rivista 16/10) – LA PRIORITÀ N.1
- Stop iniziale FERMO finché un 5m non CHIUDE oltre +2R. Niente BE, niente trail su micro-swing prima.
- Dopo +2R (chiusura 5m): stop a +0.5R. Poi trail solo oltre swing 5m che hanno prodotto un nuovo estremo di ≥1R; in range laterale lo stop resta sopra/sotto VWAP o swing principale.
- Con 2+ MNQ: chiudere 1 a +2R, resto in trail.
- Uscita discrezionale solo su: livello strutturale opposto raggiunto + rallentamento, o chiusura 5m oltre VWAP contro.
- Lasciar correre fino a 11:30 se la struttura regge.

## DIREZIONE
- Direzione del gap = direzione 9:30-11:30 in 3/4 giorni (eccezione gap >1.2% dopo più giorni di calo). Default: trade solo a favore del gap/trend; flip solo se SPY E SMH fanno nuovi estremi DI SEDUTA nella nuova direzione e VWAP riconquistato.
- Dopo stop-out a favore del trend: re-ingresso nella stessa direzione (rottura del range a favore), non il flip.

## Setup (in ordine di resa)
2/C. Sweep & reclaim (min/max pre, ieri, OR): bucata + CHIUSURA 5m oltre il livello -> ingresso; stop 0.30 oltre estremo sweep. Mai anticipare su 1m. (13/10 +474)
A. Gap&go: chiusura 5m oltre estremo OR15 nella direzione del gap + lato giusto VWAP; stop sopra VWAP/LH +0.30. (14/10 e 16/10: trade del giorno, perso per gestione)
5. Rottura range 1h (dopo 10:30): chiusura 5m oltre estremo del range + SPY a nuovi max/min DI SEDUTA + SMH allineato + a favore del trend -> ingresso; stop sotto minimo barra di rottura -0.30. (15/10 +164; 16/10 -112 contro trend senza SPY)
3. Trappola -> reverse: solo al 1° test del livello, stop sopra max retest +0.30.
1. ORB15 + VWAP: contro gap in giorno macro evitare.
4. Trend 2a ora: solo HH/HL + pullback VWAP con rifiuto. Long VWAP con LH VIETATO.

## Settimana 2 (19-23/10)
Fase 2 -196.48: un trade gestito bene (+300) basta. 1 trade A/C a favore del gap al giorno, stop strutturale fermo fino a +2R. Massimo 1 trade extra, solo a favore del trend.
