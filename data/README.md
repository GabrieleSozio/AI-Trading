# Dati storici (Databento + Alpaca)

Scaricato il 2026-09-20 dal ruolo "data" con budget di 20 USD. Costo effettivo stimato totale: **17.94 USD** (5.26 barre a 1 minuto + 12.68 barre a 1 secondo).

## Fonte
- Provider: [Databento](https://databento.com/), dataset `GLBX.MDP3` (CME Globex MDP 3.0).
- Simboli: contratti continui `MES.c.0` (Micro E-mini S&P 500) e `MNQ.c.0` (Micro E-mini Nasdaq-100), `stype_in=continuous`. Nota: la serie continua di Databento **non è back-adjusted** — i prezzi sono quelli grezzi del contratto front-month via via in vigore, quindi ai roll (vedi log di qualità) c'è un salto di prezzo reale, non un errore.

## File

| File | Periodo | Schema | Simbolo | Dimensione |
|---|---|---|---|---|
| `futures/mes_1m.csv.gz` | 2024-09-01 → 2026-09-18 | ohlcv-1m | MES.c.0 | 7.4 MB (720.554 barre) |
| `futures/mnq_1m.csv.gz` | 2024-09-01 → 2026-09-18 | ohlcv-1m | MNQ.c.0 | 9.6 MB (720.830 barre) |
| `futures/mes_1s_2026-06-19_2026-09-19.csv.gz` | 2026-06-19 → 2026-09-19 (3 mesi) | ohlcv-1s | MES.c.0 | 20.5 MB (3.471.945 barre) |

Colonne in tutti i file: `ts_event` (UTC, ISO-8601), `open, high, low, close, volume, symbol`.

Non è stato necessario scaricare barre a 1 secondo per MNQ (fuori budget dopo il costo di MES; vedi log del giorno) né spezzare i file per anno (tutti sotto i 90 MB).

## Come rileggerli
```python
import pandas as pd
df = pd.read_csv("data/futures/mes_1m.csv.gz", parse_dates=["ts_event"])
```

## Controllo qualità e confronto proxy SPY/QQQ vs futures
Rapporto completo in `state/logs/dati-2026-09-20.md`. Sintesi: correlazione dei rendimenti a 1 minuto ~0.995 per entrambe le coppie; errore mediano sul range di apertura (5 min) ~0.78 tick per MES/SPY e ~3.73 tick per MNQ/QQQ; segnale di rottura del range discorde in <2% delle giornate. Il proxy SPY/QQQ è **utilizzabile** per sviluppare la strategia (vedi dettagli e limiti nel log).

## Storico lungo contratti grandi (ES/NQ) — 2026-09-21

Tentativo di scaricare `ES.c.0` / `NQ.c.0` (contratti grandi, non micro) dal 2010 al 2026 con budget nominale di **45 USD**. **Il credito reale della chiave Databento configurata si è esaurito dopo soli ~2.03 USD** (confermato da 4 richieste consecutive, anche piccole ~0.09-0.11 USD, respinte con `402 account_insufficient_funds`) — non è stato quindi possibile coprire l'intervallo richiesto. Dettagli e tabella costi in `state/logs/dati-2026-09-21.md`.

| File | Periodo coperto | Schema | Simbolo | Dimensione |
|---|---|---|---|---|
| `futures/es_1m_2010.csv.gz` | 2010-06-07 → 2010-12-31 (178 gg, dall'inizio del dataset Databento) | ohlcv-1m | ES.c.0 | 1.5 MB (197.791 barre) |
| `futures/nq_1m_2010.csv.gz` | 2010-06-07 → 2010-12-31 (178 gg) | ohlcv-1m | NQ.c.0 | 1.3 MB (169.823 barre) |
| `futures/es_1m_2011.csv.gz` | **solo 2011-04-01 → 2011-04-29** (24 gg, budget esaurito) | ohlcv-1m | ES.c.0 | 196 KB (27.143 barre) |
| `futures/nq_1m_2011.csv.gz` | **solo 2011-03-01 → 2011-03-31** (27 gg, budget esaurito) | ohlcv-1m | NQ.c.0 | 216 KB (26.550 barre) |

Colonne: `ts_event, open, high, low, close, volume` (senza colonna `symbol`, univoco per file).

**Anomalia operativa**: durante l'esplorazione del vero credito residuo sono stati scaricati e addebitati anche ES/NQ gennaio-febbraio 2011 ed ES marzo 2011 (~0.49 USD) senza salvarli su disco (errore dello script di probe). Non è stato possibile riscaricarli perché il credito si è esaurito subito dopo. Copertura 2011 quindi **non contigua**: manca gen-feb (ES e NQ), manca ES-marzo, manca tutto da maggio 2026-09 in poi.

Nessun file oltre il 2011 è stato scaricato (2012-2026 tutti respinti per credito esaurito, sia in blocchi annuali sia mensili).

## Dati storici azioni (Alpaca) — SPY/QQQ, 1 minuto — 2026-09-21

Storico a 1 minuto di SPY e QQQ scaricato da Alpaca (`GET /v2/stocks/bars`, `feed=sip`, `adjustment=all`), dal 2016-01-01 a ieri (2026-09-20; ultima seduta disponibile venerdì 2026-09-18). Un file per anno e per simbolo, 22 file totali, 47 MB su disco.

### File

| File | Periodo | Barre | Dimensione |
|---|---|---|---|
| `equity/spy_1m_2016.csv.gz` … `equity/spy_1m_2025.csv.gz` | anni interi 2016-2025 | ~171k-214k/anno | ~1.7-2.6 MB/anno |
| `equity/spy_1m_2026.csv.gz` | 2026-01-01 → 2026-09-18 (parziale, in corso) | 162.742 | 2.0 MB |
| `equity/qqq_1m_2016.csv.gz` … `equity/qqq_1m_2025.csv.gz` | anni interi 2016-2025 | ~140k-221k/anno | ~1.4-2.7 MB/anno |
| `equity/qqq_1m_2026.csv.gz` | 2026-01-01 → 2026-09-18 (parziale, in corso) | 167.261 | 2.1 MB |

Totali: SPY 2.148.675 barre, QQQ 2.072.626 barre. Dettaglio anno per anno e controllo qualità completo in `state/logs/dati-2026-09-21b.md`.

Colonne: `ts,open,high,low,close,volume`, timestamp UTC ISO-8601. Include le sessioni estese (pre/post market): i timestamp vicini alla mezzanotte UTC possono quindi appartenere alla giornata di borsa ET del giorno del calendario UTC precedente o successivo — non è un buco nei dati, è il fuso orario.

### Come rileggerli
```python
import pandas as pd
df = pd.read_csv("data/equity/spy_1m_2024.csv.gz", parse_dates=["ts"])
```
