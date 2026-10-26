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

## Revisione 19/10 (-294) onesta
- Gap +1.37% su. Seduta: frusta 718-720 fino 9:55, falsa rottura giù a 716.64, V-reversal, retest VWAP 10:30 (719.23, tenuto), trend su fino 724.1. Direzione del gap ha vinto ANCORA (gap fill mai neanche avvicinato).
- T1 short contro gap: il setup B era nel piano, ma è il trade a probabilità più bassa (contro gap). Fill 0.56 peggio del segnale: la regola diceva ricalcolare R e io no -> rischio 164 invece di ~115.
- T2 long: direzione giusta, ma INSEGUITO dopo +4 $ in 10 min, con stop sotto la barra di rottura (micro-struttura). Il pullback normale è tornato al VWAP (719.23 vs VWAP 719.04) e mi ha preso; poi +4.3 $. Stesso schema di 14/10 e 16/10: direzione giusta, stop dentro il rumore.
- DIAGNOSI 6 GIORNI: 12 perdite su 15. Il problema non è la direzione, è DOVE entro: a mercato dopo la barra di rottura (già estesa, slittamento 0.4-0.6) e con stop a 1.4-2 $ che sta dentro il ritracciamento normale (QQQ ritraccia 50-60% di una gamba da 4 $ prima di ripartire).
- REGOLA NUOVA (ingresso sul retest): dopo la rottura/chiusura 5m che dà la direzione, NON entro a mercato. Aspetto il ritracciamento verso il livello rotto o il VWAP (entro 0.5 $) con una barra 1-5m di rifiuto, entro lì. Stop oltre il VWAP / swing di ritracciamento +0.30. Se non torna, salto il trade (meglio perdere un trade che inseguire).
- Stop sotto la "barra di rottura" VIETATO come stop principale: lo stop va oltre il VWAP o oltre lo swing che ha generato la mossa.
- Contro gap: vietato prima delle 10:30. Il gap +/- >0.8% ha tenuto la direzione 9:30-11:30 in 4 giorni su 6 (eccezione 15/10 e 13/10 parziale); i miei trade contro gap: quasi tutti persi.
- Dopo il primo stop-out, il secondo trade nella direzione opposta (flip) è stato perso 3 volte su 3 (15/10, 16/10, 19/10). Dopo uno stop: pausa fino a nuova struttura chiara (retest VWAP), non flip immediato a mercato.

## Revisione 20/10 (+47.52)
- T1 short: setup A eseguito "da manuale" (retest VWAP + rifiuto) ma con SPY ai MAX di seduta e QQQ sul close di venerdì (709.8, supporto): stop in 2 min. Il check "SPY d'accordo?" era NO e l'ho ignorato. REGOLA: se SPY fa nuovi max mentre shorto QQQ (o viceversa) -> niente trade, anche se il setup è perfetto. Gap piccolo (<0.5%) = direzione del gap non vale.
- T2 long: ingresso dentro la bandiera (non sulla rottura) con stop sotto la bandiera, tutti gli indici allineati -> +4.3 $ MFE, +149. Stop fermo fino a +2R, poi trail su swing che ha creato nuovo max: ha funzionato. Il flip dopo stop-out ha funzionato perché c'era NUOVA struttura (chiusura 5m sopra OR high + gap fill) e 20 min di pausa.
- Ingresso "in bandiera" = buona alternativa al retest quando il trend è forte e il pullback non arriva (10:00-10:14 nessun retest).
- Trail a fine sessione (<30 min) sul min del range di 30' = corretto.
- Quello che manca ancora: il trade A+ del giorno era il long dalla V (713.5-714 alle 9:55 con stop 712.6) → +8 $. Riconoscere prima la V-reversal su supporto chiave (close ven) con SPY forte.

