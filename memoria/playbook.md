# Playbook fase 2 (aggiornato 20/10)
Obiettivo: P&L fase 2 > 0 entro 06/11 (ora -442.96 dopo 7 gg, mancano 13 gg). Saldo ~49559.90, minimo 48290.44, margine ~1270.
RISCHIO: max 150 $/trade, perdita max giornaliera 200 $; dopo 1 perdita: 1 solo altro trade con NUOVA struttura; dopo 2 perdite STOP. Max 2 trade/giorno.
Serve: 1-2 trade buoni a +2/+3R. Pochi trade, entrate migliori, stop fuori dal rumore.

## ORDINE DI LAVORO PER OGNI TRADE
1) Direzione: gap >0.8% -> direzione del gap (default). Gap <0.5% -> direzione NON data: seguire SPY/SMH e la reazione ai livelli chiave (close ieri/ven, PM min/max).
2) FILTRO ASSOLUTO: SPY (e possibilmente SMH) nella stessa direzione. SPY a nuovi estremi di seduta nel verso opposto = NIENTE trade.
3) Conferma: chiusura 5m oltre OR / VWAP / sweep reclaim -> NON entro a mercato sulla barra di rottura.
4) Ingresso: RETEST del livello/VWAP (entro 0.5) con barra di rifiuto, OPPURE dentro la bandiera/consolidamento successivo (stop sotto la bandiera -0.30) se il retest non arriva.
5) Stop oltre VWAP / swing di ritracciamento / bandiera +0.30. Mai sotto la sola barra di rottura.
6) Taglia: stop ≤1.0 -> 2 MNQ (rischio ≤150); 1.0-1.8 -> 1 MNQ; >1.8 -> salto. Mai stringere lo stop.
7) Check: stop == tesi? fill entro 0.3? SPY/SMH d'accordo?

## GESTIONE
- Stop iniziale FERMO finché un 5m non CHIUDE oltre +2R. Niente BE, niente micro-trail.
- Dopo +2R: stop sotto/sopra lo swing 5m che ha generato il nuovo estremo -0.30 (almeno +0.5R). Con 2 MNQ chiudo 1 a +2R.
- Ultimi 30 min (dopo 11:00): trail sul min/max del range di 30' (20/10 ok).
- Aprire SENZA target.

## Setup attivi
A. Gap&go su retest (solo gap >0.8% e SPY d'accordo).
C. Sweep & reclaim / V-reversal su livello chiave (close ieri/ven, PM min) con SPY forte: ingresso al retest o in bandiera, stop sotto sweep/bandiera. (13/10 +474; 20/10 +149) MIGLIOR SETUP.
5. Rottura range 1h (dopo 10:30) a favore del trend con SPY a nuovi estremi di seduta: ingresso al retest del bordo.
## Setup SOSPESI
Trappola->reverse immediato a mercato (0/5). Flip immediato dopo stop-out senza nuova struttura. Gap fade prima delle 10:30. Long VWAP con LH. Short QQQ con SPY ai max.

## Aggiunte 20/10 (revisione)
- Stato: -442.96, margine 1269.46, servono ~35 $/giorno in 13 sedute.
- Filtro livello: niente ingresso se un livello chiave opposto (close ieri/ven, min/max ieri, PM min/max) è a <1.5R dal fill -> aspetto la reazione al livello.
- Priorità setup: C > 5 > A. C con stop ≤1.0 e primo trade del giorno = 2 MNQ (rischio ≤150).
- Il cumulato si recupera con 1 trade buono al giorno, non con il 2°/3°: se il 1° chiude a +2R o più, il 2° solo se A+ con rischio ≤ metà del profitto.
