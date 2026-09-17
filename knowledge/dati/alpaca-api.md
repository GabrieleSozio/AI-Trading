# Alpaca API: guida rapida operativa

Le credenziali sono nelle variabili d'ambiente `APCA_API_KEY_ID` e `APCA_API_SECRET_KEY`. Se non ci sono, le aggiunge il proxy (API credentials). La funzione `j` gestisce entrambi i casi. **Non stampare mai le variabili.** Se una chiamata risponde 401/403, le credenziali non sono configurate: registra l'errore in `runs.csv` e **non** tentare altre strade.

```bash
T=https://paper-api.alpaca.markets      # trading (SOLO paper)
D=https://data.alpaca.markets           # dati
# usa sempre jq per filtrare; ridefinisci j in ogni comando bash (le shell non condividono le funzioni)
j() { if [ -n "${APCA_API_KEY_ID:-}" ]; then
        curl -sS --max-time 20 -H "APCA-API-KEY-ID: $APCA_API_KEY_ID" -H "APCA-API-SECRET-KEY: $APCA_API_SECRET_KEY" "$@"
      else curl -sS --max-time 20 "$@"; fi; }
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
# Azione: ingresso stop in rottura + bracket con gambe GTC (rete di sicurezza: non scadono a fine giornata)
j -X POST $T/v2/orders -H 'Content-Type: application/json' -d '{
 "symbol":"NVDA","qty":"2","side":"buy","type":"stop","stop_price":"181.20",
 "time_in_force":"gtc","order_class":"bracket",
 "take_profit":{"limit_price":"184.40"},"stop_loss":{"stop_price":"179.60"},
 "client_order_id":"20260917-trd-orb-1"}'

# Short su azioni/ETF: NON disponibile sotto 2.000 USD di equity (403 "account is not allowed to short").
# Il lato ribassista si esprime con ETF inversi long (SH, PSQ, RWM) o put / put debit spread.
# Vedi knowledge/dati/alpaca-conto-e-limiti.md.

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

# Crypto: acquisto limit + stop-limit di protezione GTC (dopo il fill; lo "stop" semplice non esiste per le crypto)
j -X POST $T/v2/orders -H 'Content-Type: application/json' -d '{"symbol":"BTC/USD","qty":"0.002","side":"buy","type":"limit","limit_price":"64000","time_in_force":"gtc","client_order_id":"20260919-cry-trend-1"}'
j -X POST $T/v2/orders -H 'Content-Type: application/json' -d '{"symbol":"BTC/USD","qty":"0.002","side":"sell","type":"stop_limit","stop_price":"62500","limit_price":"62000","time_in_force":"gtc","client_order_id":"20260919-cry-trend-1-sl"}'
```

## Gestione dell'uscita (stop che segue il prezzo)
```bash
# 1) Stop a pareggio o più stretto: PATCH della gamba SL del bracket.
#    L'id della gamba si legge dal parent con nested=true; la PATCH restituisce un id NUOVO (il vecchio va in "replaced").
j "$T/v2/orders?status=open&symbols=NVDA&nested=true" | jq '[.[]|{id,symbol,legs:[.legs[]?|{id,type,side,limit_price,stop_price,status}]}]'
j -X PATCH $T/v2/orders/<id_gamba_SL> -H 'Content-Type: application/json' -d '{"stop_price":"180.40"}'
# se la gamba e' stop_limit servono entrambi: {"stop_price":"180.40","limit_price":"180.20"}

# 2) Trailing stop (lo alza il server da solo, senza bisogno che una routine sorvegli).
#    NON può essere la gamba di un bracket: va inviato come ordine singolo, dopo aver cancellato le gambe esistenti.
j "$T/v2/orders?status=open&symbols=NVDA" | jq -r '.[].id' | while read id; do j -X DELETE $T/v2/orders/$id; done
j -X POST $T/v2/orders -H 'Content-Type: application/json' -d '{
 "symbol":"NVDA","qty":"2","side":"sell","type":"trailing_stop","trail_percent":"1.2",
 "time_in_force":"day","client_order_id":"20260917-trd-orb-1-trail"}'
# stringere il trail più tardi: j -X PATCH $T/v2/orders/<id> -d '{"trail":"0.8"}'
# hwm = massimo raggiunto dall'invio; lo stop sale con il prezzo e non scende mai. Quando scatta diventa market.

# 3) OCO su una posizione già aperta (target + stop insieme, senza nuovo ingresso)
j -X POST $T/v2/orders -H 'Content-Type: application/json' -d '{
 "symbol":"NVDA","qty":"2","side":"sell","type":"limit","time_in_force":"gtc","order_class":"oco",
 "take_profit":{"limit_price":"184.40"},"stop_loss":{"stop_price":"179.60"}}'
```
Limiti da ricordare: il trailing stop vale solo per azioni ed ETF interi (**niente crypto, niente opzioni, niente frazionari**), funziona solo in orario regolare, TIF day o gtc. La quantità di un ordine complesso non si può modificare con PATCH; la PATCH senza modifiche dà errore.

## Gestione e chiusura
```bash
j -X DELETE $T/v2/orders/<id>
j -X DELETE "$T/v2/positions/NVDA"                     # chiude una posizione
j -X DELETE "$T/v2/orders"                             # cancella TUTTI gli ordini aperti (attenzione: anche gli stop crypto!)
j -X DELETE "$T/v2/positions?cancel_orders=true"       # chiude TUTTO, crypto comprese: da non usare
```

## Attenzione
- `DELETE /v2/orders` e `DELETE /v2/positions` agiscono su **tutto**, crypto comprese. Il Closer chiude simbolo per simbolo, escludendo le crypto.
- Per chiudere una posizione che ha un bracket attivo: **prima** cancella gli ordini aperti di quel simbolo (altrimenti la quantità risulta "held_for_orders" e la chiusura risponde 403 "insufficient qty available"), aspetta lo stato `canceled`, **poi** `DELETE /v2/positions/{symbol}`. Verifica con GET che non restino ordini o posizioni.
- **Gambe GTC:** proteggono anche se una routine salta, ma uno stop che scatta diventa un ordine market: con un gap di apertura il prezzo di uscita può essere molto peggiore dello stop. Restano una rete di sicurezza, non un sostituto della chiusura intraday.
- Gli ordini non idonei all'extended hours inviati dopo le 16:00 ET partono il giorno di borsa successivo. Fuori orario sono accettati solo limit con TIF day o gtc (niente bracket né OCO).
- Le quantità e i prezzi nel JSON vanno come stringhe. Arrotonda i prezzi al tick: 0,01 sopra 1 USD (4 decimali sotto 1 USD); per le opzioni 0,01 o 0,05 a seconda del contratto.
- Dopo ogni POST: `GET /v2/orders/{id}` e controlla che `status` non sia `rejected`. In caso di rifiuto, leggi il motivo e non ripetere l'ordine alla cieca.
- Timestamp in UTC (RFC3339). Il mercato apre alle 13:30Z (fino al 31/10) e alle 14:30Z (dal 2/11).
- Vincoli di conto (short, margine, opzioni, crypto, dati): `knowledge/dati/alpaca-conto-e-limiti.md`.
