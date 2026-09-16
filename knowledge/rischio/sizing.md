# Dimensionamento delle posizioni

Il **rischio per trade** lo decidi tu, entro i limiti della modalità attiva. Qui trovi come calcolarlo e come sceglierlo.

## 1. Formule (da eseguire sempre nella shell)
```
equity0   = equity di inizio giornata (GET /v2/account → last_equity, o equity alla prima lettura)
risk_usd  = equity0 × risk_pct

Azioni/ETF:   qty = floor(risk_usd / |entry − stop|)
              poi qty = min(qty, floor(buying_power_libero / entry), floor(equity0 × 1.0 / entry) − esposizione_esistente)
              se qty < 1 → trade non fattibile con questo stop: cambia strumento o rinuncia
Opzioni long: contratti = floor(budget_premio / (prezzo_limit × 100))   [budget ≤ 8% equity0]
Debit spread: contratti = floor(budget_premio / (debito × 100))
Credit spread: rischio = (larghezza − credito) × 100 × contratti ≤ risk_usd
Crypto:       qty = risk_usd / (|entry − stop| × 1.5)       [1.5 = margine per salti di prezzo e commissioni]
              notional ≤ 50% equity0 (considerando anche la crypto già in portafoglio)
```
Poi controlla che il **rischio aperto totale** (somma di tutti i rischi allo stop più i premi) resti ≤ 8% dell'equity.

## 2. Scegliere la percentuale di rischio
| Situazione | Rischio suggerito |
|---|---|
| Setup del playbook con statistiche positive (≥ 30 trade), catalizzatore forte, regime favorevole | 1,5-2% (fino a 3% solo con motivazione scritta) |
| Setup valido ma con statistiche ancora scarse (< 30 trade) | 0,75-1% |
| Setup nuovo o sperimentale | 0,25-0,5% |
| Regime avverso (VIX in forte salita, evento macro imminente) | dimezzare |
| Dopo 3 perdite consecutive nella giornata | 0,5% o stop |
| Modalità `reduced` / `minimal` | ≤ 1% / ≤ 0,5% |

## 3. Criterio di Kelly (solo come tetto, mai come obiettivo)
- f* = (b·p − q) / b, dove p = probabilità di vincita, q = 1 − p, b = vincita media / perdita media.
- Il Kelly pieno massimizza la crescita ma ha drawdown enormi ed è molto sensibile a errori nella stima di p. **Mezzo Kelly** mantiene circa il 75% della crescita con metà della volatilità. [R. O'Connell](https://ryanoconnellfinance.com/kelly-criterion/)
- Regola del progetto: dopo **almeno 100 trade** di un setup, il rischio per quel setup non deve superare **¼ di Kelly** calcolato sulle statistiche reali. Prima dei 100 trade valgono solo le fasce del §2.

## 4. Volatilità
- Usa l'ATR (14 giorni, e intraday a 5 minuti) per decidere dove mettere lo stop. Uno stop più largo richiede **meno azioni**, non più rischio.
- Posizioni correlate (ad es. NVDA e SMH, oppure due titoli dello stesso settore) contano come un'unica esposizione: somma i rischi.

## 5. Cosa ci dicono le simulazioni (Monte Carlo, 500 trade ≈ 1 anno con 2 trade al giorno)
Scenario con un buon vantaggio (win rate 35%, vincita media 2,2R, cioè +0,12R per trade):

| Rischio per trade | Equity finale mediana | Drawdown max mediano | P(drawdown ≥ 30%) | P(drawdown ≥ 50%) |
|---|---|---|---|---|
| 1% | 1,72x | 21% | 12% | 0% |
| 2% | 2,64x | 38% | 81% | 16% |
| 3% | 3,62x | 52% | 99% | 58% |
| 5% | 4,92x | 74% | 100% | 98% |
| 10% | 1,74x | 97% | 100% | 100% |

Scenario senza vantaggio (+0R): con il 2% di rischio l'equity mediana arriva a 0,84x e il drawdown mediano è 54%. Con il 3% arriva a 0,66x.
Con un win rate del 35%, **una serie di 10 perdite di fila in 500 trade capita nel 91% dei casi**.

**Conclusioni:**
- Anche con un buon vantaggio, un rischio sopra il 2% costante porta a drawdown molto profondi.
- Oltre un certo livello (qui intorno al 5-10%) il rendimento **cala**, come previsto da Kelly.
- Usa il 3% solo in casi eccezionali, non come abitudine.
