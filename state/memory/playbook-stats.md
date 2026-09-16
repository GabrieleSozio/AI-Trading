# Statistiche del playbook (aggiornate dal Coach)

Ultimo aggiornamento: 2026-09-16 (ricalcolo da `trades.csv`: **0 trade reali, 0 shadow** → nessuna metrica disponibile)

| setup | stato | trade (real) | trade (shadow) | win % | R medio vinc. | R medio perd. | expectancy R | IC 95% | profit factor | ultimo cambio stato |
|---|---|---|---|---|---|---|---|---|---|---|
| orb-sip | in_prova | 0 | 0 | – | – | – | – | – | – | init |
| gap-go | in_prova | 0 | 0 | – | – | – | – | – | – | init |
| gap-fade | sperimentale | 0 | 0 | – | – | – | – | – | – | init |
| vwap-reclaim | sperimentale | 0 | 0 | – | – | – | – | – | – | init |
| etf-noise | sperimentale | 0 | 0 | – | – | – | – | – | – | init |
| opt-catalyst | sperimentale | 0 | 0 | – | – | – | – | – | – | init |
| crypto-trend | sperimentale | 0 | 0 | – | – | – | – | – | – | init |
| crypto-asia-open | sperimentale | 0 | 0 | – | – | – | – | – | – | init |

**Cambi di stato applicati oggi: nessuno.** Con 0 trade non c'è alcun dato che giustifichi una transizione: il ciclo di vita (metriche §6) è guidato dal numero di trade, e nessun setup si è mosso dal valore di init.

> ⚠ **Incoerenza da sciogliere (proprietario).** `playbook/README.md` assegna a `orb-sip` e `gap-go` lo stato iniziale `in_prova` (rischio ≤ 1%), mentre il criterio di metriche §6 dice `sperimentale` = "nuovo, meno di 10 trade" (rischio 0,25-0,5%). Con 0 trade i due criteri divergono. Il Coach **non** ha modificato gli stati: la transizione va guidata dai dati e i dati non esistono ancora. Da decidere prima del primo trade reale: se vale l'anagrafica del README (perché sono setup documentati in letteratura, non inventati qui) o il conteggio dei trade (più prudente). Nel dubbio il Trader usi la fascia più bassa.

## Per asset class
_(nessun trade)_

## Per regime
_(nessun trade)_

## Per ruolo (chi propone e chi esegue)
_(nessun trade)_
