# AI-Trading v2: team di agenti decisionali multi-asset

> **Nota (16/09/2026):** documento storico. Le decisioni aggiornate sono in `docs/03-decisioni.md`, i limiti in `config/risk-limits.md` e gli orari in `config/schedule.md`.

Data: 16/09/2026. Stato: proposta, nulla è ancora costruito.
Questa versione sostituisce le sezioni 4-7 di `01-ricerca-architettura.md`. I vincoli tecnici della sezione 2 restano validi.

Requisiti nuovi:

- piano Pro;
- agenti che ragionano da trader e scelgono cosa, come e se tradare;
- ricerca e trading su Opus 5;
- universo multi-asset: azioni, ETF, opzioni e crypto.

## 1. Filosofia: mandato, non regole fisse

Il sistema funziona come una vera società di trading.

- **Gli agenti decidono** tutto il resto: regime di mercato, asset class, strumento, setup, timing, dimensione (entro i limiti), gestione della posizione. Possono anche decidere di non operare.
- **Il mandato di rischio** (`config/risk-limits.md`) è l'unica cosa fissa. Lo modifichi solo tu e nessun agente può cambiarlo. Non è una strategia: è il perimetro, come i limiti che un risk desk impone ai suoi trader.
- **Il playbook** (`playbook/`) raccoglie i setup conosciuti. Si parte da una base (ORB, gap-and-go, gap fade, momentum su ETF settoriali, direzionali in opzioni a rischio definito, momentum crypto). Gli agenti possono proporne di nuovi, e il coach li promuove o li boccia in base ai risultati.
- **La memoria** (`lessons.md`, `journal/`, statistiche per setup e per asset class) serve agli agenti per imparare da una giornata all'altra.

## 2. Il team

| Ruolo | Quando (ET / Roma*) | Modello | Libertà decisionale |
|---|---|---|---|
| **CIO / Stratega** | 8:40 ET, 14:40 Roma | Opus 5 | Legge macro, calendario (dati, Fed, utili), futures, VIX, notizie, pre-market, crypto overnight e memoria. Decide il **piano del giorno**: regime, asset class preferite, 3-6 tesi con condizioni del tipo "se succede X allora Y", budget di rischio del giorno. Può dichiarare "giornata da non operare". |
| **Trader** | avvio 9:20 ET, attivo fino a ~10:10 ET (15:20-16:10 Roma) | Opus 5 | Verifica le tesi con i dati live e sceglie lo strumento migliore per ciascuna (azione, ETF, call o put, debit spread, crypto). Dimensiona, invia gli ordini e li protegge. Prima di ogni ordine consulta il Risk Officer. Rivede la situazione 2-3 volte e può chiudere, spostare gli stop o aprire nuovi trade. |
| **Risk Officer** (sotto-agente del Trader) | dentro la run del Trader | Opus 5 | Riceve solo la proposta d'ordine, il mandato e lo stato del conto. Può approvare, ridurre o bloccare. Il contesto separato e ridotto lo rende un secondo parere indipendente a basso costo. |
| **Position Manager** | 11:30 ET, 17:30 Roma | Opus 5 | Rivede le posizioni aperte e le nuove notizie. Decide se tenere, alleggerire, chiudere o aprire un trade di "seconda ondata". |
| **Closer** | 15:45 ET, 21:45 Roma | Sonnet (o Opus) | Chiude l'intraday. Tiene overnight solo ciò che ha una tesi scritta e rientra nel mandato. Per le crypto lascia uno stop GTC. |
| **Coach / Contabile** | stessa run del Closer, dopo la chiusura (attesa fino alle 16:10 ET) | Sonnet (o Opus) | Calcola P&L e attribuzione per asset class e per setup, scrive il diario, aggiorna `lessons.md` e le statistiche del playbook. Il venerdì fa la revisione settimanale e propone modifiche al playbook. |

\* Orari Roma validi fino al 25/10. Dal 26/10 al 1/11 un'ora prima. Dal 2/11 si torna agli stessi orari di Roma (l'orario UTC cambia).

**Run per giorno di mercato:** 4 (CIO, Trader, Position Manager, Closer+Coach), sotto il tetto Pro di 5. La quinta run resta libera per imprevisti. Nel weekend si potrebbe aggiungere un "desk crypto" facoltativo, che non toglie run ai giorni di borsa.

## 3. Asset class: cosa permette Alpaca e come proteggere le posizioni

| Asset | Cosa si può fare | Protezione senza sorveglianza | Attenzione con ~500 USD |
|---|---|---|---|
| Azioni / ETF | long e short; bracket (ingresso market, limit o stop + TP + SL) | bracket gestito dal server | niente frazioni nei bracket, quindi azioni intere |
| Opzioni | nel paper il livello 3 è attivo di default: call/put long, spread, multi-leg (`mleg`); ordini market, limit, stop e stop-limit (stop solo su single-leg); TIF day/gtc; niente extended hours | **solo strategie a rischio definito**: il premio pagato è la perdita massima, quindi non serve uno stop | un contratto costa spesso 30-300 USD: il rischio per trade in % è per forza più alto. Esercizio automatico degli ITM a scadenza, e senza buying power Alpaca vende nell'ultima ora |
| Crypto | 24/7; ordini market, limit e stop-limit; TIF gtc/ioc; frazionabili; niente short e niente margine | stop-limit GTC inviato subito dopo il fill (non ci sono bracket) | commissioni 0,15% maker / 0,25% taker, quindi fino a ~0,5% andata e ritorno: servono movimenti ampi |