- Aggiunta revisione 20/10: T1 short preso con il supporto chiave (close ven 709.8) a soli 3 $ e SPY ai max -> due "no" ignorati. REGOLA: niente short se un supporto chiave (close ieri/ven, min ieri) è a <1.5R dal fill; niente long simmetrico sotto resistenza chiave. Lì si aspetta la reazione al livello (setup C), non si entra prima.
- T2: con stop 0.95 il playbook dava 2 MNQ, ho tenuto 1 per il limite dopo-perdita (rischio ≤95). Coerente con le regole; costo opportunità ~150 $. Ok così finché il conto è in perdita: la disciplina viene prima.
- Unico setup con aspettativa positiva provata: C (sweep/V su livello chiave + SPY allineato + ingresso al retest/bandiera) 2W/2L +427. Tutti gli altri negativi. Domani: C prima scelta; A solo con gap >0.8% e SPY d'accordo.

## Revisione 21/10 (+91.28)
- Giornata di range puro (720.13-723.54 per 80 min), gap +0.68% senza direzione, SPY e SMH divergenti. Ho aspettato invece di forzare: giusto. Il trade buono è arrivato alla risoluzione della COMPRESSIONE (minimi crescenti 720.13/721.20/722.29 + max ripetuti a 723) con SMH su: long in bandiera al top, stop sotto bandiera. Setup nuovo valido: "compressione -> bandiera al top/fondo del range dopo 10:30".
- T1: ordine a mercato su barra veloce = slip 0.65 (3a volta >0.5). Chiudere subito è stato corretto (regola rispettata). Prima di entrare in bandiera controllare che l'ultima barra 1m non stia già rompendo: se sì, aspetto il retest.
- T2 gestione: negli ultimi 15' ho trailato sotto uno swing 1m (-0.30) e IEX non mostrava nemmeno il tocco (min 724.01, fill 723.65: i dati IEX sottostimano i minimi di ~0.35). REGOLA: trail finale sul minimo del range 30' oppure swing 5m -0.50 (non -0.30) per il rumore IEX. Costo stimato ~55 $.
- Mancato: range day = mean reversion agli estremi (long 720.3 stop 719.8 al triplo minimo 10:10-10:21 → +2.5 $). Nei giorni di range dopo 10:00 posso fare 1 fade dell'estremo al 3° test con stop 0.5 oltre, se SPY non fa nuovi estremi nel verso della rottura.

## Revisione 21/10 – punti onesti aggiuntivi
- Il +28.84 del T1 è FORTUNA, non abilità: ingresso sbagliato (market su barra veloce, 2 MNQ, rischio reale 258 > limite). Lo conto come errore di esecuzione corretto in tempo.
- T2: la regola "dopo 11:00 trail su range 30'" ESISTEVA già nel playbook e l'ho violata con swing 1m. Non è una lezione nuova, è indisciplina in gestione (4a volta in fase 2 che la gestione toglie profitto: 15/10, 16/10, 21/10). Regola di processo: prima di ogni modify_stop scrivo "quale regola del playbook autorizza questo stop?". Se non ne trovo una -> non lo muovo.
- Dato positivo: 2 giorni di fila positivi rispettando filtro SPY e attesa. 1° trade buono del giorno resta la chiave; ~30 $/giorno bastano.

