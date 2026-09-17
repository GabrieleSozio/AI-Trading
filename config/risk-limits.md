# Mandato di rischio: limiti non negoziabili

Solo il proprietario del repo può modificare questo file. Dentro questi limiti gli agenti decidono liberamente dimensioni, strumenti e frequenza.
Il ragionamento e le simulazioni dietro ogni numero sono in `knowledge/rischio/limiti-e-circuit-breaker.md`.

## A. Per singolo trade
| Regola | Limite |
|---|---|
| Rischio massimo (perdita allo stop) su azioni, ETF e crypto | **3% dell'equity** di inizio giornata |
| Premio massimo per un trade in opzioni (rischio definito) | **8% dell'equity** |
| Dimensione di riferimento consigliata (non obbligatoria) | 0,5-2% di rischio |
| Protezione | obbligatoria all'ingresso: bracket o stop sul server, oppure rischio definito |
| Time in force delle gambe di protezione (azioni ed ETF) | **`gtc`**, così target e stop non scadono a fine giornata se una routine salta |
| Stop "mentali" | vietati |

**Gestione dell'uscita (facoltativa, a scelta dell'agente).** Dopo l'ingresso lo stop può essere spostato **solo in direzione favorevole** (mai allargato), in tre modi ammessi:
1. **Stop a pareggio**: quando il trade guadagna almeno 1R, la gamba di stop si sposta al prezzo d'ingresso (PATCH della gamba SL).
2. **Trailing stop di Alpaca**: si cancellano le gambe del bracket e si invia un `trailing_stop` con `trail_percent` o `trail_price`. Lo gestisce il server, non consuma run né token, ma rinuncia al target fisso. Non disponibile per crypto, opzioni e frazionari.
3. **Stop fisso fino alla chiusura**: nessuna modifica (comportamento di default, e quello con più evidenza a favore nello studio ORB).
La scelta e il motivo vanno scritti nel log e in `decisions.jsonl` (`exit_mgmt`: `fixed` / `breakeven` / `trailing`), così il Coach può confrontarne i risultati.

## B. Portafoglio
| Regola | Limite |
|---|---|
| Esposizione lorda | ≤ 100% dell'equity (niente leva, anche se il conto la consentisse) |
| Posizioni aperte contemporaneamente | ≤ 4 |
| Nuove posizioni al giorno | ≤ 6 (anti-overtrading) |
| Premio totale in opzioni aperte | ≤ 15% dell'equity |
| Esposizione crypto | ≤ 50% dell'equity |
| Rischio aperto totale (somma delle perdite agli stop + premi) | ≤ 8% dell'equity |

## C. Strumenti e orari
- **Azioni, ETF e opzioni**: solo intraday. Tutto flat entro le 15:50 ET. Niente overnight e niente weekend.
- **Opzioni**: solo acquisti (call o put) e spread a rischio definito. **Mai vendite scoperte.** Niente contratti con spread bid/ask > 10% del mid. Le 0DTE vanno chiuse entro le 15:30 ET.
- **Crypto**: solo long (Alpaca non consente short). Overnight e weekend ammessi solo con stop-limit GTC attivo sul server.
- **Short su azioni ed ETF**: **non disponibile** finché l'equity resta sotto i 2.000 USD (Alpaca risponde 403). Il lato ribassista si esprime **solo** con ETF inversi comprati long (SH, PSQ, RWM, e simili) o con put / put debit spread. Se un giorno l'equity superasse stabilmente i 2.000 USD, lo short torna ammesso solo con bracket e solo su titoli `shortable` ed `easy_to_borrow`. Dettagli: `knowledge/dati/alpaca-conto-e-limiti.md`.
- Niente titoli sotto 3 USD, niente ordini in extended hours, niente leva tramite ETF 3x oltre l'1% di rischio.

## D. Circuit breaker (calcolati dal Coach in `state/risk-state.json`)
| Condizione | Modalità | Effetto |
|---|---|---|
| Drawdown dal massimo < 10% | `normal` | limiti A-C |
| Drawdown dal massimo ≥ 10% | `reduced` | rischio max 1% per trade, premio opzioni max 4%, max 2 posizioni |
| Drawdown dal massimo ≥ 15% | `minimal` | rischio max 0,5%, niente opzioni. Il Coach scrive una revisione straordinaria |
| Drawdown dal massimo ≥ 25% | `shadow` | **nessun ordine reale.** Gli agenti continuano a lavorare con trade virtuali. Si esce SOLO con un reset manuale del proprietario |
| Perdita giornaliera ≥ 6% dell'equity di inizio giornata | stop giornaliero | niente nuovi ingressi, chiusura delle posizioni intraday |
| Perdita settimanale ≥ 10% | `reduced` fino a lunedì | come `reduced` |

Si risale di livello solo quando il drawdown torna sotto la soglia del livello **meno 5 punti** (isteresi): ad esempio da `reduced` a `normal` sotto il 5%.

## E. Operatività
- Solo `paper-api.alpaca.markets`.
- Se i dati sono incoerenti (prezzi anomali, API in errore, orologio non verificabile): **nessun nuovo ordine**.
