# Routine della firm

Ogni file contiene i metadati (orario, modello, repo, ambiente) e, dopo la riga `---PROMPT---`, il prompt esatto salvato nella routine.
Se cambi un prompt qui, aggiorna anche la routine su claude.ai/code/routines (o chiedi a Claude di farlo).

| File | Ruolo | Orario ET | Cron UTC (fino al 31/10) | Cron UTC (dal 2/11) | Modello |
|---|---|---|---|---|---|
| 00-test-connessione.md | Test | manuale | – | – | Opus 5 |
| 01-cio.md | CIO / Stratega | 08:40 lun-ven | `40 12 * * 1-5` | `40 13 * * 1-5` | Opus 5 |
| 02-trader.md | Trader + Risk Officer | 09:20-10:15 lun-ven | `20 13 * * 1-5` | `20 14 * * 1-5` | Opus 5 |
| 03-position-manager.md | Position Manager | 11:30 lun-ven | `30 15 * * 1-5` | `30 16 * * 1-5` | Opus 5 |
| 04-closer-coach.md | Closer + Coach | 15:45-16:30 lun-ven | `45 19 * * 1-5` | `45 20 * * 1-5` | Opus 5 (o Sonnet) |
| 05-crypto-desk.md | Desk crypto | sab/dom 15:00 UTC | `0 15 * * 6,0` | `0 15 * * 6,0` | Opus 5 |
| 06-scarico-dati-futures.md | Scarico dati futures (una tantum) | manuale | – | – | Sonnet 5 |

Run al giorno: 4 nei giorni di borsa, 1 nei giorni del weekend (limite del piano Pro: 5 al giorno). Secondo la documentazione, le run programmate una sola volta (one-off) non contano nel limite giornaliero; per "Run now" non è specificato.
