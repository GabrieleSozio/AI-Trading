# Playbook fase 2 (aggiornato 23/10, revisione settimana 2)
Stato: fase 2 -505.36 dopo 10 sedute, 22 trade (7W/15L, 32%, PF 0.63). Saldo 49497.50, minimo 48290.44, margine 1207.06. Scadenza 06/11: 10 sedute, servono ~51 $/giorno.
RISCHIO: max 150 $/trade, perdita max giorno 200 $. Max 2 trade/giorno. Dopo 1 perdita: 1 solo altro trade con NUOVA struttura e rischio ≤100. Dopo 2 perdite STOP.

## I 3 SETUP DELLA SETTIMANA 3 (solo questi)
1. C ALL'APERTURA (9:35-9:55) – PRIMA SCELTA. Sweep di un livello chiave (min/max ieri, PM, numero tondo) + 1-2 chiusure 5m di nuovo dentro, SPY che NON conferma l'estremo. Entro subito (1 MNQ; 2 se stop ≤0.9), stop 0.30 oltre lo sweep IEX. Se mancato: NON inseguire con la rottura successiva. Gestione: stop fermo; +2R su chiusura 5m -> stop a +0.5R oltre swing 5m; dopo 10:30 si applica la regola target del setup 2.
2. ROTTURA RANGE 30-60' DOPO LE 10:15, con SPY (meglio anche SMH) a nuovi estremi di seduta NEL MOMENTO dell'ingresso. Entrata entro 0.5 dal bordo (chiusura 5m fuori o primo retest). Se già >1 $ oltre -> solo retest del bordo o salto. Stop oltre il bordo/ultimo swing interno +0.30 (non sotto micro-bandiere). Stop ≤0.9 -> 2 MNQ; 0.9-1.8 -> 1; >1.8 salto.
3. GESTIONE DOPO 10:30 (qualsiasi trade aperto dopo le 10:30): TARGET FISSO sul server = minore tra +1.8R e livello strutturale -0.15. Stop fermo, nessun trail. (MFE seconda ora 1.4-2.0R in 3/3 trade: il +2R su chiusura 5m non arriva.)

## Filtri (tutti obbligatori)
- Gap >0.8% -> solo direzione del gap prima delle 10:30. Gap <0.8% -> nessuna direzione: SPY/SMH e livelli.
- SPY d'accordo all'ingresso. Niente short QQQ con SPY ai max (e viceversa).
- Livello opposto a <1.5R dal fill -> niente trade.
- Dopo impulso >3 $ prima delle 10:00 -> aspetto range 30-45' (setup 2).
- Fill >0.3 peggio del segnale -> ricalcolo R; se >150 chiudo.
- Prima di ogni modify_stop: "quale regola lo autorizza?" Se nessuna -> fermo.

## SOSPESI
Trappola->reverse (0/5). Flip immediato dopo stop-out. Gap fade prima 10:30. Long VWAP con LH. Gap&go A (0/2) salvo gap >0.8% con retest pulito. Fade range E: non ancora testato, non prioritario.
