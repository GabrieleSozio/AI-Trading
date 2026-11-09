# Playbook fase 2 (aggiornato 09/11)
Stato: fase 2 +6.53 dopo 26 trade (10W/16L, 38%, PF 0.97). Saldo 50009.39, minimo 48290.44, margine ~1719. Scadenza 06/11 superata: si continua, obiettivo restare positivi e crescere (~+50 $/giorno medi).
RISCHIO: max 150 $/trade, perdita max giorno 200 $. Max 2 trade/giorno. Dopo 1 perdita: 1 solo altro trade con NUOVA struttura e rischio ≤100. Dopo 2 perdite STOP. Dopo vincente ≥+1.5R: 2° trade solo A+ con rischio ≤75.

## I 4 SETUP
0. TREND OPEN-DRIVE (nuovo 09/11, 1W +239). Entro 9:45: gap ≥0.6% + 3 barre 5m con min crescenti + SPY/SMH a nuovi max (o simmetrico giù) + pullback 1m ≤1.3 $. Long alla prima bandiera 1m, stop sotto bandiera -0.30 (≤1.8 $, 1 MNQ). Nessun target: stop fermo fino a chiusura 5m oltre +2R, poi trail sotto swing 5m che hanno fatto nuovo estremo ≥1R, -0.50. La regola "aspetta range dopo impulso >3 $" NON si applica a questo setup.
1. C ALL'APERTURA (9:35-9:55). Sweep di un livello chiave + 1-2 chiusure 5m di nuovo dentro, SPY che NON conferma. 1 MNQ (2 se stop ≤0.9), stop 0.30 oltre lo sweep IEX. Solo se stop ≤150 $ e livello opposto ≥1.5R.
2. ROTTURA RANGE/COMPRESSIONE 30-60' DOPO LE 10:15 (6W/4L, +178). SPY a nuovi estremi di seduta. Entrata entro 0.5 dal bordo (bandiera al bordo = migliore). Stop oltre bandiera/swing interno +0.30. Stop ≤0.9 -> 2 MNQ; 0.9-1.8 -> 1; >1.8 salto. Target fisso = min(1.8R, livello strutturale -0.15).
3. GESTIONE: setup 0 = trail da +2R; setup 2 = target fisso. Prima di ogni modify_stop: "quale regola lo autorizza?". Mai spostare lo stop durante un rimbalzo verso di esso. Ultimi 5' -> chiudo a mano.

## CHECKLIST PRIMA DI place_trade (nella tesi)
1) Setup n°? 2) SPY d'accordo? 3) Livelli del piano tra ingresso e target ≥1.5R? 4) Rischio $ ≤ limite? 5) Ingresso entro 0.5 dal bordo/bandiera?

## Filtri
- Gap >0.8% -> solo direzione del gap prima delle 10:30. Gap <0.6% -> nessuna direzione.
- Niente short QQQ con SPY ai max (e viceversa).
- Fill >0.3 peggio del segnale -> ricalcolo R; se >150 chiudo.
- Volatilità alta (barre 15m 3-6 $): sempre 1 MNQ.

## SOSPESI
Trappola->reverse (0/5). Flip immediato dopo stop-out. Gap fade prima 10:30. Long VWAP con LH.

## Aggiunte 09/11 (revisione)
- Setup 0: ingresso alla PRIMA bandiera 1m dopo le 3 barre 5m allineate, non dopo. Se a 9:50 non sono dentro e il prezzo è >1R oltre la bandiera -> aspetto la base 5m successiva.
- Protezione fine sessione (in prova): dopo 11:00, MFE ≥3R -> stop = estremo -1R (se migliore del trail). Unica eccezione ammessa al "solo swing 5m".
- Ogni giorno una riga in statistiche.md, anche se flat.
