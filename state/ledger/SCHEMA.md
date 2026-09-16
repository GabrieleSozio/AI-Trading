# Schemi dei registri (append-only)

Regole: UTF-8, separatore `,`, timestamp UTC ISO-8601, numeri con il punto decimale. **Non modificare né cancellare righe esistenti.** Le correzioni si fanno con una nuova riga che ha `note=correction:<id>`.

## runs.csv — una riga per ogni run
`run_id,date,role,started_utc,ended_utc,status,mode,orders_sent,decisions,web_searches,notes`
- `status`: ok | market_closed | error | aborted | shadow
- `run_id`: `YYYYMMDD-<ruolo>` con ruolo cio|trd|pm|cls|cry

## decisions.jsonl — una riga JSON per ogni decisione
Campi: vedi `knowledge/processo/decisione-e-registrazione.md` §5. Obbligatori: `ts, run_id, role, mode, action, symbol, asset, setup, rationale`.

## forecasts.csv — previsioni probabilistiche
`forecast_id,ts,run_id,role,symbol,setup,question,prob,horizon,resolved_utc,outcome,brier`
- `question`: ad es. "target 184.40 prima dello stop 179.60 entro le 15:50"
- `outcome`: 1 | 0 | void (se il trade non è partito: si valuta comunque sul prezzo reale, altrimenti void)
- `brier` = (prob − outcome)²: lo calcola il Coach alla risoluzione, aggiungendo una **nuova riga** con lo stesso `forecast_id` e i campi di risoluzione compilati

## trades.csv — trade chiusi (li aggiunge il Coach)
`trade_id,date,mode,asset,symbol,setup,side,thesis_id,opened_by,entry_utc,exit_utc,qty,entry_px,exit_px,planned_entry,stop_px,target_px,risk_usd,pnl_usd,fees_usd,r_multiple,mae_r,mfe_r,slippage_bps,exit_reason,catalyst,regime,rvol,prob_target,process_grade,client_order_id,notes`
- `mode`: real | shadow
- `exit_reason`: target | stop | time | manual | eod | invalidation
- `process_grade`: A | B | C | D

## equity.csv — una riga per giornata (Coach)
`date,equity_open,equity_close,day_pnl_usd,day_pnl_pct,cum_pnl_pct,hwm,drawdown_pct,spy_day_pct,spy_cum_pct,spy_open_window_pct,trades,wins,losses,exposure_max_pct,mode,notes`
- `spy_open_window_pct`: rendimento di SPY dalle 9:30 alle 10:30 ET

## shadow.csv — titoli scartati seguiti in ombra (Coach)
`date,symbol,setup,reason_skipped,hypothetical_entry,hypothetical_stop,hypothetical_target,hypothetical_r,notes`
