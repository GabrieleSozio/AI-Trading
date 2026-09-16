# Strategie intraday su ETF

## Perché gli ETF
- Tesi su mercato, settore o fattore, senza il rischio del singolo titolo.
- Liquidità altissima (SPY, QQQ, IWM, DIA, XLK, XLF, XLE, XLV, SMH, TLT, GLD) e spread minimi.
- Prezzi alti (SPY sopra i 500 USD): con ~500 USD di capitale e niente frazioni nei bracket, spesso servono ETF con prezzo per quota più basso sullo stesso indice (ad es. QQQM per il Nasdaq-100; per l'S&P 500 verifica il ticker attuale degli ETF "low price"), oppure le opzioni.

## 1. Momentum intraday su SPY ("Noise Area")
**Evidenza:** Zarattini, Aziz, Barbon (2024), "Beat the Market". [SSRN](https://ssrn.com/abstract=4824172)
- Si calcola una "zona di rumore" attorno all'apertura, basata sulla volatilità media di ogni minuto della giornata (misurata dall'apertura) nei giorni precedenti.
- Si entra quando il prezzo esce dalla zona (long sopra, short sotto), controllando a intervalli regolari.
- Il VWAP fa da trailing stop, la dimensione segue un target di volatilità, e a fine giornata si chiude tutto.
- Risultati riportati: Sharpe alto e hit ratio intorno al 43%. Una recensione critica segnala l'assenza di test di significatività e di costi realistici. [Recensione](https://quantmacro.substack.com/p/paper-review-an-effective-intraday)
- **Uso per noi:** nei primi 30-60 minuti, se SPY o QQQ escono chiaramente dalla "noise area" con volume, il trend della giornata tende a continuare. Serve anche come **filtro di regime** per i trade su singoli titoli.

## 2. Momentum di mercato: prima e ultima mezz'ora
Il rendimento della prima mezz'ora (dalla chiusura precedente) predice quello dell'ultima mezz'ora, e l'effetto è più forte nei giorni volatili o con dati macro. Il backtest pubblico è modesto (Sharpe ~0,4), quindi va usato come **informazione di contesto**, non come strategia autonoma. [Gao et al.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2440866), [PapersWithBacktest](https://paperswithbacktest.com/strategies/market-intraday-momentum)

## 3. Rotazione settoriale intraday
- La mattina conviene confrontare i rendimenti degli ETF settoriali (XLK, XLF, XLE, XLV, XLI, XLY, XLP, XLU, XLB, XLRE, XLC) rispetto a SPY.
- I settori guidati da notizie macro della giornata (petrolio → XLE, tassi → XLF e XLU, semiconduttori → SMH) offrono trend più puliti.

## 4. Reazione ai dati macro (08:30 ET: CPI, occupazione, PPI)
- Il dato esce prima dell'apertura: il gap di SPY o QQQ incorpora la sorpresa. Nella prima mezz'ora conta se il mercato **conferma** (tiene il gap) o **rifiuta** (lo riempie).
- Nei giorni FOMC (comunicato alle 14:00 ET) la mattina è spesso compressa: dimensioni ridotte, e nessun trade aperto verso le 14:00 visto che siamo flat prima. Il noto "pre-FOMC drift" (Lucca e Moench) secondo studi successivi si è attenuato. [NY Fed](https://www.newyorkfed.org/research/staff_reports/sr512.html)

## 5. ETF a leva (TQQQ, SQQQ, SOXL…)
- Si possono usare solo intraday, con rischio calcolato sul movimento reale (circa 3 volte il sottostante).
- Il decadimento da ribilanciamento conta poco nell'intraday, ma le escursioni sono ampie: lo stop va messo in base all'ATR dell'ETF a leva, non a quello del sottostante.
- Il mandato limita il rischio all'1% quando si usano ETF 3x.
