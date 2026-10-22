# Playbook fase 2 (aggiornato 22/10)
Stato: fase 2 -338.98 dopo 9 sedute, 20 trade (7W/13L, 35%). Saldo 49663.88, minimo 48290.44, margine 1373.44. Scadenza 06/11: 11 sedute, servono ~31 $/giorno. 3 giorni positivi di fila.
RISCHIO: max 150 $/trade, perdita max giorno 200 $. Max 2 trade/giorno (3° solo se i primi 2 sono positivi e A+). Dopo 1 perdita: 1 solo altro trade con NUOVA struttura e rischio ≤100. Dopo 2 perdite STOP.

## ORDINE DI LAVORO PER OGNI TRADE
1) Direzione: gap >0.8% -> direzione del gap (5/6 giorni; mai contro prima delle 10:30). Gap <0.8% -> nessuna direzione: seguire SPY/SMH e la reazione ai livelli chiave.
2) FILTRO ASSOLUTO: SPY (meglio anche SMH) d'accordo. SPY a nuovi estremi opposti = NIENTE trade.
3) Filtro livello: niente ingresso con un livello chiave opposto a <1.5R dal fill. Valutarlo SUBITO con l'R reale, non aspettare la rottura del livello successivo.
4) Conferma: chiusura 5m oltre OR / VWAP / livello sweep / bordo compressione.
5) Ingresso: alla chiusura 5m che rompe il bordo di una compressione (se l'ultima 1m non è già estesa >0.5) OPPURE al primo retest/bandiera. Se la mossa ha già fatto >2R dal bordo: salto o aspetto un nuovo retest (22/10: entrato tardi = R grande, 1 MNQ, metà mossa persa).
6) Stop strutturale (oltre VWAP / swing / bandiera ±0.30, ±0.35 IEX). POI la taglia: stop ≤0.9 -> 2 MNQ; 0.9-1.8 -> 1 MNQ; >1.8 -> salto. Mai stringere.
7) Fill >0.3 peggio del segnale -> ricalcolo R; se rischio >150 chiudo subito.

## GESTIONE
- Senza target. Stop iniziale FERMO finché un 5m non CHIUDE oltre +2R.
- Dopo +2R: con 2 MNQ chiudo 1; stop oltre swing 5m che ha creato il nuovo estremo ±0.30 (≥ +0.5R).
- Livello target strutturale raggiunto + rallentamento (≥3 barre 5m ferme) senza +2R: con 2 MNQ chiudo 1; con 1 MNQ lascio stop originale (non micro-trail).
- Dopo 11:00: trail SOLO su max/min del range 30' ±0.50 o swing 5m ±0.50, e oltre lo swing PIÙ RECENTE (incluso il rimbalzo in corso). MAI spostare lo stop mentre il prezzo sta rimbalzando verso di esso. Mai swing 1m.
- Prima di ogni modify_stop: "quale regola autorizza questo stop?" Se nessuna -> non lo muovo.

## Setup attivi (priorità)
C. Sweep & reclaim / V-reversal su livello chiave con SPY forte, ingresso retest/bandiera. 2W/2L +427.
D. Compressione (≥3 test, minimi crescenti/max decrescenti) -> ingresso ALLA ROTTURA del bordo (chiusura 5m) o primo retest, dopo 10:00, SMH/SPY d'accordo. 2W +75 (con ingresso/trail giusti ~+120 e ~+500). Nei giorni di gap grande è il setup principale dopo il range iniziale.
5. Rottura range 1h dopo 10:30 con SPY a nuovi estremi DI SEDUTA, ingresso retest/bandiera.
A. Gap&go su retest: solo gap >0.8% e SPY d'accordo. 0W/2L.
E. (da provare, 1 MNQ) Range day dopo 10:00: fade al 3° test dell'estremo con barra di rifiuto, stop 0.5 oltre, target VWAP. Solo se SPY non rompe nel verso dell'estremo.
## Setup SOSPESI
Trappola->reverse immediato (0/5). Flip immediato dopo stop-out. Gap fade prima 10:30 (0/1). Long VWAP con LH (0/1). Short QQQ con SPY ai max (e viceversa).
