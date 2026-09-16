# AI-Trading: ricerca e proposta di architettura

> **Nota (16/09/2026):** documento storico. Le decisioni aggiornate sono in `docs/03-decisioni.md`, i limiti in `config/risk-limits.md` e gli orari in `config/schedule.md`.

Data: 16/09/2026. Stato: proposta, niente è stato ancora costruito.

## 1. Cosa mi hai chiesto

- Un "team" di routine cloud che si comporta come una piccola società di investimento, con un flusso tutto AI: le decisioni le prende Claude, niente logica Python deterministica.
- Conto paper Alpaca con saldo iniziale di circa 500 EUR (Alpaca ragiona in USD).
- Operatività concentrata nei primi ~30 minuti dopo l'apertura USA, per consumare pochi crediti.
- Obiettivo: un piccolo profitto quasi ogni giorno, da confrontare con i tuoi bot Python.

Nota sul contesto: tra le routine cloud del tuo account ci sono solo `Visitors-Daily` e `Visitors-Weekley`, tutte e due in pausa. Le vecchie routine di trading che citi non compaiono. Probabilmente erano attività locali dell'app desktop, che da qui non vedo. Ho comunque ripreso il loro schema: prompt autonomo, repo GitHub come memoria, commit a fine run.

## 2. Vincoli che decidono l'architettura

| Vincolo | Dettaglio | Conseguenza |
|---|---|---|
| Limite giornaliero di run | Secondo fonti di terze parti (aprile 2026): Pro 5 run/giorno, Max 15. Il valore aggiornato è su claude.ai/code/routines | Il team deve stare in circa 5 run per giorno di mercato se hai Pro |
| Run una tantum | Le run programmate una sola volta non contano nel limite giornaliero, ma consumano l'uso normale | Utili per test e per cambi di orario, non come trucco per aggirare il limite |
| Intervallo minimo | Un'ora per singola routine | Niente polling ogni 5 minuti: più routine distinte a orari diversi, oppure una sola run che aspetta con `sleep` |
| Ritardo di avvio | Le run possono partire con qualche minuto di ritardo; lo scarto è costante per ogni routine | Non si può contare su un avvio alle 9:35:00 esatte: il trader parte prima e aspetta l'orario giusto usando l'orologio di Alpaca |
| Memoria | Ogni run è una sessione nuova, senza ricordi delle precedenti | Serve uno stato condiviso: repo GitHub per piano, diario e lezioni, e Alpaca come fonte di verità per ordini e posizioni |
| Cartella locale | Le routine cloud non vedono `E:\...\AI-Trading` | La cartella resta per documenti e clone locale; il cervello condiviso sta su GitHub |
| Chiavi API | Su Pro/Max si possono salvare "API credentials" nell'ambiente cloud: il proxy aggiunge gli header e Claude non vede mai le chiavi | Header `APCA-API-KEY-ID` e `APCA-API-SECRET-KEY` per `paper-api.alpaca.markets` e `data.alpaca.markets`, con accesso di rete Custom solo verso questi host |
| MCP Alpaca | Esiste un server MCP ufficiale, ma solo locale (stdio/uvx) e vuole le chiavi nelle variabili d'ambiente | Meglio chiamate REST dirette con curl: resta tutto AI, senza script con logica, e le chiavi restano nascoste |
| Regola PDT | FINRA l'ha abolita dal 4 giugno 2026 (Regulatory Notice 26-10). Alpaca applica il nuovo "Intraday Margin Framework" | Niente più limite di 4 day trade. Sotto i 2.000 USD il conto non ha leva: il potere d'acquisto è il cash. Da verificare che il conto paper si comporti allo stesso modo |
| Dati gratuiti | Il piano Basic dà in tempo reale solo il feed IEX (una piccola quota del volume); lo storico SIP è libero solo se più vecchio di 15 minuti | Volume relativo e opening range del giorno calcolati su IEX sono approssimativi. Algo Trader Plus (99 USD/mese) dà il SIP completo; ha senso solo se la strategia mostra un vantaggio |
| Ordini | Bracket con ingresso market, limit o stop, TIF day/gtc, niente extended hours. I bracket non accettano azioni frazionarie. Il trailing stop scatta solo durante l'orario regolare | Con 500 USD servono azioni intere, quindi titoli tra circa 5 e 100 USD e al massimo 2-3 posizioni |
| Paper vs reale | Il paper non simula slippage, impatto sul mercato e coda degli ordini; il 10% delle volte fa riempimenti parziali casuali | I risultati del paper saranno più ottimistici di quelli reali |

