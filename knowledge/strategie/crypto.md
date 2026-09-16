# Crypto su Alpaca

## Regole della piattaforma
- Mercato aperto 24/7. Ordini market, limit e stop_limit; TIF `gtc` o `ioc`. **Niente bracket.** [Docs](https://docs.alpaca.markets/docs/crypto-trading)
- Niente margine e **niente short**: si può solo comprare e rivendere.
- Tutte le crypto sono frazionabili. Ordine massimo 200.000 USD di controvalore.
- **Commissioni** (fascia fino a 100k USD di volume mensile): 0,15% maker e 0,25% taker, addebitate sull'asset ricevuto. Un giro completo con ordini a mercato costa circa lo **0,5%**.
  → Evita i trade che puntano a meno dell'1-1,5% lordo. Preferisci ordini limit (maker) quando non serve immediatezza.
- Dati: `/v1beta3/crypto/us/...` (barre, quote, snapshot, order book), inclusi nel piano gratuito.

## Protezione (obbligatoria, perché le posizioni restano aperte senza sorveglianza)
Subito dopo l'esecuzione dell'acquisto, invia un **stop_limit di vendita GTC** con `stop_price` sul livello di invalidazione e `limit_price` un po' più basso (ad es. −0,5% o −1% sotto lo stop), così è eseguibile anche con un movimento rapido. Poi verificalo con GET.
Rischio: in un crollo veloce il prezzo può saltare oltre il limit e l'ordine restare non eseguito. Per questo la dimensione deve tenere conto di uno scenario peggiore (stop × 1,5).

## Evidenze utili
- **Stagionalità oraria di BTC:** rendimenti medi positivi e significativi intorno alle 22:00-23:00 UTC, quando le borse tradizionali sono chiuse. Studio su un solo exchange (Gemini, 2015-2022), senza test fuori campione: da trattare come indizio, non come regola. [Quantpedia](https://quantpedia.com/are-there-seasonal-intraday-or-overnight-anomalies-in-bitcoin/)
- **Trend intraday di BTC (2018-2025):** una strategia long/short di trend-following ha ottenuto uno Sharpe lordo di circa 1,6, contro 0,8 del buy & hold. La componente più forte parte la **domenica verso le 19:00 di New York** e dura circa 24 ore (effetto "apertura dell'Asia del lunedì"); la domenica mattina USA invece è laterale e mean-reverting. [Concretum](https://concretumgroup.com/seasonality-in-bitcoin-intraday-trend-trading/)
  → Per il desk del weekend: la domenica sera è la finestra in cui i trend tendono a partire. Noi possiamo solo andare long, quindi conviene entrare solo con un trend rialzista confermato.
- **Momentum di serie storica** su orizzonti di 1-4 settimane e ruolo dell'attenzione degli investitori: Liu e Tsyvinski, "Risks and Returns of Cryptocurrency" (Review of Financial Studies, 2021).
- **Macro e azionario:** durante la sessione USA, BTC ed ETH sono spesso correlate con il Nasdaq, e i dati macro delle 08:30 ET le muovono.

## Indicatori di contesto (gratuiti, vedi `dati/fonti-dati.md`)
- Funding rate e open interest dei perpetui: funding molto positivo indica long affollati e rischio di flush; funding negativo indica short affollati e rischio di squeeze.
- Crypto Fear & Greed Index (alternative.me): gli estremi segnalano sentiment esagerato.
- Volatilità implicita BTC (DVOL di Deribit).
- Dominance di BTC e andamento di ETH/BTC: dicono se il mercato è in fase risk-on (altcoin forti) o difensiva.

## Approccio consigliato
- Universo: BTC/USD, ETH/USD, SOL/USD e poche altre molto liquide disponibili su Alpaca. Verifica con `GET /v2/assets?asset_class=crypto`.
- Setup: trend con pullback su timeframe 1h-4h, breakout da range con volume, uso delle fasce orarie favorevoli.
- Tempo di detenzione: da ore a qualche giorno (le crypto sono l'unico asset che può restare aperto overnight).
- Esposizione massima: 50% dell'equity (mandato).
