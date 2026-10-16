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

## Revisione 15/10 (+48.29)
- T1 short 718.79: MFE +3.3 $ (~+270), chiuso a pareggio. Il pareggio a +1R su chiusura 5m in un range di 6 $ ha tolto tutto. NUOVA REGOLA: a +2R prendo METÀ? (impossibile con 1 MNQ) -> con 1 MNQ: a +2R sposto lo stop a +0.5R sopra/sotto lo swing 5m più vicino, non a pareggio puro; se arriva al livello target strutturale (es. min/max del range opposto, swing chiave) e rallenta -> chiudo. Con 2 MNQ: chiudo 1 a +2R.
- T2: ho stretto lo stop da 721.70 a 721.30 "sopra LH" dopo 15 min laterali -> preso di 0 cent. ERRORE N.1 ANCORA (variante: stringere durante il trade). Mai stringere uno stop in perdita.
- T3 long: rottura del range con SPY/SMH allineati, trail sui minimi 5m crescenti -> +164. Funziona: rottura di un range di 1 ora dopo 10:30 con indici allineati.
- Gap molto grande (>1.2%) dopo più giorni di calo: la direzione del gap NON è garantita anche con dato caldo; in range prima ora, seguire la rottura del range confermata da SPY/SMH.
- 2 trappole sullo stesso livello = il terzo test spesso rompe. Non rifare short al massimo del range al 2°-3° test se SPY fa nuovi massimi.

## Revisione 15/10 – punti onesti in più
- T1: il trade del giorno era corretto (trappola su OR high) e ha dato +2.5R. L'ho restituito tutto per il pareggio puro. Su 4 giorni il problema non è trovare i trade, è TENERE i guadagni: 13/10 e 15/10 MFE totali ~+750 $, incassati ~+640 / ~0.
- T2: fade al 2° test dello stesso massimo mentre SPY saliva = trade a bassa probabilità, non "trappola". Lo stop stretto stavolta ha perso meno (l'originale sarebbe stato preso), ma resta errore di processo: una sola regola, mai stringere.
- T3: il trade migliore è venuto quando ho cambiato idea senza ostinarmi (dopo 2 short, long sulla rottura). Flessibilità di direzione = OK.
- Pattern 4 giorni: le perdite più grandi vengono da trade presi contro la conferma degli altri indici o al 2°/3° tentativo nella stessa zona. Ogni trade: chiedersi "SPY/SMH sono d'accordo?".

## Revisione 16/10 (-147.25)
- ERRORE N.3 (nuovo, costoso): TRAIL TROPPO PRESTO in un range. Short giusto (gap&go 721.89), stop originale 724.15 mai minacciato; l'ho spostato su "swing 5m" minori dentro un range di 2 $ (723.85, poi 722.30) a +0.7R/+1R -> preso a -35, poi il trade sarebbe arrivato a +345. È la 3a volta in 4 giorni che restituisco/manco il trade del giorno per gestione (13/10 ok, 15/10 BE, 16/10 trail).
- REGOLA NUOVA: lo stop iniziale NON si muove finché il prezzo non chiude un 5m oltre +2R. Dopo: trail solo oltre swing 5m che hanno prodotto un nuovo minimo/massimo di almeno 1R (non micro-swing dentro un range). Se il prezzo entra in range sotto VWAP, lo stop resta sopra VWAP/swing principale.
- Long rottura range 1h con SPY NON a nuovi max (solo SMH) contro trend del giorno e sotto struttura LH di giornata = trappola. Setup 5 richiede SPY a nuovi max/min DI SEDUTA, non del range. Ho anche stretto lo stop di 0.21 (721.49->721.70): stessa malattia.
- In giorno con gap giù e trend giù, preferire SOLO short; dopo stop-out del primo, il re-ingresso giusto era nella stessa direzione (rottura 719.8 alle 11:05), non il flip.
- Statistica utile: direzione del gap = direzione della seduta 9:30-11:30 in 3/4 giorni (non 15/10, gap >1.2%).
