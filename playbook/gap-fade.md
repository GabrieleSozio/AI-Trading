# gap-fade — Riempimento del gap senza catalizzatore
- **stato:** sperimentale | **asset:** put o put debit spread (lo short di azioni non è disponibile sotto i 2.000 USD di equity) | **finestra:** 09:45-11:00 ET
- **condizioni:** gap ≥ 3% con catalizzatore debole o assente (`no_news`, `sympathy`, upgrade minore); rifiuto del massimo pre-market; perdita del VWAP con volume.
- **ingresso:** rottura del minimo del range con il prezzo sotto VWAP.
- **stop:** sopra VWAP o sopra il massimo del giorno.
- **uscita:** chiusura di ieri (gap fill) o 2R.
- **vincoli:** il premio della put deve stare nel tetto del mandato e lo spread bid/ask sotto il 10% del mid; altrimenti si rinuncia e si registra `no_trade`. Se un giorno l'equity superasse i 2.000 USD, torna possibile lo short con bracket su titoli `shortable` ed `easy_to_borrow` (occhio alla SSR sotto il −10%).
- **da registrare:** gap %, catalizzatore, % del gap riempito, R.