## 3. Principio chiave: l'AI decide, Alpaca esegue

Un LLM è lento (ogni decisione richiede decine di secondi) e costoso se lo si fa girare in continuo. Per questo:

1. L'AI lavora nei momenti di giudizio: capire le notizie, scegliere i titoli, definire il piano e rivedere i risultati.
2. L'esecuzione e le uscite le fa il server di Alpaca con ordini bracket (ingresso stop, take profit, stop loss) decisi dall'AI. Se la sessione si blocca, le posizioni restano comunque protette.
3. Nessuna sorveglianza continua: poche run brevi, in momenti precisi.

In più, qui l'AI ha un vantaggio vero sul Python deterministico: legge e valuta i catalizzatori (utili, guidance, FDA, M&A, upgrade o downgrade) e scarta i gap "sporchi". È questa la parte da mettere alla prova contro i tuoi bot.

## 4. Strategia consigliata: ORB sugli "Stocks in Play" con filtro AI sui catalizzatori

Base con riscontri pubblicati: Zarattini, Barbon e Aziz (2024), "A Profitable Day Trading Strategy For The U.S. Equity Market". È un opening range breakout a 5 minuti sui 20 titoli con volume relativo più alto. Nel periodo 2016-2023 riportano un rendimento netto oltre il 1.600% e uno Sharpe di 2,81, ma con leva e uscita a fine giornata. Altre repliche mostrano circa il 17% di trade vincenti, costi che pesano molto e risultati molto variabili da un anno all'altro.

Adattamento per questo progetto:

- **Universo:** titoli USA liquidi tra 5 e 100 USD, con gap in pre-market e un catalizzatore reale di giornata.
- **Selezione (AI):** 3-6 candidati ordinati per qualità del catalizzatore e volume relativo; esclusi i titoli senza notizie o con notizie ambigue.
- **Opening range:** 5 minuti (9:30-9:35 ET), oppure 15 minuti. I 15 minuti reggono meglio il ritardo di avvio e il rumore del feed IEX: li proporrei come primo test.
- **Ingresso:** ordine stop sopra il massimo del range (long) se la candela del range è verde, sotto il minimo (short) se è rossa. All'inizio consiglio solo long: con conti piccoli e nel paper lo short è più delicato.
- **Stop:** estremo opposto del range, oppure una frazione dell'ATR a 14 giorni; va scelto quello più stretto e sensato.
- **Target:** 2R, cioè il doppio del rischio. La variante "tieni fino a fine giornata" è quella del paper accademico.
- **Dimensione:** rischio dell'1% del conto per trade (circa 5 USD), con al massimo 2-3 posizioni aperte e mai più del 50% del cash su un singolo titolo.
- **Uscita a tempo:** gli ordini non eseguiti si cancellano alle 10:00-10:15 ET. Le posizioni aperte si chiudono all'orario scelto (vedi le varianti nella sezione 6).
- **Limiti di giornata:** stop di giornata a -2%; niente nuovi ingressi dopo +1,5% se sei già in profitto. È un guardrail, non una promessa di profitto.

