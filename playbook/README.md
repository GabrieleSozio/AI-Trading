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

Formato di una scheda: `id, stato, asset, finestra, evidenza, condizioni, ingresso, stop, uscita, dimensione, alternative, da evitare, cosa registrare`.
