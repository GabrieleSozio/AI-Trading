# Playbook fase 2 (aggiornato 19/10)
Obiettivo: P&L fase 2 > 0 entro 06/11 (ora -490.48 dopo 6 gg, mancano 14 gg). Saldo 49512.38, minimo 48290.44, margine 1221.94.
RISCHIO (margine piccolo): max 150 $/trade, perdita max giornaliera 200 $ -> dopo 1 perdita piena: solo 1 altro trade A+ nella direzione del gap; dopo 2 perdite STOP giornata. Max 2 trade/giorno.
Serve: 1-2 trade buoni a +2/+3R. Pochi trade, entrate migliori, stop fuori dal rumore.

## ORDINE DI LAVORO PER OGNI TRADE
1) Direzione = direzione del gap (default). Contro gap solo dopo 10:30 e solo se SPY E SMH fanno nuovi estremi di seduta nell'altro verso + VWAP perso con chiusura 5m.
2) Aspetto la conferma (chiusura 5m oltre OR / VWAP / sweep reclaim) -> NON entro a mercato.
3) Ingresso sul RETEST: prezzo torna entro 0.5 $ dal livello rotto o dal VWAP + barra di rifiuto -> entro. Se non torna entro ~20 min, salto.
4) Stop oltre VWAP o swing di ritracciamento +0.30 (mai sotto la sola barra di rottura).
5) Taglia: stop ≤1.0 -> 2 MNQ (rischio ≤150); stop 1.0-1.8 -> 1 MNQ; stop >1.8 -> salto. Mai stringere lo stop.
6) Check: stop == tesi? fill entro 0.3 dal segnale (altrimenti ricalcolo/chiudo)? SPY/SMH d'accordo?

## GESTIONE
- Stop iniziale FERMO finché un 5m non CHIUDE oltre +2R. Niente BE, niente micro-trail.
- Dopo +2R: stop a +0.5R; poi trail oltre swing 5m che hanno fatto nuovo estremo ≥1R. Con 2 MNQ chiudo 1 a +2R.
- Lasciar correre fino a 11:30 se la struttura regge (19/10: trend dal VWAP fino a 11:30).
- Aprire SENZA target.

## Setup attivi
A. Gap&go su retest: chiusura 5m oltre OR15 nella direzione del gap + lato giusto VWAP -> ingresso al retest OR/VWAP. (14/10, 16/10, 19/10: il trade del giorno era questo)
C. Sweep & reclaim a favore del gap: bucata min/max OR/PM contro gap + chiusura 5m di ritorno -> ingresso al retest del livello, stop 0.30 oltre estremo sweep. (13/10 +474; 19/10: sweep 716.64 -> ingresso giusto era retest VWAP 719.2-719.5, stop 718.7)
5. Rottura range 1h (dopo 10:30) a favore del trend con SPY a nuovi estremi di seduta: ingresso al retest del bordo del range.
## Setup SOSPESI
3. Trappola->reverse immediato a mercato (0W/5L). Flip dopo stop-out (0/3). Gap fade prima delle 10:30. Long VWAP con LH. ORB a mercato contro gap in giorni macro.
