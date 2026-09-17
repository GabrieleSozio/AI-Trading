# Strategie intraday su azioni (prima ora di contrattazione)

Qui trovi il "perché" e le evidenze dietro ogni setup. Le schede operative sono in `playbook/`.

## 1. Opening Range Breakout (ORB) sugli "Stocks in Play"
**Evidenza principale:** Zarattini, Barbon, Aziz (2024). Campione di ~7.000 azioni USA, 2016-2023. [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4729284)
- Universo: prezzo di apertura > 5 USD, volume medio a 14 giorni ≥ 1M, ATR a 14 giorni > 0,50 USD.
- "In play": volume dei primi 5 minuti ≥ 100% della media dei primi 5 minuti degli ultimi 14 giorni. Si tengono i 20 titoli con volume relativo (RVOL) più alto.
- Ingresso: ordine stop sul massimo del range dei primi 5 minuti se la prima candela è verde, sul minimo se è rossa. Nessun trade se la candela è un doji.
- Stop: **10% dell'ATR a 14 giorni** dal prezzo d'ingresso. Uscita a fine giornata.
- Dimensione: 1% di rischio per trade, leva massima 4x. Commissioni stimate a 0,0035 USD per azione.
- Risultato riportato: +1.637% netto contro +198% dell'S&P 500, Sharpe 2,81. Su tutte le azioni, senza il filtro "in play", i risultati erano molto più deboli. Il valore sta nella **selezione**.
- Il paper confronta anche range da 15, 30 e 60 minuti.

**Critiche e repliche:** replica su QuantConnect su un universo e un periodo diversi: win rate intorno al 17%, forte sensibilità ai parametri e ai costi, sospetto di overfitting e risultati variabili da un anno all'altro. [QuantConnect](https://www.quantconnect.com/research/18444/opening-range-breakout-for-stocks-in-play/)

**Come lo adattiamo:**
- Dati: con IEX il volume dei primi 5 minuti è parziale. Stima l'RVOL confrontando IEX di oggi con IEX dei giorni precedenti (stesso feed), oppure usa un range da 15 minuti. Lo storico SIP più vecchio di 15 minuti è utilizzabile per ATR e medie.
- La tua parte è **selezionare meglio**: il catalizzatore spiega il volume? È una notizia che cambia il valore dell'azienda?
- Stop al 10% dell'ATR è molto stretto: con slippage reale e feed IEX valuta tra 10% e 25% dell'ATR, oppure l'estremo opposto del range se più vicino. Registra sempre la scelta fatta.
- Uscita: nella nostra finestra niente overnight. Target a 2R o trailing sul VWAP, e chiusura comunque entro le 15:50 ET.

## 2. Gap and Go (continuazione del gap)
- Condizioni: gap ≥ 3-4% con catalizzatore forte (utili sopra le attese con guidance alzata, contratto importante, upgrade rilevante, approvazione regolatoria). Volume pre-market alto. Il titolo **tiene sopra VWAP** dopo l'apertura.
- Ingresso: rottura del massimo pre-market o del massimo del range di apertura, con volume.
- Stop: sotto VWAP o sotto il minimo del range.
- Evidenza: la PEAD (deriva post-utili) esiste ma è debole e concentrata nelle microcap; per le large cap è discussa. [UCLA Anderson Review](https://anderson-review.ucla.edu/is-post-earnings-announcement-drift-a-thing-again/) Il vantaggio sta nel riconoscere la **qualità** del catalizzatore, non nel gap in sé.

## 3. Gap Fade (riempimento del gap)
- Condizioni: gap senza catalizzatore solido (notizia vecchia, generica, "sympathy move", upgrade minore), apertura debole, rifiuto del massimo pre-market, **perdita del VWAP**.
- Ingresso: rottura del minimo del range con il prezzo sotto VWAP. Target sulla chiusura del giorno prima (gap fill parziale o totale).
- **Con questo conto lo short non è disponibile** (equity sotto i 2.000 USD): il trade si esprime con **put o put debit spread**, oppure si rinuncia. Un ETF inverso non serve qui, perché la tesi è su un singolo titolo.
- Rischi: IV alta sulle put dopo un gap, spread bid/ask larghi, SSR se il titolo è già −10%.

## 3-bis. Tesi ribassiste senza short
Finché l'equity resta sotto i 2.000 USD (vedi `knowledge/dati/alpaca-conto-e-limiti.md`), una tesi al ribasso si esegue solo così:
| Tesi | Strumento |
|---|---|
| Mercato o indice debole | ETF inverso comprato long: **SH** (S&P 500), **PSQ** (Nasdaq-100), **RWM** (Russell 2000), **DOG** (Dow). Prezzi per quota bassi, quindi adatti a un conto piccolo |
| Settore debole | put o put spread sull'ETF settoriale (XLK, XLF, XLE…), oppure ETF inverso settoriale se liquido |
| Singolo titolo debole | put o put debit spread sul titolo; se il premio supera il tetto del mandato, si rinuncia |
Attenzione: gli ETF inversi replicano **il rendimento giornaliero** invertito, quindi vanno benissimo per l'intraday e male per periodi lunghi. Il rischio si calcola sull'ATR dell'ETF inverso, non su quello dell'indice. Gli inversi a leva (SDS, QID, SQQQ) rientrano nel limite dell'1% di rischio previsto per i 3x e nella prudenza dei 2x.

## 4. VWAP Reclaim / Reject
- Il VWAP è il prezzo medio "istituzionale" della giornata. Un titolo in play che lo riconquista con volume segnala domanda; se lo perde e non lo recupera, segnala offerta.
- Utile soprattutto al Position Manager (10:30-11:30) per una seconda occasione.

## 5. Forza relativa rispetto al mercato
- Nei giorni di SPY debole, i titoli che salgono comunque (con un catalizzatore) sono i long più robusti, e viceversa per gli short.
- Misura: rendimento del titolo dall'apertura − beta × rendimento di SPY dall'apertura. Approssimazione: differenza semplice.

## 6. Cosa evitare
- **Target di M&A** (acquisizioni in contanti): il prezzo resta ancorato al prezzo d'offerta, quindi non c'è momentum.
- Small cap sotto 5 USD, float minuscoli, titoli sospesi di recente: halt, spread enormi, manipolazione.
- Le prime 1-2 candele dopo l'apertura, senza un piano.
- Titoli con utili **dopo** la chiusura di oggi: l'intraday è spesso compresso e la volatilità implicita alta.
- Ordini a mercato su titoli con spread > 0,3%.

## Metriche da registrare per setup
RVOL, gap %, tipo di catalizzatore (tassonomia sotto), posizione rispetto a VWAP, distanza dello stop in ATR, R ottenuto, MAE e MFE (massima escursione contro e a favore).

## Tassonomia dei catalizzatori (da usare nei log)
`earnings_beat_raise`, `earnings_beat_only`, `earnings_miss`, `guidance_cut`, `fda_approval`, `fda_reject`, `contract_win`, `m&a_target`, `m&a_acquirer`, `analyst_upgrade`, `analyst_downgrade`, `offering_dilution`, `macro_sector`, `sympathy`, `no_news`, `other`.
