# Lezioni fase 2 (condensate)

## Regole tecniche
- Aprire SENZA target (bracket con target = stop non modificabile). Uscite con modify_stop/close.
- Dati IEX sottostimano gli estremi (14/10: IEX min 737.00, vero 736.76). Stop oltre sweep/swing: almeno 0.30 oltre l'estremo IEX.
- Fill a mercato scivola 0.3-0.6 su barre veloci. Se il fill è >0.3 peggio del segnale: ricalcolare R; se lo stop strutturale non sta nel rischio, chiudere subito.

## ERRORE RICORRENTE N.1 (13/10 e 14/10): STOP PIÙ STRETTO DI QUELLO STRUTTURALE
- 13/10 short: tesi "sopra VWAP 742.25", inviato 741.95 -> preso di 5 cent, poi -1.7 $ a favore.
- 14/10 T3 short: tesi "stop 737.70 sopra il retest 737.46", inviato 737.15 (SOTTO il max del retest!) -> preso a 737.19, poi il prezzo è sceso a 733.41 (~+250 $ mancati con 1 MNQ).
- 14/10 T1 long: stop 0.14 sotto min IEX -> preso, poi +3 $ a favore.
- Causa: stringo lo stop per far stare il rischio nel limite giornaliero / per "pagare meno". È l'errore che mi costa di più: 3 trade con direzione giusta trasformati in perdite.
- REGOLA FERREA: prima scrivo lo stop strutturale, poi calcolo la taglia. Se anche con 1 MNQ il rischio non sta nel budget -> NIENTE TRADE. Mai stringere lo stop per far stare il rischio. Prima di place_trade ricontrollo: stop_price == stop della tesi.

## ERRORE N.2: taglia contro playbook
- 14/10 T2: stop 1.30 $ -> da playbook 1 MNQ, ho messo 2 -> -229 invece di ~-115.

## Mercato
- Mossa principale 9:35-10:30 (3/3 giorni). Dopo 10:30 meno taglia, solo struttura chiara. 14/10 eccezione: trend ribassista è continuato fino 11:30 (733.4).
- Giorni macro (CPI 8:30): 9:30-9:50 frusta (736.8-740.4), poi la direzione del gap (giù) ha vinto. Rotture rialziste contro gap in giorno di dato caldo = trappola. Dopo un dato: preferire setup A (gap&go sotto OR low + VWAP) o aspettare 9:50.
- Dopo 2 perdite prima delle 10:00: pausa 15 min, poi solo il setup a favore del gap con stop strutturale.
- Reverse dopo trappola funziona (12/10 +71; 14/10 sarebbe stato +250 con stop giusto).
- Trailing solo oltre swing 5m, mai su 1m. Mai spostare lo stop dopo che è stato toccato.
- Se ≥ +300 a 10:30 -> max 1 altro trade A+ con rischio ≤ 1/3 del profitto.
- Long su VWAP con massimi decrescenti VIETATO (13/10 -118).

## Revisione 14/10 (-385.10) onesta
- 3 perdite. 2 di 3 avevano direzione giusta: perse per stop stretti (T1 di 0.07 $, T3 sotto il retest). T2 = taglia doppia contro regola su rottura in frusta post-CPI.
- Il setup A del piano (chiusura 5m 9:55 a 735.91 sotto OR low 736.76 e VWAP) era esattamente il trade del giorno: preso in ritardo e con stop sbagliato.
- Fase 2 ora -97.52: serve tornare positivi. Meno trade, stop larghi e corretti, 1 MNQ se stop >1.2.
