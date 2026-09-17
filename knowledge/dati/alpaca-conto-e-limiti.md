# Alpaca: cosa permette davvero questo conto (verificato 17/09/2026)

Scheda di riferimento sui vincoli reali del conto paper attuale (~550 USD, dati Basic gratuiti). Le fonti sono i documenti ufficiali Alpaca e FINRA. Rileggila prima di scartare una tesi per motivi "di conto": molti vincoli che sembrano ovvi qui non valgono.

## 1. Margine e vendite allo scoperto
- Tutti i conti Alpaca nascono come **margin account**. L'accesso a margine e short si sblocca con **equity ≥ 2.000 USD** (soglia in dollari, calcolata sull'equity **corrente**, non sul deposito iniziale). Sotto: buying power 1x, `shorting_enabled=false`, ogni ordine short risponde **403 "account is not allowed to short"**. [account-plans](https://docs.alpaca.markets/us/docs/account-plans) · [margin-and-short-selling](https://docs.alpaca.markets/us/docs/margin-and-short-selling)
- Il conto paper replica la regola: paper supporta margine e short esattamente come il live. [paper-trading](https://docs.alpaca.markets/docs/paper-trading)
- Se l'equity scende di nuovo sotto i 2.000 USD, leva e short si disattivano (e si riattivano risalendo). Non è documentato se il controllo sia intraday o di fine giornata: **incerto**.
- Con equity sufficiente servono comunque: `no_shorting=false`, `max_margin_multiplier>1` e, sul simbolo, `shortable` ed `easy_to_borrow` (circa il 35% degli asset; lista aggiornata ogni giorno). Gli ordini short **frazionari** non esistono.
- Margine di mantenimento sugli short: il maggiore tra 5 USD/azione e il 30% sopra i 5 USD; ETF 2x → 50%, ETF 3x → 75%.
- **Conclusione operativa (equity 550 USD):** nessuno short su azioni ed ETF. Il lato ribassista si esprime solo con **ETF inversi** (SH, PSQ, RWM, comprati long) o **put / put debit spread**.

## 2. Day trading: la regola PDT non esiste più
- FINRA ha ritirato la Pattern Day Trader e l'ha sostituita con l'**Intraday Margin Rule**, efficace dal **4 giugno 2026**: niente soglia dei 25.000 USD, niente conteggio dei day trade. [FINRA 26-10](https://www.finra.org/rules-guidance/notices/26-10)
- Alpaca l'ha adottata: la leva intraday 4x richiede 2.000 USD, e dal **6 luglio 2026** i campi `pattern_day_trader`, `daytrade_count` e `daytrading_buying_power` sono stati **rimossi dall'API** (si usa `buying_power`). [blog Alpaca](https://alpaca.markets/blog/finra-retires-the-pdt-rule-introducing-alpacas-new-intraday-margin-framework/) · [intraday margin rule](https://docs.alpaca.markets/us/docs/the-intraday-margin-rule)
- Alpaca **non offre conti cash**: i conti sotto i 2.000 USD sono "limited margin" e possono operare su fondi non ancora regolati. Quindi **niente vincolo T+1, niente good faith violation, niente free riding**: lo stesso capitale si può riusare più volte nella stessa giornata. [cash accounts](https://alpaca.markets/support/alpaca-cash-accounts)
- **Correzione importante:** il log del 17/09/2026 dava per scontato il regolamento T+1 come vincolo. È sbagliato. Il vincolo vero è solo il **capitale nominale**: con 550 USD e titoli sopra i 100 USD si tiene di fatto una posizione per volta, ma si possono fare più giri in sequenza nello stesso giorno.

## 3. Restrizione automatica
Alpaca blocca il conto se una singola posizione supera il **600% dell'equity**. Con il nostro limite di esposizione lorda ≤ 100% non è un problema. [user-protection](https://docs.alpaca.markets/us/docs/user-protection)

## 4. Azioni ed ETF
- **Frazionari:** da 1 USD, con market/limit/stop/stop_limit ma **solo `tif=day`**, e senza trailing stop. [fractional-trading](https://docs.alpaca.markets/docs/fractional-trading)
- **Extended hours:** solo ordini `limit` con TIF day o gtc. Bracket e OCO **non** sono ammessi fuori orario.
- **Overnight 24/5** (domenica 20:00 → venerdì 04:00 ET): solo limit, solo asset con `overnight_tradable=true`, feed `overnight` gratuito. Non lo usiamo: il mandato vieta le posizioni notturne. [245-trading](https://docs.alpaca.markets/us/docs/245-trading-for-trading-api)

## 5. Opzioni
- Livelli 0-3, non esiste il livello 4 (niente vendite scoperte). Nei conti **paper le opzioni sono attive di default**. [options-trading](https://docs.alpaca.markets/us/docs/options-trading)
- Commissioni Alpaca **0 USD** per contratto; restano le fee regolatorie (ORF 0,015, OCC 0,025, TAF 0,00329 per contratto; indici +0,50).
- **Auto-liquidazione delle posizioni in scadenza a partire dalle 15:30 ET.** Cutoff per le 0DTE: 15:15 ET, 15:30 per SPY e QQQ. Le nostre regole (0DTE chiuse entro le 15:30) restano prudenti: meglio 15:00.
- Esercizio automatico ITM da 0,01 USD.
- Multi-leg (`order_class="mleg"`): massimo 4 gambe, solo market o limit, `qty` intera, niente gambe azionarie; con il livello 3 tutte le gambe devono stare nello stesso ordine.
- **Niente bracket, OCO, OTO né trailing stop sulle opzioni.** `stop` e `stop_limit` solo su ordini a una gamba. Il rischio è definito dal premio pagato: la protezione è la struttura stessa.

## 6. Crypto
- 24/7, tutto frazionabile, taglio minimo tipico 0,0001 BTC, massimo 200.000 USD di nozionale per ordine, fee maker/taker 15/25 bps (tier 1). [crypto-trading](https://docs.alpaca.markets/us/docs/crypto-trading)
- **Niente margine, niente short, niente uso come collaterale.**
- Tipi ammessi: market, limit, **stop_limit** (lo `stop` semplice non c'è). TIF: gtc o ioc. Nessun bracket, OCO o trailing.

## 7. Dati (piano Basic gratuito)
- Azioni: feed **IEX** in tempo reale; SIP storico disponibile ma **escluso l'ultimo quarto d'ora**.
- **200 richieste/minuto**; websocket: 1 connessione, 30 simboli.
- Opzioni: feed "indicative" (200 quote in streaming).
- News e screener (movers, most-actives) inclusi.

## 8. Cosa il paper NON simula
Dividendi, slippage, impatto di mercato, posizione nella coda degli ordini, fee regolatorie, interessi e costi di prestito sugli short. I fill parziali sono casuali (circa 10%) e può eseguire oltre la liquidità reale. Le statistiche del paper sono quindi **ottimistiche**: tenerne conto nelle revisioni del Coach. [paper-trading](https://docs.alpaca.markets/docs/paper-trading)

## 9. Se un giorno si passa a 2.000 USD
- 2.000 EUR valgono circa **2.300 USD** (cambio BCE 16/09/2026: 1 EUR = 1,1537 USD), quindi sopra la soglia — ma con soli ~300 USD di margine: basta un −13% per perdere short e leva. **Consigliato aprire il conto paper con 2.500-3.000 USD.**
- Il saldo di un conto paper non si modifica: si crea un **nuovo conto paper** con il saldo voluto e si aggiornano le chiavi nell'ambiente.
- Dopo il cambio, verificare via API `shorting_enabled=true` e `multiplier ≥ 2`, e controllare `shortable` ed `easy_to_borrow` sul simbolo prima di ogni short.
- Il mandato di rischio andrà riscalato sul nuovo capitale (i limiti sono in percentuale, ma le soglie in dollari cambiano).

## 10. Nota per i residenti UE
Il Trading API resta un conto **statunitense in USD** (Alpaca Securities, modulo W-8BEN). Alpaca Europe (dal 2026) è solo Broker API B2B: non esistono conti retail in euro. [live-trading-account-non-us](https://alpaca.markets/learn/live-trading-account-non-us)
