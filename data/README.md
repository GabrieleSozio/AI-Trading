# Dati storici futures (Databento)

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