Aspettativa realistica: un ORB sano perde spesso poco e guadagna ogni tanto molto. Un "piccolo profitto ogni giorno" non è una distribuzione realistica per nessuna strategia intraday. Gli studi sui day trader retail sono molto negativi: in Brasile il 97% di chi ha insistito per più di 300 giorni ha perso. La valutazione va fatta su 40-60 giorni di mercato, confrontando con i tuoi bot Python e con SPY.

## 5. Il team di routine (5 run al giorno)

Orari in ET, poi UTC e Roma validi **fino al 25 ottobre 2026**. Fino al 1 novembre la differenza con Roma scende a 5 ore; dal 2 novembre l'apertura sarà alle 14:30 UTC.

| # | Ruolo | Quando | Modello | Cosa fa |
|---|---|---|---|---|
| 1 | Analista pre-market | 8:45 ET (12:45 UTC, 14:45 Roma) | Opus | Controlla calendario e orologio di Alpaca (se il mercato è chiuso esce subito). Legge `lessons.md`. Scansiona i movers, le notizie Alpaca e poche ricerche web, poi classifica i catalizzatori. Scrive `plan/<data>.json` con candidati, direzione ammessa, livelli di invalidazione e regime di mercato (SPY/QQQ, VIX, eventi macro della giornata). Commit. |
| 2 | Trader di apertura + risk manager | Avvio 9:25 ET (13:25 UTC), attesa fino alle 9:35 o 9:45 | Sonnet | Legge il piano, aspetta con `sleep` usando l'orologio di Alpaca, calcola il range dalle barre, valida la dimensione con una checklist di rischio e invia i bracket con `client_order_id` etichettati. Controlla alle 9:50 e alle 10:05 (pochi turni), cancella gli ingressi non partiti e scrive `log/<data>.md`. |
| 3 | Chiusura | 11:00 ET (15:00 UTC), oppure 15:50 ET se si tiene fino a fine giornata | Sonnet | Cancella gli ordini aperti del giorno e chiude le posizioni rimaste. È poco più di una formalità. |
| 4 | Contabile e coach | 16:15 ET (20:15 UTC) | Opus | Scarica i fill, calcola P&L, R multipli e slippage, confronta con SPY, aggiorna `journal/` ed `equity.csv`. Riscrive `lessons.md` (massimo circa 30 regole). Il venerdì fa anche la revisione settimanale. |
| 5 | Riserva | una tantum o da usare in caso di problemi | - | Resta libera entro il limite Pro, per un eventuale "controllo di metà mattina" o per i test. |

Perché i ruoli sono separati per orario e non per sub-agenti dentro una stessa run: ogni sub-agente riparte da zero e ricostruisce il contesto, quindi costa token in più senza dati nuovi. Il "risk manager" funziona meglio come checklist obbligatoria dentro il prompt del trader, con regole rigide.

Alternativa più economica in run: fondere 2 e 3 in un'unica sessione se chiudi entro le 10:30.

### Stato condiviso (repo GitHub, per esempio `GabrieleSozio/AI-Trading`)

```
config/strategy.md      regole della strategia (l'unica cosa che cambi a mano)
config/risk.md          limiti di rischio non negoziabili
plan/YYYY-MM-DD.json    output dell'analista
log/YYYY-MM-DD.md       decisioni e ordini del trader
journal/YYYY-MM-DD.md   consuntivo e analisi
equity.csv              curva del conto
lessons.md              memoria di lungo periodo, curata dal coach
```

Alpaca resta la fonte di verità per posizioni e ordini. Il repo contiene il "perché" delle decisioni.

## 6. Varianti da decidere

- **A. Uscita 11:00 ET:** coerente con l'idea del "primo tratto di sessione". Tiene meno esposizione, ma taglia i trend che proseguono nel resto della giornata.
- **B. Uscita a fine giornata:** fedele allo studio accademico, dove il grosso del profitto viene dai trend che durano tutto il giorno. Costa la stessa run: cambia solo l'orario della chiusura.
- **C. Esperimento parallelo "overnight/swing AI":** ingresso vicino alla chiusura e uscita il mattino dopo, oppure dopo qualche giorno. È meno sensibile alla lentezza dell'LLM e sfrutta di più la lettura delle notizie. Richiede un secondo conto paper. Lo terrei come seconda fase.