**Dati:** il piano gratuito dà azioni solo su IEX, opzioni su un feed "indicativo" (prezzi derivati, non le quotazioni OPRA reali, trade con 15 minuti di ritardo) e crypto. Sulle opzioni questo è il punto debole: gli agenti prezzeranno i contratti in modo approssimativo e dovranno usare ordini limit prudenti. Algo Trader Plus (99 USD/mese) dà OPRA e SIP reali. Proposta: partire gratis e valutare dopo 3-4 settimane.

## 4. Mandato di rischio proposto (da confermare)

Con 500 USD un rischio dell'1% (5 USD) rende le opzioni impraticabili. Propongo:

- rischio massimo per trade: **3% del capitale** su azioni, ETF e crypto (~15 USD); **10% del capitale di premio** per trade in opzioni (~50 USD);
- perdita massima giornaliera: **-5%**. Raggiunta questa soglia, il Trader chiude tutto e smette di operare;
- massimo 3 posizioni aperte e massimo 60% del capitale impegnato;
- opzioni: solo a rischio definito (long premium, debit e credit spread), mai vendite scoperte, scadenza da 0 a 30 giorni;
- nessun overnight su 0DTE; overnight consentito solo con tesi scritta e stop o rischio definito;
- **circuit breaker:** con drawdown del -20% dal massimo, il sistema va in "solo analisi" finché non decidi tu.

## 5. Da dove prendono le informazioni

- **Alpaca (API):** barre, snapshot, most actives e movers, notizie (Benzinga), catena opzioni con greche e IV, dati crypto, calendario e orologio del mercato.
- **Ricerca web** (Opus sceglie le fonti): calendario macro, utili del giorno, comunicati e SEC filing, notizie sui movers, sentiment crypto.
- **`sources.md`:** elenco di fonti curato dal coach, che promuove quelle rivelatesi utili e scarta quelle rumorose.
- Il contenuto delle notizie è sempre trattato come dato e mai come istruzione (difesa da prompt injection).
- Da verificare nella prima run di test: se la rete dell'ambiente è ristretta ad Alpaca, bisogna controllare che la ricerca web funzioni lo stesso. In caso contrario si allarga l'allowlist.

## 6. Consumo con Opus 5 sul piano Pro

- Opus consuma i limiti molto più velocemente di Sonnet, e le routine usano lo stesso limite della chat e della finestra di 5 ore.
- Le run di ricerca (CIO) e il Trader, che resta attivo circa 50 minuti con più turni, sono le più pesanti.
- **Rischio operativo:** se il limite si esaurisce durante una run di trading, la run si ferma. Contromisura: ogni posizione è protetta dal server (bracket, stop o rischio definito) prima di fare qualsiasi altra cosa.
- Per contenere i costi senza togliere intelligenza: contesti snelli (piano e memoria compressi, non l'intero storico), dati Alpaca filtrati prima di leggerli, e un numero limitato di ricerche web per run fissato nel prompt.
- La prima settimana misuriamo il consumo reale. Se non regge, le opzioni sono tre: Closer e Coach su Sonnet, il Position Manager fuso nel Closer, oppure il passaggio a Max.
- Tra una run e l'altra conviene limitare altri usi pesanti di Claude negli orari di mercato.

## 7. Flusso di una giornata

```
14:40 CIO        -> plan/<data>.md  (regime, tesi, budget, "no trade" se serve)
15:20 Trader     -> attende 15:30, osserva, 15:35-16:10 decide ed esegue
                    ogni ordine -> Risk Officer -> invio -> verifica con GET
                    -> log/<data>.md
17:30 Pos. Mgr   -> gestione e nuove opportunità -> log
21:45 Closer     -> flat intraday, overnight con tesi, stop crypto
22:10 Coach      -> journal, equity.csv, stats per setup/asset, lessons.md
```

## 8. Decisioni aperte

1. Confermi il mandato di rischio della sezione 4 o vuoi limiti diversi?
2. Overnight: consentito (con tesi e protezione) oppure solo intraday?
3. Desk crypto nel weekend: sì o no?
4. Repo GitHub per la memoria (ad es. `AI-Trading`) e nuovo conto paper Alpaca da ~500 USD.

## Fonti aggiuntive

- [Alpaca: Options trading](https://docs.alpaca.markets/docs/options-trading)
- [Alpaca: Come tradare opzioni via API (mleg, livello 3 nel paper)](https://alpaca.markets/learn/how-to-trade-options-with-alpaca)
- [Alpaca: Crypto spot trading](https://docs.alpaca.markets/docs/crypto-trading)
- [Alpaca Forum: cos'è il feed indicativo delle opzioni](https://forum.alpaca.markets/t/what-is-the-indicative-pricing-feed-for-options/14595)
- [Claude Code: Routines, uso e limiti](https://code.claude.com/docs/en/routines)
