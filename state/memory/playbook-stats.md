# Statistiche del playbook (aggiornate dal Coach)

Ultimo aggiornamento: 2026-09-17 (Coach)

| setup | stato | trade (real) | trade (shadow) | win % | R medio vinc. | R medio perd. | expectancy R | IC 95% | profit factor | ultimo cambio stato |
|---|---|---|---|---|---|---|---|---|---|---|
| orb-sip | in_prova | 0 | 1 | – | – | – | – | – | – | init |
| gap-go | in_prova | 0 | 1 (void) | – | – | – | – | – | – | init |
| gap-fade | sperimentale | 0 | 0 | – | – | – | – | – | – | init |
| vwap-reclaim | sperimentale | 1 | 1 | 0% | – | -1,03R | -1,03R | n=1, troppo pochi per un IC | 0,00 | init |
| etf-noise | sperimentale | 0 | 1 (void) | – | – | – | – | – | – | init |
| opt-catalyst | sperimentale | 0 | 0 | – | – | – | – | – | – | init |
| crypto-trend | sperimentale | 0 | 0 | – | – | – | – | – | – | init |
| crypto-asia-open | sperimentale | 0 | 0 | – | – | – | – | – | – | init |

Nota: con n=1 nessuna statistica è significativa (§4 metriche-e-valutazione.md: servono ~440 trade per un'expectancy stimata con confidenza al 95%). Nessun cambio di stato oggi (tutti i setup restano sotto le soglie di `sperimentale`/`in_prova`).

## Per asset class
| asset | trade (real) | R medio | note |
|---|---|---|---|
| stock | 1 | -1,03R | INTC (vwap-reclaim), unico trade reale del 17/09 |

## Per regime
| regime | trade (real) | R medio | note |
|---|---|---|---|
| post-fomc digestion, vol in salita, ampiezza stretta | 1 | -1,03R | 17/09/2026 (giorno dopo FOMC +25bp) |

## Per ruolo (chi propone e chi esegue)
| ruolo che apre | trade (real) | R medio |
|---|---|---|
| pos_manager (pm) | 1 | -1,03R |