## 7. Stima di consumo (indicativa)

- Analista: circa 60-150k token in input (le ricerche web pesano).
- Trader: circa 40-100k, perché ogni turno dopo un'attesa rilegge il contesto (in gran parte dalla cache).
- Chiusura: circa 10-20k.
- Coach: circa 30-60k.

Sonnet per i ruoli meccanici e Opus solo per analista e coach contengono la spesa. La misura vera la prendiamo dalle prime run su claude.ai/settings/usage.

## 8. Rischi operativi e contromisure

- **Giorni di chiusura o mezza giornata:** ogni run controlla prima `/v2/calendar` e `/v2/clock` ed esce subito se il mercato è chiuso.
- **Cambio dell'ora legale:** le cron sono in UTC. Le aggiorno il 1-2 novembre (fine dell'ora legale USA) con un promemoria una tantum. Tra il 25 ottobre e il 1 novembre Roma è a 5 ore da New York invece di 6.
- **Run che non parte o parte tardi:** i bracket proteggono le posizioni; la chiusura ripulisce.
- **Allucinazioni sui numeri:** il prompt obbliga a ricalcolare dimensione e rischio con l'aritmetica nella shell e a rileggere l'ordine con GET dopo l'invio.
- **Prompt injection dalle notizie:** i testi delle notizie sono dati, non istruzioni, e i limiti di rischio non si possono modificare durante la run.
- **Stato verde ma task fallito:** il coach segnala le anomalie nel diario (con notifica push).

## 9. Cosa serve da te prima di costruire

1. Il tuo piano (Pro o Max), che decide quante run al giorno.
2. Un nuovo repo GitHub per lo stato, oppure una tua alternativa.
3. Un nuovo conto paper Alpaca con saldo di 500 USD (o l'equivalente di 500 EUR) e le sue chiavi, da inserire tu come API credentials nell'ambiente cloud. Le chiavi non devono passare dalla chat.
4. La scelta tra le varianti A e B (ed eventualmente C).

## Fonti

- [Claude Code: Automate work with routines](https://code.claude.com/docs/en/routines)
- [Claude Code: Configure cloud environments](https://code.claude.com/docs/en/cloud-environments)
- [OpenHelm: limiti giornalieri delle routine](https://openhelm.ai/blog/claude-code-routines-daily-limit)
- [FINRA Regulatory Notice 26-10](https://www.finra.org/rules-guidance/notices/26-10)
- [Alpaca: Intraday Margin Framework](https://alpaca.markets/blog/finra-retires-the-pdt-rule-introducing-alpacas-new-intraday-margin-framework/)
- [Alpaca: Intraday Margin Rule for non-leverage accounts](https://docs.alpaca.markets/us/docs/intraday-margin-rule-for-non-leverage-margin-accounts)
- [Alpaca: Orders](https://docs.alpaca.markets/docs/orders-at-alpaca)
- [Alpaca: Market Data API](https://docs.alpaca.markets/docs/about-market-data-api)
- [Alpaca: Paper trading](https://docs.alpaca.markets/docs/paper-trading)
- [Alpaca MCP server (GitHub)](https://github.com/alpacahq/alpaca-mcp-server)
- [Zarattini, Barbon, Aziz (2024), SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4729284)
- [Concretum Group: sintesi dello studio](https://concretumgroup.com/a-profitable-day-trading-strategy-for-the-u-s-equity-market/)
- [QuantConnect: replica ORB Stocks in Play](https://www.quantconnect.com/research/18444/opening-range-breakout-for-stocks-in-play/)
- [Chague, De-Losso, Giovannetti: Day Trading for a Living?](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3423101)
