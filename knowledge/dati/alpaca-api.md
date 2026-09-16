# Alpaca API: guida rapida operativa

Le credenziali le aggiunge il proxy dell'ambiente: **non passare header di autenticazione**. Se una chiamata risponde 401/403, le credenziali non sono configurate: registra l'errore in `runs.csv` e **non** tentare altre strade.

```bash
T=https://paper-api.alpaca.markets      # trading (SOLO paper)
D=https://data.alpaca.markets           # dati
j() { curl -sS --max-time 20 "$@"; }    # usa sempre jq per filtrare
```

## Stato del mercato e del conto
```bash
j $T/v2/clock | jq '{ts:.timestamp,open:.is_open,next_open,next_close}'
j "$T/v2/calendar?start=2026-09-17&end=2026-09-17"            # orari reali (mezze giornate)
j $T/v2/account | jq '{equity,last_equity,cash,buying_power,daytrading_buying_power,status}'
j $T/v2/positions | jq '[.[]|{symbol,asset_class,qty,avg_entry_price,current_price,unrealized_pl,unrealized_plpc}]'
j "$T/v2/orders?status=open&limit=100" | jq '[.[]|{id,client_order_id,symbol,type,side,qty,stop_price,limit_price,status,order_class}]'
j "$T/v2/orders:by_client_order_id?client_order_id=20260917-trd-orb-1"
j "$T/v2/account/activities/FILL?date=2026-09-17"            # fill del giorno (per il Coach)
j "$T/v2/account/portfolio/history?period=1M&timeframe=1D"
j "$T/v2/assets/NVDA" | jq '{tradable,shortable,easy_to_borrow,fractionable}'
j "$T/v2/assets?asset_class=crypto&status=active" | jq '[.[]|.symbol]'
```

## Dati azioni (piano gratuito: `feed=iex`)
```bash
j "$D/v2/stocks/snapshots?symbols=NVDA,AMD,SPY&feed=iex" | jq 'map_values({p:.latestTrade.p, bid:.latestQuote.bp, ask:.latestQuote.ap, dayO:.dailyBar.o, dayV:.dailyBar.v, prevC:.prevDailyBar.c})'
j "$D/v2/stocks/bars?symbols=NVDA&timeframe=5Min&start=2026-09-17T13:30:00Z&feed=iex&limit=100"
j "$D/v2/stocks/bars?symbols=NVDA&timeframe=1Day&start=2026-08-01&adjustment=split&feed=sip"   # storico SIP ok se > 15 min fa
j "$D/v1beta1/screener/stocks/most-actives?by=volume&top=20"     # SIP; prima dell'apertura = dati di ieri
j "$D/v1beta1/screener/stocks/movers?top=20"                       # idem
j "$D/v1beta1/news?symbols=NVDA,AMD&start=2026-09-16T20:00:00Z&limit=50" | jq '[.news[]|{t:.created_at,s:.symbols,h:.headline,src:.source}]'
j "$D/v1beta1/news?limit=50&start=2026-09-17T08:00:00Z"          # notizie generali della notte (utile per trovare i gap)
```

## Opzioni
```bash
j "$T/v2/options/contracts?underlying_symbols=SPY&expiration_date=2026-09-17&type=call&limit=100"
j "$D/v1beta1/options/snapshots/SPY?feed=indicative&type=call&expiration_date=2026-09-17&strike_price_gte=655&strike_price_lte=670" \
  | jq '.snapshots|to_entries|map({k:.key,bid:.value.latestQuote.bp,ask:.value.latestQuote.ap,iv:.value.impliedVolatility,d:.value.greeks.delta})'
```
Formato del simbolo OCC: `SPY260917C00660000` (sottostante, AAMMGG, C/P, strike × 1000 su 8 cifre).

## Crypto
```bash
j "$D/v1beta3/crypto/us/snapshots?symbols=BTC/USD,ETH/USD"
j "$D/v1beta3/crypto/us/bars?symbols=BTC/USD&timeframe=1Hour&start=2026-09-10T00:00:00Z&limit=200"
j "$D/v1beta3/crypto/us/latest/orderbooks?symbols=BTC/USD" | jq '.orderbooks["BTC/USD"]|{bid:.b[0],ask:.a[0]}'
j "$D/v1beta1/screener/crypto/movers?top=10"
```

