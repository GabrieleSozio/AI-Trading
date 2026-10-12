# Playbook fase 2 (dal 12/10/2026)
Obiettivo: P&L fase 2 > 0 entro 06/11, senza bruciare (margine ~1950 $).
Rischio: 100-250 $/trade, perdita max giornaliera ~400 $ (poi stop giornata). Max 3 trade/giorno.
TAGLIA (applicarla davvero): stop ≤1.2 $ QQQ + conferma chiusura 5m -> 2 MNQ. Stop 1.2-2.5 $ -> 1 MNQ. A+ (allineamento SPY/SMH + livello chiave) con stop ≤0.8 -> 3 MNQ.
Ordini: aprire SENZA target (altrimenti lo stop bracket non è modificabile); uscita con modify_stop/close.
Gestione: a +1R stop a pareggio; trailing solo sopra/sotto swing 5m; target 2R (1.5R in giorni a bassi volumi/festivi); lasciar correre fino 11:30 se struttura 5m regge.

## Setup
1. ORB15 + VWAP: range 9:30-9:45; ingresso alla CHIUSURA 5m oltre estremo, lato giusto del VWAP. Stop: sopra/sotto ultimo swing 5m interno al range.
2. Sweep & reclaim livelli (max/min ieri, pre, OR): bucata e rientro CON CHIUSURA 5m oltre il livello -> ingresso; stop oltre estremo dello sweep. Mai anticipare su 1m.
3. Trappola -> reverse: reclaim fallito (sotto VWAP 15-20 min, massimi decrescenti) -> uscire e prendere la rottura dell'estremo OR nell'altro verso. (12/10: +71)
4. Trend 2a ora (10:15-11:00): prezzo stabile su un lato del VWAP con HH/HL -> pullback a VWAP con candela di rifiuto, stop oltre swing.
Nota: la mossa principale spesso 9:45-10:30; dopo 10:30 range stretto -> stringere.
Non usare zona di rumore.
