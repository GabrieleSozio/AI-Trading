# Playbook fase 2 (aggiornato 26/10)
Stato: fase 2 -289.38 dopo 11 sedute, 23 trade (8W/15L, 35%, PF 0.77). Saldo ~49713.48, minimo 48290.44, margine ~1423. Scadenza 06/11: 9 sedute, servono ~32 $/giorno.
RISCHIO: max 150 $/trade, perdita max giorno 200 $. Max 2 trade/giorno. Dopo 1 perdita: 1 solo altro trade con NUOVA struttura e rischio ≤100. Dopo 2 perdite STOP. Dopo un vincente ≥+1.5R: 2° trade solo A+ con livello opposto ≥1.5R e rischio ≤75.

## I 3 SETUP (solo questi)
1. C ALL'APERTURA (9:35-9:55). Sweep di un livello chiave + 1-2 chiusure 5m di nuovo dentro, SPY che NON conferma. 1 MNQ (2 se stop ≤0.9), stop 0.30 oltre lo sweep IEX. Solo se stop ≤150 $ e livello opposto ≥1.5R. Se mancato: non inseguire.
2. ROTTURA RANGE 30-60' DOPO LE 10:15 (IL SETUP CHE FUNZIONA: 26/10 +216). SPY a nuovi estremi di seduta all'ingresso. Entrata entro 0.5 dal bordo. Se già >1 $ oltre -> retest o salto. Stop oltre bandiera/ultimo swing interno +0.30. Stop ≤0.9 -> 2 MNQ; 0.9-1.8 -> 1; >1.8 salto. Il retest del livello rotto è NORMALE: stop fermo.
3. GESTIONE: aprire con target fisso sul server = minore tra +1.8R e livello strutturale -0.15. Stop fermo, nessun trail. Con 2 MNQ (test da fare): 1 al target 1.8R, il 2° su proiezione ampiezza range (se range ≥3.5 $) con stop a pareggio dopo il 1° target.
   NB: con target, lo stop non appare nello snapshot -> controllo manuale ogni 2-3'.

## Filtri (tutti obbligatori)
- Gap >0.8% -> solo direzione del gap prima delle 10:30. Gap <0.8% -> nessuna direzione: SPY/SMH e livelli.
- SPY d'accordo all'ingresso. Niente short QQQ con SPY ai max (e viceversa).
- Livello opposto a <1.5R dal fill -> niente trade.
- Dopo impulso >3 $ prima delle 10:00 -> aspetto range 30-45' (setup 2).
- Fill >0.3 peggio del segnale -> ricalcolo R; se >150 chiudo.
- Prima di ogni modify_stop: "quale regola lo autorizza?" Se nessuna -> fermo.

## SOSPESI
Trappola->reverse (0/5). Flip immediato dopo stop-out. Gap fade prima 10:30. Long VWAP con LH. Gap&go A (0/2) salvo gap >0.8% con retest pulito. Fade range E: non testato.

## Nota 26/10 (revisione)
- Target fisso sul server = regola valida (supera "aprire senza target" in lezioni). Con target: nessun modify_stop, controllo manuale 2-3'.
- Runner 2° MNQ solo se R ≤0.9 e range rotto ≥3.5 $: target 2 = bordo + ampiezza range; dopo target 1 stop del 2° a pareggio (richiede chiudere e riaprire 1 MNQ: costi ~1.24 + slip).
- Settimana 3: +216 dopo 1 giorno. Venerdì 30/10 verifica. Non aumentare rischio per euforia: max 150/trade invariato.
