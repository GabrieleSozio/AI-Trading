# Playbook: schede dei setup

Le schede descrivono setup **conosciuti**, non regole obbligatorie. Gli agenti possono:
- usarle, adattarle (la variante va scritta nel log) o ignorarle;
- proporne di nuove: il file va creato con `stato: sperimentale` e un id nuovo.
Lo stato di ogni setup (sperimentale / in_prova / attivo / sospeso / ritirato) lo decide il Coach con le statistiche in `state/memory/playbook-stats.md`.

| id | Asset | Finestra | Stato iniziale |
|---|---|---|---|
| `orb-sip` | azioni | 09:35-10:30 | in_prova |
| `gap-go` | azioni | 09:31-10:30 | in_prova |
| `gap-fade` | azioni (short o put) | 09:45-11:00 | sperimentale |
| `vwap-reclaim` | azioni/ETF | 10:00-12:00 | sperimentale |
| `etf-noise` | ETF (SPY/QQQ/IWM, settoriali) | 10:00-15:30 | sperimentale |
| `opt-catalyst` | opzioni (long o debit spread) | 09:45-11:00 | sperimentale |
| `crypto-trend` | crypto | qualsiasi | sperimentale |
| `crypto-asia-open` | crypto | domenica sera ET | sperimentale |
| `orb15-conferma`, `orb-retest`, `orb-fallito`, `orb-inverso`, `orb-indice-leva` (in `orb-varianti.md`) | azioni/ETF | apertura | sperimentale, **facoltative** |

## Nome del setup
Nel campo `setup` dei registri va **esattamente** l'id di una scheda (`vwap-reclaim`, non `vwap-reclaim-pullback`). Le varianti applicate si scrivono in `notes` o nel log: nomi diversi spezzano le statistiche.

## Gestione dell'uscita
Ogni scheda indica l'uscita di default. L'agente può scegliere, trade per trade, fra tre modi (vedi `config/risk-limits.md` §A e gli esempi in `knowledge/dati/alpaca-api.md`):
- `fixed` — bracket con target e stop fermi (default; è la gestione con più evidenza a favore negli studi ORB);
- `breakeven` — a +1R lo stop si sposta al prezzo d'ingresso;
- `trailing` — trailing stop di Alpaca (lo muove il server, niente target fisso; non disponibile per crypto, opzioni e frazionari).
La scelta va registrata nel campo `exit_mgmt`, così il Coach può confrontare i risultati dei tre modi.

## Lato ribassista
Con equity sotto i 2.000 USD lo short di azioni ed ETF non è eseguibile: si usano ETF inversi comprati long o put/put spread (`knowledge/dati/alpaca-conto-e-limiti.md`).

Formato di una scheda: `id, stato, asset, finestra, evidenza, condizioni, ingresso, stop, uscita, dimensione, alternative, da evitare, cosa registrare`.
