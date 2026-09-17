# Opzioni: quando conviene, come e con quali rischi

## Cosa permette Alpaca (conto paper)
- Livello 3 attivo di default: acquisto di call e put, spread, ordini multi-leg (`order_class: "mleg"`), anche straddle, strangle e condor. [Alpaca](https://alpaca.markets/learn/how-to-trade-options-with-alpaca)
- Ordini: market, limit, stop e stop_limit (stop solo su single-leg). TIF `day` o `gtc`. Niente extended hours, solo contratti interi, niente `notional`. [Docs](https://docs.alpaca.markets/docs/options-trading)
- Scadenza: i contratti ITM vengono **esercitati automaticamente**. Se manca il buying power, Alpaca li liquida nell'ultima ora prima della scadenza. Per noi vale una regola più semplice: **tutto chiuso in giornata.**
- Dati gratuiti: feed `indicative`, con quotazioni derivate da OPRA (non reali) e trade ritardati di 15 minuti. Il feed `opra` reale è a pagamento. [Forum Alpaca](https://forum.alpaca.markets/t/what-is-the-indicative-pricing-feed-for-options/14595)
  → **Conseguenza:** usa il feed indicative per orientarti, valuta il prezzo equo con Black-Scholes sul prezzo live del sottostante e sulla IV, e invia solo ordini **limit**.

## Evidenze e avvertimenti
- **0DTE e retail:** oltre il 75% dei trade retail sulle opzioni S&P 500 è su 0DTE, e nonostante spread effettivi più bassi i retail **perdono in modo sostanziale**. [Beckmeyer, Branger, Gayda](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4404704)
- I costi (spread bid/ask) pesano molto di più che sulle azioni: uno spread di 0,05 su un'opzione da 0,50 costa il 10% all'andata e il 10% al ritorno.
- **IV crush:** dopo gli utili la volatilità implicita crolla. Comprare opzioni "per l'evento" dopo l'annuncio spesso significa pagare una IV ancora alta.
- **Theta:** una 0DTE perde valore molto in fretta durante la giornata. Il movimento deve arrivare presto.

## Quando le opzioni sono lo strumento migliore
0. **È una tesi ribassista su un singolo titolo**: con equity sotto i 2.000 USD lo short non è disponibile, quindi put o put debit spread sono l'unica via (per indici e settori si preferiscono gli ETF inversi, più economici in spread). Il premio resta dentro il tetto del mandato: se non ci sta, si rinuncia al trade.
1. Si attende un movimento **ampio e rapido** e lo stop tecnico sull'azione sarebbe troppo lontano per il capitale disponibile.
2. Il sottostante costa troppo per comprare azioni intere con il rischio consentito (ad es. titoli sopra i 300 USD).
3. Si vuole un **rischio definito** senza dipendere da uno stop che salta durante un halt.

## Strutture ammesse e come sceglierle
| Struttura | Quando | Note |
|---|---|---|
| Call/put long, 0-7 DTE | movimento forte atteso oggi | delta 0,35-0,60; theta alto; il premio è la perdita massima |
| Debit spread verticale | movimento moderato, IV alta | costa meno, e theta e vega si compensano in parte. Il guadagno massimo è la larghezza meno il debito |
| Credit spread verticale | tesi "non va oltre X" | rischio = larghezza − credito. Rischio di assegnazione anticipata sulla gamba corta (opzioni americane): chiudere in giornata |
| Straddle/strangle long | evento binario atteso **oggi** in orario di mercato | raro per noi: costoso |

## Filtri di liquidità (obbligatori)
- Spread bid/ask ≤ 10% del mid (limite di mandato); meglio ≤ 5%.
- Open interest ≥ 500 e volume di oggi > 0 sul contratto; preferire gli strike vicini al denaro.
- Sottostanti preferiti: SPY, QQQ, IWM (scadenze giornaliere), mega cap molto liquide (AAPL, NVDA, TSLA, AMZN, META, MSFT, AMD).

## Con circa 500 USD
- Premio massimo per trade: 8% dell'equity, cioè ~40 USD, cioè un premio ≤ 0,40 per un singolo contratto. Le call e put vicine al denaro su titoli liquidi costano quasi sempre di più.
- Quindi in pratica: **debit spread stretti** (larghezza 1-2 USD con debito ≤ 0,40) oppure opzioni su sottostanti più economici.
- Non comprare opzioni molto OTM solo perché sono economiche: la probabilità di profitto è bassa e lo spread in percentuale è alto.

## Esecuzione
1. Scegli la scadenza e lo strike con la catena (`/v1beta1/options/snapshots/{underlying}`), filtrando per tipo, strike e scadenza.
2. Calcola il mid e il prezzo equo teorico (vedi `strumenti/stack.md`, Black-Scholes).
3. Invia un limit al mid. Se non viene eseguito entro 1-2 minuti, avvicinati di 1 tick alla volta, al massimo 2 volte, poi rinuncia.
4. Per i multi-leg usa `order_class: "mleg"` con il `limit_price` sul debito o credito netto.
5. Uscita: target sul premio (ad es. +50/+100%) con un ordine limit di chiusura (TIF `day`), per i multi-leg un ordine `mleg` di chiusura; in alternativa gestione da parte del Position Manager. Sulle multi-leg non si possono mettere stop sul server: il rischio è già definito dal premio.
6. Il Closer chiude tutte le opzioni entro le 15:50 ET (le 0DTE entro le 15:30).

## Greche essenziali
- **Delta:** variazione del prezzo dell'opzione per 1 USD di movimento del sottostante, e anche probabilità approssimativa di finire ITM.
- **Gamma:** quanto cambia il delta. È altissimo sulle 0DTE vicine al denaro.
- **Theta:** perdita di valore per giorno. Sulle 0DTE è concentrata nelle ultime ore.
- **Vega:** sensibilità alla IV. Conta molto nei giorni di evento.
