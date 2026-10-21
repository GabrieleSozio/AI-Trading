# Playbook fase 2 (aggiornato 21/10)
Stato: fase 2 -351.68 dopo 8 sedute, 19 trade (6W/13L). Saldo 49651.18, minimo 48290.44, margine 1360.74. Scadenza 06/11: 12 sedute, servono ~30 $/giorno.
RISCHIO: max 150 $/trade, perdita max giorno 200 $. Max 2 trade/giorno (3° solo se i primi 2 sono positivi e A+). Dopo 1 perdita: 1 solo altro trade con NUOVA struttura e rischio ≤100. Dopo 2 perdite STOP.

## ORDINE DI LAVORO PER OGNI TRADE
1) Direzione: gap >0.8% -> direzione del gap (default, mai contro prima delle 10:30). Gap <0.8% -> nessuna direzione: seguire SPY/SMH e la reazione ai livelli chiave (close ieri, max/min ieri, PM min/max).
2) FILTRO ASSOLUTO: SPY (meglio anche SMH) d'accordo. SPY a nuovi estremi di seduta nel verso opposto = NIENTE trade.
3) Filtro livello: niente ingresso con un livello chiave opposto a <1.5R dal fill.
4) Conferma: chiusura 5m oltre OR / VWAP / livello sweep. Mai a mercato sulla barra di rottura.
5) Ingresso: RETEST (entro 0.5) con barra di rifiuto, OPPURE in bandiera. Controllo l'ultima barra 1m: se sta già rompendo -> aspetto (slip >0.5 già 3 volte).
6) Stop strutturale (oltre VWAP / swing / bandiera ±0.30, ±0.35 per IEX). POI la taglia: stop ≤0.9 -> 2 MNQ; 0.9-1.8 -> 1 MNQ; >1.8 -> salto. Mai stringere.
7) Dopo il fill: fill >0.3 peggio del segnale -> ricalcolo R; se rischio >150 chiudo subito.

## GESTIONE
- Senza target. Stop iniziale FERMO finché un 5m non CHIUDE oltre +2R (niente BE, niente micro-trail).
- Dopo +2R: con 2 MNQ chiudo 1 (close + riapro 1 con stop); stop sotto/sopra swing 5m che ha creato il nuovo estremo -0.30 (≥ +0.5R).
- Dopo 11:00 (ultimi 30'): trail SOLO su min/max del range 30' o swing 5m -0.50. MAI swing 1m (21/10: -55 $).

## Setup attivi (priorità)
C. Sweep & reclaim / V-reversal su livello chiave con SPY forte, ingresso retest/bandiera. 2W/2L +427. PRIMA SCELTA.
D. Compressione (≥3 test, minimi crescenti/max decrescenti) -> bandiera al bordo, dopo 10:30, SMH/SPY d'accordo. 1W +62 (con trail giusto ~+120).
5. Rottura range 1h dopo 10:30 con SPY a nuovi estremi DI SEDUTA, ingresso al retest/bandiera.
A. Gap&go su retest: solo gap >0.8% e SPY d'accordo. 0W/2L.
E. (da provare, 1 MNQ) Range day dopo 10:00: fade al 3° test dell'estremo con barra di rifiuto, stop 0.5 oltre, target VWAP. Solo se SPY non rompe nel verso dell'estremo.
## Setup SOSPESI
Trappola->reverse immediato (0/5). Flip immediato dopo stop-out. Gap fade prima 10:30 (0/1). Long VWAP con LH (0/1). Short QQQ con SPY ai max (e viceversa).