## Ordini (esempi)
```bash
# Azione: ingresso stop in rottura + bracket (TP e SL sul server)
j -X POST $T/v2/orders -H 'Content-Type: application/json' -d '{
 "symbol":"NVDA","qty":"2","side":"buy","type":"stop","stop_price":"181.20",
 "time_in_force":"day","order_class":"bracket",
 "take_profit":{"limit_price":"184.40"},"stop_loss":{"stop_price":"179.60"},
 "client_order_id":"20260917-trd-orb-1"}'

# Short con bracket (TP sotto, SL sopra)
#   "side":"sell", "type":"stop","stop_price":<sotto il minimo del range>, take_profit < entry < stop_loss

# Opzione singola: limit al mid
j -X POST $T/v2/orders -H 'Content-Type: application/json' -d '{
 "symbol":"SPY260917C00660000","qty":"1","side":"buy","type":"limit","limit_price":"0.38",
 "time_in_force":"day","client_order_id":"20260917-trd-optc-1"}'

# Debit spread (multi-leg)
j -X POST $T/v2/orders -H 'Content-Type: application/json' -d '{
 "order_class":"mleg","qty":"1","type":"limit","limit_price":"0.40","time_in_force":"day",
 "legs":[
  {"symbol":"SPY260917C00660000","ratio_qty":"1","side":"buy","position_intent":"buy_to_open"},
  {"symbol":"SPY260917C00661000","ratio_qty":"1","side":"sell","position_intent":"sell_to_open"}],
 "client_order_id":"20260917-trd-dspr-1"}'
# Chiusura: stesse gambe con side invertiti e position_intent sell_to_close / buy_to_close

# Crypto: acquisto limit + stop-limit di protezione GTC (dopo il fill)
j -X POST $T/v2/orders -H 'Content-Type: application/json' -d '{"symbol":"BTC/USD","qty":"0.002","side":"buy","type":"limit","limit_price":"64000","time_in_force":"gtc","client_order_id":"20260919-cry-trend-1"}'
j -X POST $T/v2/orders -H 'Content-Type: application/json' -d '{"symbol":"BTC/USD","qty":"0.002","side":"sell","type":"stop_limit","stop_price":"62500","limit_price":"62000","time_in_force":"gtc","client_order_id":"20260919-cry-trend-1-sl"}'

# Gestione
j -X PATCH $T/v2/orders/<id> -H 'Content-Type: application/json' -d '{"stop_price":"180.40"}'   # es. stop della gamba SL a breakeven (sostituzione delle gambe dei bracket: da verificare al primo test)
j -X DELETE $T/v2/orders/<id>
j -X DELETE "$T/v2/positions/NVDA"                     # chiude una posizione
j -X DELETE "$T/v2/orders"                             # cancella TUTTI gli ordini aperti (attenzione: anche gli stop crypto!)
```

## Attenzione
- `DELETE /v2/orders` e `DELETE /v2/positions` agiscono su **tutto**, crypto comprese. Il Closer chiude simbolo per simbolo, escludendo le crypto.
- Per chiudere una posizione che ha un bracket attivo: **prima** cancella gli ordini aperti di quel simbolo (altrimenti la quantità risulta "held" e la chiusura può essere rifiutata), **poi** `DELETE /v2/positions/{symbol}`. Verifica con GET che non restino ordini o posizioni.
- Le quantità e i prezzi nel JSON vanno come stringhe. Arrotonda i prezzi al tick: 0,01 sopra 1 USD; per le opzioni 0,01 o 0,05 a seconda del contratto.
- Dopo ogni POST: `GET /v2/orders/{id}` e controlla che `status` non sia `rejected`. In caso di rifiuto, leggi il motivo e non ripetere l'ordine alla cieca.
- Timestamp in UTC (RFC3339). Il mercato apre alle 13:30Z (fino al 31/10) e alle 14:30Z (dal 2/11).
