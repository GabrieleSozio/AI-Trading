# Playbook fase 2 (aggiornato 27/10)
Stato: fase 2 -232.65 dopo 12 sedute, 25 trade (9W/16L, 36%, PF 0.82). Saldo 49770.21, minimo 48290.44, margine 1479.77. Scadenza 06/11: 8 sedute, servono ~29 $/giorno. Settimana 3: +272.71.
RISCHIO: max 150 $/trade, perdita max giorno 200 $. Max 2 trade/giorno. Dopo 1 perdita: 1 solo altro trade con NUOVA struttura e rischio ≤100. Dopo 2 perdite STOP. Dopo un vincente ≥+1.5R: 2° trade solo A+ con livello opposto ≥1.5R e rischio ≤75.

## I 3 SETUP (solo questi)
1. C ALL'APERTURA (9:35-9:55). Sweep di un livello chiave + 1-2 chiusure 5m di nuovo dentro, SPY che NON conferma. 1 MNQ (2 se stop ≤0.9), stop 0.30 oltre lo sweep IEX. Solo se stop ≤150 $ e livello opposto ≥1.5R. Se mancato: non inseguire.
2. ROTTURA RANGE/COMPRESSIONE 30-60' DOPO LE 10:15 (6W/4L, +178; con target fisso 2/2). SPY a nuovi estremi di seduta o in spinta verso di essi. Entrata entro 0.5 dal bordo (bandiera al bordo = migliore). Se già >1 $ oltre -> retest o salto. Stop oltre bandiera/ultimo swing interno +0.30. Stop ≤0.9 -> 2 MNQ; 0.9-1.8 -> 1; >1.8 salto. Il retest del livello rotto è NORMALE: stop fermo.
   - Range day (entrambi i lati bucati e ripresi): preferire la rottura che parte da minimi crescenti/bandiera al bordo; NON la prima rottura debole (<0.6 $, volume calante).
3. GESTIONE: target fisso sul server = minore tra +1.8R e livello strutturale -0.15. Stop fermo, nessun trail. Runner 2° MNQ solo se R ≤0.9 e range ≥3.5 $.
   NB: con target, lo stop non appare nello snapshot -> controllo manuale ogni 2-3'.

## CHECKLIST PRIMA DI place_trade (obbligatoria, scriverla nella tesi)
1) Setup n°? 2) SPY d'accordo? 3) Livelli del piano tra ingresso e target: il primo è ≥1.5R? (27/10 violato: 713.6 a 0.6R -> -109) 4) Rischio $ ≤ limite del momento? 5) Ingresso entro 0.5 dal bordo?

## Filtri
- Gap >0.8% -> solo direzione del gap prima delle 10:30. Gap <0.8% -> nessuna direzione: SPY/SMH e livelli.
- Niente short QQQ con SPY ai max (e viceversa).
- Dopo impulso >3 $ prima delle 10:00 -> aspetto range 30-45' (setup 2).
- Fill >0.3 peggio del segnale -> ricalcolo R; se >150 chiudo.
- Prima di ogni modify_stop: "quale regola lo autorizza?" Se nessuna -> fermo.

## SOSPESI
Trappola->reverse (0/5). Flip immediato dopo stop-out. Gap fade prima 10:30. Long VWAP con LH. Gap&go A (0/2) salvo gap >0.8% con retest pulito.

## 28/10 (mercoledì, decisione FOMC 14:00 ET, fuori orario)
Mattina pre-FOMC: probabile range stretto/compressione. Restare su setup 2 con target 1.8R ridotto al livello strutturale; se il range 9:30-10:15 è <2 $ e gli stop risultano >1.2 $ per R 1.8 non raggiungibile, basta 1 trade pulito. Livelli: 720.26 (max 27/10), 718.05, 716.6, 714.35-713.66, 712.1.
