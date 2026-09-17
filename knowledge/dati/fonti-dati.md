# Fonti di dati gratuite (mix consigliato)

**Principio:** Alpaca è la fonte primaria per prezzi, ordini e notizie. Le altre fonti servono a **contesto, catalizzatori e conferme**.
Ogni dominio chiamato con curl deve essere nella allowlist di rete dell'ambiente cloud. La colonna "Allowlist" indica cosa aggiungere.
I limiti dei piani gratuiti cambiano spesso: le voci con (v) vanno verificate al primo test.

## 1. Mercato, prezzi, notizie
**Verificato il 17/09/2026: nessuna fonte gratuita batte Alpaca sui prezzi.** Nessun piano gratuito offre il consolidato (SIP) in tempo reale né open interest e greche delle opzioni. Le alternative servono solo come riserva o per le notizie.

| Fonte | Cosa dà | Limiti gratuiti (2026) | Allowlist |
|---|---|---|---|
| **Alpaca Market Data** | barre, quote, snapshot (azioni IEX in tempo reale, storico SIP con 15 min di ritardo), opzioni (indicative), crypto, screener, **notizie Benzinga** | 200 richieste/min | `data.alpaca.markets` |
| **SEC EDGAR** | 8-K, 424B5, 13D, Form 4 — vedi `knowledge/dati/sec-edgar.md` | 10 richieste/s, serve header User-Agent | `www.sec.gov`, `data.sec.gov`, `efts.sec.gov` |
| **Ricerca web** (WebSearch/WebFetch) | notizie dell'ultima ora, movers pre-market, contesto | limite interno per run | nessuna (è un tool) |
| Finnhub | notizie per società, calendario utili, quote di riserva | ~60 chiamate/min; licenza **solo uso personale** | `finnhub.io` |
| Tiingo | notizie (3 mesi di storico), quote IEX | 50/ora, 1.000/giorno, 500 simboli/mese; uso personale | `api.tiingo.com` |
| RSS dei comunicati (PR Newswire, Business Wire, GlobeNewswire) | comunicati originali, anche su titoli piccoli che Benzinga salta | pubblici, senza chiave | `www.prnewswire.com`, `www.businesswire.com`, `www.globenewswire.com` |

**Da non usare (verificato, per non perderci tempo):** Polygon (ora "Massive": il piano gratuito dà solo dati di fine giornata, 5 chiamate/min) · Alpha Vantage (25 richieste al **giorno**) · EODHD (20 al giorno) · marketstack (100 al **mese**) · Financial Modeling Prep (solo ~87 simboli) · Intrinio (sandbox, vietato in produzione) · NewsAPI.org (24 ore di ritardo) · marketaux · Yahoo Finance non ufficiale · finvizfinance (il `robots.txt` di Finviz vieta proprio gli endpoint che usa).

**Licenze:** Finnhub, Tiingo e Twelve Data vietano l'uso commerciale nel piano gratuito. Per un conto paper personale non è un problema; se un giorno si passa a capitale reale, va riletto il contratto.

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
| **SEC EDGAR** | 8-K (risultati, cambi di CEO/CFO), **424B5 e offerte ATM = diluizione**, 13D attivisti, Form 4 insider | gratuito, senza chiave, appare entro secondi dal deposito. Ricette pronte e regole d'uso in `knowledge/dati/sec-edgar.md` | `www.sec.gov`, `data.sec.gov`, `efts.sec.gov` |
| Comunicati stampa | testo originale di utili e guidance | RSS dei circuiti sopra, o ricerca web | – |

## 4-bis. Struttura del mercato e calendari (gratis, senza chiave)
| Fonte | Cosa dà | Come si usa | Allowlist |
|---|---|---|---|
| **Halt Nasdaq (RSS)** `http://www.nasdaqtrader.com/rss.aspx?feed=tradehalts` | blocchi di negoziazione in corso, con motivo e ora di riapertura | **protezione, non segnale**: se un titolo è in halt non si invia niente e si rivede la tesi alla riapertura. Non esiste evidenza seria di momentum post-halt | `www.nasdaqtrader.com` |
| **Calendario utili Nasdaq** `https://api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD` | chi pubblica oggi e domani, prima o dopo la chiusura | evita di entrare su titoli con utili in serata; spiega i gap del mattino. Endpoint non ufficiale: se cambia, si passa a Finnhub | `api.nasdaq.com` |
| **Calendario FDA (PDUFA)** `https://www.pdufa.bio/api/v1` | date di decisione sui farmaci | solo se si valuta una biotech: sono gap da 30-50%, quasi sempre da evitare | `www.pdufa.bio` |
| Curva dei rendimenti Treasury (CSV) | tassi 2 e 10 anni | contesto di regime | `home.treasury.gov` |
| Cboe (CSV) | storico VIX, rapporto put/call | solo contesto: il put/call **pubblico** non ha potere predittivo (Pan-Poteshman) | `cdn.cboe.com` |
| Short interest (Nasdaq/NYSE, bisettimanale) | quante azioni sono vendute allo scoperto, giorni per ricoprire | filtro di rischio, non segnale | `api.nasdaq.com` |

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

## 6. Sentiment e attenzione retail (solo come veto)
- Reddit e StockTwits: tramite ricerca web. L'evidenza (Barber-Huang-Odean-Schwarz, *Journal of Finance* 2022, sui dati Robinhood) dice che dopo un picco estremo di attenzione i rendimenti successivi sono **negativi** (circa −4,7% in 20 giorni nei casi più forti).
- Uso corretto: **veto**, non segnale. Se un titolo è in cima alle menzioni con un'esplosione improvvisa, non lo si insegue al rialzo.
- Google Trends: stessa logica, solo contesto.

## 7. Regole d'uso
1. Annota sempre la **fonte** e l'**ora** del dato nel log della decisione.
2. Se due fonti sono in disaccordo sul prezzo, vale **Alpaca** (è il broker che esegue).
3. Una notizia vale solo se ha data e ora verificabili ed è di oggi (o della notte).
4. Il Coach mantiene `state/memory/sources.md`: fonti utili (+) e rumorose (−), con esempi.
5. **Prima di aggiungere una fonte nuova**, chiediti se cambierebbe una decisione. Una fonte che non cambia mai una decisione costa token e basta.

## 8. Segnali valutati e scartati (verificato il 17/09/2026)
Non spendere token su questi: la ricerca dice che non funzionano, o che con dati gratuiti arriviamo tardi.
| Segnale | Perché no |
|---|---|
| Put/call ratio pubblico, "unusual options activity", gamma delle 0DTE | il put/call osservabile non predice (Pan-Poteshman, *RFS* 2006); il posizionamento sui 0DTE risulta bilanciato negli studi Cboe; il resto è materiale commerciale |
| Momentum dopo un halt | nessuno studio serio sulle azioni USA; solo aneddotica |
| Giorni con SSR attiva | tre studi indipendenti trovano effetti trascurabili sui prezzi: l'informazione ("ieri −10%") è già nel prezzo |
| Upgrade e target degli analisti | con i timestamp veri la reazione finisce in pochi minuti (Bradley et al., *JF* 2014): con dati gratuiti siamo strutturalmente in ritardo |
| Volume short giornaliero FINRA | esce dopo la chiusura, metà è copertura dei market maker, effetto misurato ~3 punti base |
| Flusso ordini (OFI, VPIN) su IEX | IEX vede il 2-3% del volume e per costruzione attira il flusso **meno** informato: campione fuorviante |
| 13F dei fondi, inserimenti negli indici | trimestrali e in ritardo i primi, effetto ormai svanito i secondi |
