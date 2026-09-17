# Processo decisionale e formati di registrazione

## 1. Checklist del trader (prima di ogni ordine)
1. **Tesi**: perché questo strumento si muoverà, e in che direzione? (1 frase)
2. **Catalizzatore / vantaggio**: notizia, utili, flusso, regime, livello tecnico. Senza un vantaggio non si entra.
3. **Conferma dai dati live**: volume relativo, prezzo rispetto a VWAP e al range di apertura, forza relativa rispetto a SPY o QQQ (o BTC per le crypto).
4. **Invalidazione**: il prezzo o la condizione che dimostra la tesi sbagliata → lì va lo stop.
5. **Target**: livello realistico (range precedente, massimo o minimo pre-market, multiplo di ATR). R:R ≥ 1,5 salvo motivi scritti.
6. **Strumento**: azione, ETF, call/put, spread o crypto? (vedi il §3)
7. **Dimensione**: calcolata nella shell (vedi `rischio/sizing.md`), entro i limiti della modalità attuale.
8. **Probabilità stimata** che il target venga raggiunto prima dello stop.
9. **Risk Officer**: approvazione (vedi il §4).
10. **Invio → verifica GET → registrazione.**

## 2. Scheda tesi (formato del piano del CIO)
```
### T1 — NVDA long (catalizzatore: guidance alzata)
- regime: risk-on | tesi: gap +4% su guidance, settore forte
- condizioni d'ingresso: tiene VWAP e rompe il massimo dei primi 5 min con RVOL>2
- invalidazione: sotto il minimo del range di apertura o sotto VWAP per più di 5 min
- strumenti candidati: azione (preferito) / call debit spread 0-7 DTE
- priorità: alta | rischio suggerito: 1,5%
- da evitare se: SPY < VWAP e VIX in salita
```

## 3. Scelta dello strumento
| Situazione | Strumento preferito | Perché |
|---|---|---|
| Titolo liquido, movimento atteso 1-3%, stop tecnico chiaro | azione con bracket | costi minimi, protezione sul server |
| Tesi sul mercato o su un settore, non su un singolo titolo | ETF (SPY, QQQ, IWM, XL*) | niente rischio idiosincratico |
| Movimento atteso ampio e rapido, stop tecnico lontano | call/put o debit spread | rischio definito anche con uno stop largo |
| Prezzo per azione troppo alto per il capitale (niente frazioni nei bracket) | debit spread o ETF alternativo | dimensione compatibile con il conto |
| Opzioni con IV molto alta (dopo gli utili) | evitare gli acquisti secchi; al massimo debit spread | IV crush |
| Tesi su BTC/ETH, o fuori dall'orario di borsa | crypto spot con stop-limit | 24/7, ma commissioni ~0,25% per lato |

## 4. Protocollo del Risk Officer
Riceve SOLO: la proposta d'ordine (JSON), `config/risk-limits.md`, `state/risk-state.json`, account e posizioni.
Controlla: limiti A-D, calcolo di quantità e rischio (lo rifà da capo), coerenza tra stop e tesi, liquidità (spread), correlazione con le posizioni aperte, eventi macro nei prossimi 30 minuti.
Risponde con una tra: `APPROVE`, `RESIZE <qty>` oppure `REJECT <motivo>`. Il Trader non può ignorare un REJECT.

## 5. Formato della decisione (`state/ledger/decisions.jsonl`)
Una riga JSON per ogni decisione:
```json
{"ts":"2026-09-17T13:41:05Z","run_id":"20260917-trd","role":"trader","mode":"normal",
 "action":"open","symbol":"NVDA","asset":"stock","setup":"orb-sip","side":"long",
 "qty":2,"entry":181.2,"stop":179.6,"target":184.4,"risk_usd":3.2,"risk_pct":0.64,
 "prob_target":0.42,"thesis_id":"T1","rationale":"rottura OR5 con RVOL 3.1, sopra VWAP, SPY forte",
 "risk_officer":"APPROVE","exit_mgmt":"fixed","client_order_id":"20260917-trd-orb-1","order_ids":["..."]}
```
Valori di `action`: `open`, `no_trade`, `modify`, `close`, `cancel`, `skip_thesis`.
- `setup`: **esattamente** l'id di una scheda di `playbook/`. Le varianti vanno in `rationale` o in `notes`, mai nel nome.
- `exit_mgmt`: `fixed` (bracket con target e stop fermi, default) · `breakeven` (a +1R lo stop va al prezzo d'ingresso) · `trailing` (trailing stop di Alpaca, senza target). Va indicato per ogni `open`; se cambia durante il trade, si scrive una riga `modify` con il nuovo valore e il motivo.
- Campi di contesto facoltativi ma consigliati (servono al Coach per capire se questi segnali aiutano): `notte_vs_giorno` (`favorevole`/`contrario`/`neutro`), `spy_prima_mezzora` (rendimento di SPY 9:30-10:00 in %), `cambio_mese` (true/false), `insider_cluster_buy_30d` (true/false), `sec_filing` (es. `8-K 2.02`, `424B5`, `nessuno`).
- Per una tesi ribassista, `side` resta `long` quando lo strumento è un ETF inverso o una put: nel campo `rationale` spiega la direzione della tesi (es. "tesi short su Nasdaq espressa long su PSQ").

## 6. Diario (Coach, `state/journal/YYYY-MM-DD.md`)
```
# Diario YYYY-MM-DD
Equity: apertura X → chiusura Y (±Z%) | SPY ±W% | modalità: normal
## Trade (tabella: simbolo, setup, R, esito, voto al processo A-D)
## Cosa ha funzionato / cosa no (max 5 righe)
## Decisioni di non-trade corrette o sbagliate
## Calibrazione del giorno (previsioni vs esiti)
## Lezioni candidate (vanno in lessons.md solo se confermate ≥ 2 volte)
```

## 7. Voto al processo (indipendente dall'esito)
- **A**: piano rispettato, ingresso e uscita corretti. Il risultato è irrilevante.
- **B**: piccoli errori di esecuzione.
- **C**: trade fuori piano ma nei limiti.
- **D**: violazione del processo (niente tesi, stop spostato, dimensione sbagliata).
Un buon sistema accumula A e B anche nei giorni in perdita.