## Revisione 22/10 (+12.70) onesta
- Lettura giusta: gap -1.77%, aspettato il range 9:30-10:15 (niente trade in frusta = bene), visto il triangolo discendente sotto VWAP (max 715.27/713.62/713.41/712.58), SPY/SMH allineati. Direzione corretta.
- ERRORE: INGRESSO TARDIVO. La rottura del triangolo è stata alle 10:20 (~712.0, stop sopra 712.58+0.30 = 712.90, R ~0.9 -> 2 MNQ). Sono entrato alle 10:31 a 708.82, dopo 3.2 $ già percorsi, con R 1.48 e quindi 1 MNQ. Stessa mossa (fino 706.7): ingresso 10:20 = ~+5 $ x 2 MNQ (~+800 MFE) contro +2.11 x 1. Il setup D va preso ALLA rottura del bordo della compressione (barra 5m che chiude fuori) o al primo retest del bordo, non 2 barre dopo.
- Il filtro "livello opposto a <1.5R" (710.4) andava valutato SUBITO alle 10:20: 712.0-710.4 = 1.6 $ = 1.8R con R 0.9 -> ok. Aspettare la rottura di 710.4 mi ha fatto entrare a metà mossa.
- GESTIONE: trail post-11:00 a 708.54 = 0.08 sopra il max della barra 11:15 (708.46) mentre il prezzo rimbalzava già. Tecnicamente "swing 5m 11:05 +0.50", ma la barra successiva aveva già testato lì: stop dentro il rumore. REGOLA: lo stop di trail va oltre lo swing PIÙ RECENTE (incluso il rimbalzo in corso) +0.50; mai spostare lo stop durante un rimbalzo in atto verso di esso. Con stop 709.46 (max range 30' +0.50) sarei uscito a 11:30 ~708.1 (+54).
- Target strutturale 707.27 toccato alle 10:45 e il prezzo ha rallentato (5 barre 707.3-708.9): regola 15/10 diceva "se arriva al target strutturale e rallenta -> chiudo/stringo". Non applicata. Su trend lento senza +2R, al livello target: prendere almeno parziale (con 2 MNQ) o stop a pareggio+0.5R SOLO se c'è uno swing 5m vero.
- Dato: in un giorno di gap grande, il trend vero è partito alle 10:15-10:20 dopo 45' di range. 3° giorno su 4 che la mossa buona parte dopo un range/compressione (20/10 10:10, 21/10 10:50, 22/10 10:20).

## Revisione 23/10 (-166.38) onesta
- T1: filtro "livello opposto <1.5R" VIOLATO consapevolmente (707.3 a 1.1R) e SPY aveva smesso di fare max dopo 10:00. Con gap piccolo, dopo una V di +3.5 $ in 15', la mezz'ora successiva è stata RANGE (703.4-706.2) attorno al VWAP: la rottura della compressione alle 9:55 era dentro un range più grande, non un nuovo trend. REGOLA: dopo una V/impulso iniziale >3 $ prima delle 10:00, la prima rottura successiva è sospetta; aspettare il range 30-45' e la sua rottura (come 22/10, 21/10, oggi: mossa buona 10:20-10:40).
- T2: lettura giusta (range 1h rotto al 4° test con SMH/SPY a nuovi max, +3.5 $ di mossa), ma ingresso dopo 1.4 $ di estensione con stop bandiera 0.79: il ritorno normale sul livello rotto (706.2-706.8) lo prende. Stessa diagnosi del 19/10: stop dentro il ritracciamento normale. Lo stop strutturale (706.19-0.30=705.89) stava a 1.7 $ = 140 $ > limite post-perdita -> per regola andava SALTATO, oppure aspettato il retest del livello rotto 706.2-706.6 (arrivato alle 11:10, 706.83) con stop 705.89.
- Gestione T2: +2R mancato per 0.02 sul massimo, poi -65. Dopo 11:00 con trade a +1.5R e 3 barre 5m senza nuovi max, nessuna regola mi proteggeva. NUOVA REGOLA (solo dopo 11:00, 1 MNQ): se il trade ha fatto ≥+1.5R e poi 2 barre 5m chiudono sotto il max senza nuovo max -> stop al pareggio +0.10 (non micro-trail: è l'ultima mezz'ora, il tempo lavora contro). Oggi = ~0 invece di -65.
- Dato: rotture di range dopo 10:30 = mossa 3-4 $ in 15-20', poi ritracciamento 50-60% entro le 11:30 (21/10, 22/10, 23/10). Quindi l'ingresso deve essere VICINO al livello rotto (entro 0.5) o niente.

## Revisione 23/10 – aggiunte (seconda lettura)
- IL TRADE DEL GIORNO ERA IL MIO SETUP C, PRIMA SCELTA DEL PIANO, E NON L'HO PRESO: sweep 701.94 -> 701.18 alle 9:37 (doppio minimo), reclaim, V fino a 704.85 entro le 9:45. Long ~702.3 con stop ~700.85 = +2.5 $ in 10'. È la 2a volta (20/10 V da 710.42) che il C migliore della giornata arriva nei primi 15' e io entro dopo, a mossa fatta, in un trade peggiore. Il dato PMI delle 9:45 non è una scusa: la V era già partita.
  REGOLA: se il C del piano scatta 9:35-9:50 (sweep del livello + chiusura 1-2 barre 5m sopra, SPY che non fa nuovi min) -> entro, 1 MNQ, stop 0.30 sotto lo sweep IEX. Se l'ho mancato, NON lo inseguo con una rottura successiva.
- MFE dei trade in seconda ora (dopo 10:30): 21/10 +1.40 $ (1.8R), 22/10 +2.11 (1.4R), 23/10 +1.56 (2.0R sul max, ma nessuna chiusura 5m oltre). La regola "aspetto chiusura 5m oltre +2R" quasi non scatta mai dopo 10:30: il prezzo fa 1.5-2R e torna indietro (ritracciamento 50-60%). Ho perso/sciupato 3 trade su 3 per questo.
  REGOLA NUOVA (trade dopo 10:30): target FISSO sul server = il minore tra +1.8R e il livello strutturale -0.15. Stop fermo. Nessun trail. Sul 23/10 T2 = +~115 invece di -65; 21/10 T2 = target preso al pelo.
- Il playbook è diventato una lista di 20 regole, una per ogni perdita. Troppe regole = esitazione all'ingresso giusto (C a 9:37) e attivismo su quello sbagliato. Per la settimana 3 lavoro con 3 cose: (1) C all'apertura, (2) rottura di range 30-60' dopo le 10:15 entrando VICINO al bordo, (3) target fisso dopo 10:30. Il resto è contorno.

## Revisione 26/10 (+215.98)
- Trade fatto da playbook: aspettato 45' di frusta (niente short sullo sweep 709.53: stop 200 $ e supporto a <1.5R; niente long sul triplo minimo perché VWAP a 1.3R), poi rottura del range con SPY a nuovi max, ingresso 0.1 dal bordo, stop strutturale sotto bandiera, retest del livello rotto (709.36/708.81) tenuto senza toccare lo stop, target fisso 1.8R preso. Disciplina di gestione rispettata (nessun modify_stop di livello).
- Costo opportunità: il trend è continuato fino 714.8 (+5.2 dal fill). Il target fisso 1.8R ha preso il 50% della mossa. Dato opposto ai 3 giorni precedenti (21-23/10). Ipotesi da testare: quando il range rotto è ampio (≥3.5 $) e SPY fa nuovi max con QQQ a minimi crescenti, la mossa misurata = ampiezza del range (709.5+3.9 = 713.4, preso). Target alternativo = proiezione range. Con 2 MNQ: 1 al 1.8R, 1 sulla proiezione/trail range 30'.
- Tecnica: aprendo con target, lo snapshot mostra "Stop sul server: -" e modify_stop risponde "nessun ordine" -> lo stop della bracket probabilmente esiste (gamba OCO in attesa) ma non è verificabile. Monitorare a mano a 2-3' quando si apre con target.
- Sweep del max di ieri all'apertura (709.15->709.53) fallito = NON ha dato direzione: era solo l'estremo del range iniziale. Con gap piccolo, il range 30-45' e la sua rottura restano il setup più affidabile (4° giorno su 5: 20,21,22,23,26/10 mossa buona 10:10-10:50).

## Revisione 26/10 – seconda lettura (onesta)
- CONTRADDIZIONE RISOLTA: "Regole tecniche" in cima diceva "aprire SENZA target"; il playbook dal 23/10 dice target fisso dopo 10:15. VALE IL PLAYBOOK: target fisso sul server per il setup 2 (provato 26/10). Prezzo: stop non modificabile/visibile -> niente modify_stop, controllo manuale ogni 2-3'. Per il setup C all'apertura (9:35-9:55) si può aprire senza target se voglio gestire.
- Il +216 non è prova statistica: setup 2 ora 3W/3L. Merito vero = processo (45' senza forzare, 2 scenari C scartati per R/R motivato, ingresso vicino al bordo, nessun intervento sullo stop durante il retest a 708.81, a 0.6 dallo stop).
- Dopo il target: niente re-ingresso perché esteso (+3 $ oltre il bordo) e resistenza 715.27 vicina = corretto per le regole. Il costo (+2.5 $ ulteriori) si recupera con il runner su 2 MNQ, non inseguendo.
- R del trade 1.43 -> 1 MNQ era corretto da playbook. Il runner richiede R ≤0.9: se la bandiera è stretta, usarlo.
