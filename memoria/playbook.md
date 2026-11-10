# Playbook fase 2 (aggiornato 10/11)
Stato: fase 2 -197.51 dopo 28 trade (10W/18L, 36%, PF 0.86). Saldo 49805.35, minimo 48290.44, margine 1514.91. Obiettivo: tornare positivi e crescere (~+50 $/giorno medi). Obiettivo 53000 lontano (mancano 3195): priorità = coerenza, non fretta.
RISCHIO: max 150 $/trade, perdita max giorno 200 $. Max 2 trade/giorno. Dopo 1 perdita: 1 solo altro trade, rischio ≤100, NUOVA struttura = almeno 15' dopo lo stop + chiusura 5m a nuovo estremo nel verso del trade (o direzione opposta con setup completo). Dopo 2 perdite STOP. Dopo vincente ≥+1.5R: 2° trade solo A+ con rischio ≤75.

## PRINCIPIO N.1 (dal 10/11)
Il problema non sono i setup: è violarli. ~1/3 dei trade ha violato un filtro scritto e spiega più dell'intera perdita. Se un filtro dice NO, il trade non esiste, anche se "sembra bello".

## I 4 SETUP
0. TREND OPEN-DRIVE (1W +239). Entro 9:45: gap ≥0.6% + 3 barre 5m con min crescenti + SPY/SMH a nuovi max (o simmetrico) + pullback 1m ≤1.3 $. Ingresso alla PRIMA bandiera 1m, stop sotto bandiera -0.30 (≤1.8 $, 1 MNQ). Nessun target: stop fermo fino a chiusura 5m oltre +2R, poi trail sotto swing 5m che hanno fatto nuovo estremo ≥1R, -0.50. Dopo 11:00 con MFE ≥3R: stop = estremo -1R (in prova).
1. C ALL'APERTURA (9:35-9:55). Sweep di livello chiave + 1-2 chiusure 5m di nuovo dentro, SPY che NON conferma. 1 MNQ (2 se stop ≤0.9), stop 0.30 oltre lo sweep IEX. Solo se stop ≤150 $ e livello opposto ≥1.5R.
2. ROTTURA RANGE/COMPRESSIONE 30-60' DOPO LE 10:15 (6W/4L, +178). SPY a nuovi estremi di seduta. Entrata entro 0.5 dal bordo. Stop oltre bandiera/swing interno +0.30. Stop ≤0.9 -> 2 MNQ; 0.9-1.8 -> 1; >1.8 salto. Target fisso = min(1.8R, livello strutturale -0.15).
3. GESTIONE: setup 0 = trail da +2R; setup 2 = target fisso. Prima di ogni modify_stop: "quale regola lo autorizza?". Mai spostare lo stop durante un rimbalzo verso di esso. Ultimi 5' -> chiudo a mano.

## CHECKLIST NELLA TESI (scritta, obbligatoria)
FILTRI DEL PIANO DI OGGI: [copia] -> SÌ/NO ciascuno. 1) Setup n° (0/1/2)? 2) SPY a nuovi estremi nel mio verso (non LH/HL contrari)? 3) Livelli tra ingresso e target ≥1.5R? 4) Stop STRUTTURALE (oltre VWAP/swing che ha generato la mossa) ≤ limite? 5) Ingresso entro 0.5 dal bordo? Un NO = niente trade.

## Filtri
- Gap >0.8% -> solo direzione del gap prima delle 10:30 (10/11: 2 long contro, -204). Gap <0.6% -> nessuna direzione.
- Gap riempito nei primi 30' e respinto sotto un livello di ieri + LH su QQQ e SPY = distribuzione: niente long.
- Niente short QQQ con SPY ai max (e viceversa). "Bandiera" valida solo se SPY tiene i max e QQQ non fa LH.
- Fill >0.3 peggio del segnale -> ricalcolo R; se >150 chiudo.
- Volatilità alta (barre 15m 3-6 $): sempre 1 MNQ.

## SOSPESI (non si fanno)
Trappola->reverse (0/5). Flip immediato dopo stop-out. Gap fade prima 10:30. Long/short al VWAP con struttura contraria (0/3, -322). Re-ingresso nella stessa zona <15' dopo uno stop.
