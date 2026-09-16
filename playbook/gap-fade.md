# gap-fade — Riempimento del gap senza catalizzatore
- **stato:** sperimentale | **asset:** azioni (short) o put / put debit spread | **finestra:** 09:45-11:00 ET
- **condizioni:** gap ≥ 3% con catalizzatore debole o assente (`no_news`, `sympathy`, upgrade minore); rifiuto del massimo pre-market; perdita del VWAP con volume.
- **ingresso:** rottura del minimo del range con il prezzo sotto VWAP.
- **stop:** sopra VWAP o sopra il massimo del giorno.
- **uscita:** chiusura di ieri (gap fill) o 2R.
- **vincoli:** titolo shortabile ed easy_to_borrow; attenzione alla SSR se il titolo è già −10% (in quel caso preferire le put).
- **da registrare:** gap %, catalizzatore, % del gap riempito, R.
