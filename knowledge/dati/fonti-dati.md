# Fonti di dati gratuite (mix consigliato)

**Principio:** Alpaca è la fonte primaria per prezzi, ordini e notizie. Le altre fonti servono a **contesto, catalizzatori e conferme**.
Ogni dominio chiamato con curl deve essere nella allowlist di rete dell'ambiente cloud. La colonna "Allowlist" indica cosa aggiungere.
I limiti dei piani gratuiti cambiano spesso: le voci con (v) vanno verificate al primo test.

## 1. Mercato, prezzi, notizie
| Fonte | Cosa dà | Limiti gratuiti | Allowlist |
|---|---|---|---|
| **Alpaca Market Data** | barre, quote, snapshot (azioni IEX in tempo reale, storico SIP con 15 min di ritardo), opzioni (indicative), crypto, screener, **notizie Benzinga** | 200 richieste/min | `data.alpaca.markets` |
| **Ricerca web** (strumento WebSearch/WebFetch) | notizie dell'ultima ora, premarket movers, calendario macro, contesto | limite interno per run | nessuna (è un tool) |
| Finnhub | notizie per società, calendario utili, dati di base | ~60 chiamate/min, alcune funzioni premium (v) | `finnhub.io` |
| Alpha Vantage | serie giornaliere, alcuni indicatori, notizie con sentiment (v) | poche chiamate al giorno (v) | `www.alphavantage.co` |
| Twelve Data | serie multi-asset | ~800 chiamate/giorno, ritardi sul piano gratuito (v) | `api.twelvedata.com` |
| Yahoo Finance (non ufficiale) | quote e storici | inaffidabile, può fallire senza preavviso | sconsigliato |

Riepilogo comparativo 2026: [NextGen Nexus](https://thenextgennexus.com/2026/05/15/10-best-free-stock-market-apis-2026/). Calendari utili, target degli analisti e insider sono raramente completi nei piani gratuiti.

## 2. Scanner pre-market (il punto debole dei dati gratuiti)
Gli screener di Alpaca **mostrano i dati di ieri fino all'apertura**. Per trovare i gap:
1. Notizie Alpaca dalla chiusura di ieri (`/v1beta1/news?start=...`), estraendo i simboli più citati.
2. Ricerca web: "premarket movers today", "stocks moving premarket <data>".
3. Calendario utili (Finnhub o ricerca web "earnings before the open today").
4. Snapshot Alpaca (`feed=iex`) sui candidati trovati: prezzo pre-market rispetto alla chiusura di ieri.
5. Dopo le 9:30: screener movers e most-actives (SIP) per confermare o scoprire nuovi titoli in play.

## 3. Macro e regime
| Fonte | Cosa dà | Note | Allowlist |
|---|---|---|---|
| **FRED** (St. Louis Fed) | serie macro: VIXCLS, rendimenti Treasury (DGS10, DGS2), spread di credito, dollaro | API gratuita con chiave | `api.stlouisfed.org` |
| federalreserve.gov | calendario FOMC, comunicati | pagine ufficiali | `www.federalreserve.gov` |
| bls.gov | calendario e dati CPI e occupazione | pagine e API ufficiali | `www.bls.gov`, `api.bls.gov` |
| bea.gov | PIL, PCE | ufficiale | `www.bea.gov` |
| Cboe | storico VIX (CSV) | gratuito | `cdn.cboe.com` |
| Ricerca web | "economic calendar today" | sempre disponibile | – |

## 4. Aziende e documenti ufficiali
| Fonte | Cosa dà | Note | Allowlist |
|---|---|---|---|
| **SEC EDGAR** | 8-K, 10-Q, S-1/S-3 (diluizioni), Form 4 (insider) | gratuito; richiede un header User-Agent con un contatto | `data.sec.gov`, `efts.sec.gov`, `www.sec.gov` |
| Comunicati stampa | testo originale di utili e guidance | tramite ricerca web | – |

## 5. Crypto
| Fonte | Cosa dà | Limiti | Allowlist |
|---|---|---|---|
| **Alpaca crypto** | prezzi, barre, book, movers | incluso | `data.alpaca.markets` |
| CoinGecko (piano Demo) | prezzi, market cap, dominance, trend | ~10.000 chiamate al mese, limite al minuto (v) | `api.coingecko.com` |
| alternative.me | Crypto Fear & Greed Index | gratuito | `api.alternative.me` |
| Deribit (API pubblica) | IV delle opzioni BTC ed ETH (DVOL), funding dei perpetui | endpoint pubblici senza chiave | `www.deribit.com` |
| Hyperliquid (API info) | funding e open interest dei perpetui | pubblico, senza chiave (v) | `api.hyperliquid.xyz` |
| Kraken / Coinbase (API pubbliche) | prezzi e book di riferimento | pubbliche | `api.kraken.com`, `api.exchange.coinbase.com` |
| Binance.com | – | spesso bloccato dagli IP USA: **evitare** | – |

Confronto delle API crypto gratuite: [CoinGecko](https://www.coingecko.com/learn/best-free-crypto-api)

## 6. Sentiment e attenzione retail (usare con cautela)
- Reddit: tramite ricerca web, oppure aggregatori di menzioni (v).
- Google Trends: tramite ricerca web.
- Il sentiment è **rumoroso** e facile da manipolare: va usato come conferma, mai come unico motivo di un trade.

## 7. Regole d'uso
1. Annota sempre la **fonte** e l'**ora** del dato nel log della decisione.
2. Se due fonti sono in disaccordo sul prezzo, vale **Alpaca** (è il broker che esegue).
3. Una notizia vale solo se ha data e ora verificabili ed è di oggi (o della notte).
4. Il Coach mantiene `state/memory/sources.md`: fonti utili (+) e rumorose (−), con esempi.
