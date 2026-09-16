# Struttura del mercato USA: cosa conta nella prima ora

## Orari (ET)
- Pre-market su Alpaca: 04:00-09:30. After-hours: 16:00-20:00. Overnight: 20:00-04:00.
- Sessione regolare: 09:30-16:00. Le opzioni su azioni seguono lo stesso orario (alcune su indici ed ETF fino alle 16:15).
- Asta di apertura: ~09:30 (NYSE opening auction / Nasdaq opening cross). Su Alpaca gli ordini OPG vanno inviati **entro le 09:28**.
- Il regolamento delle azioni è T+1.

## Come si comporta la prima mezz'ora
- **Volatilità e spread** sono i più alti della giornata (intraday ad "U"). Nei primi 1-3 minuti i prezzi sono rumorosi e gli spread larghi: evita gli ordini a mercato.
- **Stocks in play:** i titoli con catalizzatore e volume relativo alto hanno movimenti direzionali più affidabili. Su questo si basa l'ORB di Zarattini-Barbon-Aziz (vedi `strategie/azioni-intraday.md`).
- **Il gap pre-market non è una direzione garantita.** Conta come il titolo reagisce all'apertura: tiene o perde VWAP, rompe o no il range iniziale.
- **Momentum intraday di mercato:** il rendimento della prima mezz'ora dell'S&P 500 (dalla chiusura precedente) predice quello dell'ultima mezz'ora, soprattutto nei giorni volatili, con volumi alti o con dati macro. È utile al Closer per leggere la giornata. [Gao, Han, Li, Zhou – JFE](https://www.sciencedirect.com/science/article/abs/pii/S0304405X18301351)

## Meccanismi che possono bloccarti
- **LULD (Limit Up-Limit Down):** se un titolo esce dalla sua banda di prezzo, la contrattazione si ferma (in genere per 5 minuti). Le bande sono più larghe all'apertura (09:30-09:45) e in chiusura. Durante un halt gli stop non vengono eseguiti, e alla riapertura il prezzo può saltare oltre lo stop.
- **SSR (Rule 201):** se un titolo scende del 10% dalla chiusura precedente, lo short è consentito solo sopra il miglior bid per il resto della giornata e per quella successiva. Lo short su titoli in forte calo diventa difficile.
- **Circuit breaker di mercato:** pause con S&P 500 a −7% e −13%, stop totale a −20%.
- **Titoli "hard to borrow" o non shortabili:** controlla `shortable` ed `easy_to_borrow` in `GET /v2/assets/{symbol}`.

## Limiti di Alpaca da ricordare
- Bracket: ingresso market, limit o stop; TIF `day` o `gtc`; niente extended hours; **niente frazioni**.
- Trailing stop: attivo solo nella sessione regolare.
- Ordini con `notional` (frazionari): TIF solo `day`, non si possono sostituire.
- Screener movers e most-actives (dati SIP): **fino all'apertura mostrano i dati del giorno prima**, quindi non servono come scanner pre-market (vedi `dati/fonti-dati.md`).
- Conto paper: riempimenti simulati senza slippage da latenza e senza coda. Nel 10% dei casi i riempimenti sono parziali e casuali. **I risultati del paper sono ottimistici.**
- La regola PDT è stata abolita da FINRA il 04/06/2026 e Alpaca applica l'"Intraday Margin Framework". Sotto i 2.000 USD non c'è leva, quindi il potere d'acquisto coincide con l'equity.

Fonti: [Alpaca Orders](https://docs.alpaca.markets/docs/orders-at-alpaca), [Alpaca Paper](https://docs.alpaca.markets/docs/paper-trading), [FINRA RN 26-10](https://www.finra.org/rules-guidance/notices/26-10), [Alpaca Intraday Margin](https://alpaca.markets/blog/finra-retires-the-pdt-rule-introducing-alpacas-new-intraday-margin-framework/)
