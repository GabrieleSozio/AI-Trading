# Lezioni fase 2
- 12/10 TECNICO: se apro con target, lo stop (bracket) NON è visibile né modificabile (modify_stop fallisce). Per poter fare trailing/pareggio: aprire SENZA target e gestire l'uscita con modify_stop/close.
- 12/10 Sweep&reclaim: entrare SOLO dopo chiusura 5m sopra il livello (oggi la 5m 9:30 chiuse sotto 748.40, ho anticipato su 1m -> fill peggiore 748.19 già sotto il livello). Se dopo 15-20 min il prezzo è sotto VWAP con massimi decrescenti: uscire (fatto bene) e valutare il reverse.
- 12/10 Reverse funziona: uscita dal long fallito + short sulla rottura del min OR15 = +71. Tenere a mente "trappola long -> breakdown".
- 12/10 Gestione: ho spostato lo stop mentale DOPO che era stato toccato (746.30 -> 747.10). Non rifarlo. Trailing solo sopra massimi di swing a 5m, non su 1m.
- 12/10 Mossa utile tutta 10:05-10:30 (~2 $); 2a ora laterale (conferma storica fase 1). Con trade in profitto alle 10:30 e slancio fermo: stringere a sopra ultimo swing 5m.
- Se lo stop server non è modificabile (bracket con target): aprire SENZA target da ora in poi.

## Revisione 12/10 (onesta)
- TAGLIA: ho rischiato 63-102 $/trade, sotto il mio playbook (150-250). Lo short aveva stop 0.77 $ = setup per 2 MNQ e non l'ho fatto: con 2 MNQ la giornata era ~+50 invece di -23. Domani: se lo stop è ≤1.2 $ e il setup è confermato (chiusura 5m), 2 MNQ.
- Errore n.1: ingresso long anticipato su 1m, senza la chiusura 5m sopra il livello. Costo ~-94. Regola: niente chiusura 5m = niente trade.
- Short: uscita 746.35 vs chiusura 11:30 a 745.84 -> trailing su 1m in giornata a bassi volumi mi ha tolto ~0.5 $. Accettabile, ma il trailing va fatto sopra lo swing 5m (qui 746.96 / poi 746.68), non sul rumore a 1m.
- Target 744 (3R) troppo ambizioso in festività con range 1h 4.4: in giorni a bassi volumi target = 1.5-2R o estremo di ieri più vicino.
