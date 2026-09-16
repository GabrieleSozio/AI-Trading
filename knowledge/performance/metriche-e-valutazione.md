# Metriche, storico e come capire se il sistema migliora

Letto soprattutto dal **Coach**. Obiettivo: sapere in ogni momento se il sistema **migliora, peggiora o è solo fortunato**.

## 1. Metriche di conto (giornaliere, `equity.csv`)
- Equity, P&L del giorno (USD e %), P&L cumulato, **drawdown dal massimo**.
- Confronto con **SPY buy & hold** e con SPY nella finestra 9:30-10:30 (il nostro momento operativo).
- Sharpe e Sortino annualizzati (radice di 252) su finestre mobili di 20 e 60 giorni. Calmar = rendimento annualizzato / drawdown massimo.
- Esposizione media e massima, e giorni senza trade.

## 2. Metriche per trade (`trades.csv`)
- **R multiplo** = P&L / rischio iniziale. È la metrica chiave, perché non dipende dalla dimensione.
- Win rate, R medio delle vincite e delle perdite, **expectancy (R medio per trade)**, profit factor (vincite lorde / perdite lorde).
- **MAE e MFE** (massima escursione contro e a favore, in R): dicono se gli stop sono troppo stretti o i target troppo vicini.
- Slippage: prezzo eseguito − prezzo previsto (in bps e in R).
- Durata del trade.
- Ogni metrica va divisa per **setup**, **asset class**, **ruolo** (CIO che l'ha proposto, Trader o Position Manager che l'ha eseguito), **regime**, **catalizzatore**, **fascia oraria** e **direzione**.

## 3. Qualità delle decisioni (feedback più veloce del P&L)
- **Calibrazione:** per ogni previsione (`forecasts.csv`) si calcola il **Brier score** = media di (p − esito)², dove l'esito vale 1 se il target viene raggiunto prima dello stop.
  - Si confronta con il Brier "ingenuo", ottenuto prevedendo sempre il win rate storico. Se non lo batte, le probabilità stimate non aggiungono informazione.
  - Tabella di affidabilità: previsioni raggruppate per fasce (0-30%, 30-45%, 45-60%, >60%), con il tasso di successo reale di ciascuna.
- **Voto al processo** (A-D): quota di A+B sul totale. Deve salire nel tempo.
- **No-trade:** i titoli scartati vengono seguiti "in ombra" (cosa avrebbe fatto il setup?) per capire se la selezione aggiunge valore.
- **Tesi del CIO:** quota di tesi che si sono realizzate (anche senza trade). Misura la qualità della ricerca.

## 4. Significatività: quanti trade servono?
Numero di trade necessari per dimostrare che l'expectancy è > 0 con il 95% di confidenza (test a una coda):
`n ≈ (1,645 · σ_R / μ_R)²`

Esempio: con win rate del 35% e vincite medie di 2,2R, μ = +0,12R e σ ≈ 1,53R, quindi **n ≈ 440 trade**. Con 2 trade al giorno sono circa 9 mesi.
Conseguenze:
- Nelle prime settimane **non si giudica il sistema dal P&L**, ma da processo, calibrazione, slippage e rispetto delle regole.
- Si riporta sempre l'intervallo di confidenza dell'expectancy: `μ ± 1,96·σ/√n`.
- **Probabilistic Sharpe Ratio (PSR):** probabilità che lo Sharpe vero superi un valore di riferimento, tenendo conto di asimmetria e code grasse della distribuzione. Da essa si ricava anche il **Minimum Track Record Length**, cioè quante osservazioni servono. [Portfolio Optimizer](https://portfoliooptimizer.io/blog/the-probabilistic-sharpe-ratio-bias-adjustment-confidence-intervals-hypothesis-testing-and-minimum-track-record-length/), [Bailey e López de Prado, Deflated Sharpe](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551)
  `PSR = Φ( (SR − SR*) · √(T−1) / √(1 − γ3·SR + (γ4−1)/4 · SR²) )`, dove γ3 è l'asimmetria e γ4 la curtosi dei rendimenti.
- **Test multipli:** più setup si provano, più è probabile trovarne uno "buono" per caso. Quando si confrontano molti setup, si chiede uno Sharpe più alto (spirito del Deflated Sharpe).

## 5. "Sta migliorando?": il cruscotto di trend (revisione settimanale)
| Indicatore | Finestra | Miglioramento se… |
|---|---|---|
| Expectancy R (con IC) | ultimi 30 trade rispetto ai 30 precedenti | sale e l'IC si restringe |
| Brier score | ultimi 30 rispetto ai 30 precedenti | scende |
| Quota A+B | 4 settimane | sale |
| Slippage medio | 4 settimane | scende |
| Drawdown massimo | mobile | resta sotto il 10% |
| Rendimento − SPY | cumulato | positivo e crescente |
| Costo per trade (run e token) | 4 settimane | stabile o in calo |

Confronto tra due finestre: test t di Welch sulla media degli R. Con meno di 30 trade per finestra si riporta solo la direzione, **senza conclusioni**.

## 6. Ciclo di vita dei setup (`state/memory/playbook-stats.md`)
| Stato | Criterio | Rischio consentito |
|---|---|---|
| `sperimentale` | nuovo, meno di 10 trade | 0,25-0,5% |
| `in_prova` | 10-29 trade | ≤ 1% |
| `attivo` | ≥ 30 trade ed expectancy > 0 | secondo le fasce di `rischio/sizing.md` |
| `sospeso` | ≥ 20 trade con expectancy < −0,2R, oppure ultimi 15 < −0,4R | 0 (si seguono solo in ombra) |
| `ritirato` | sospeso e ancora negativo dopo 20 trade in ombra | – |
Il Coach propone i cambi di stato nella revisione settimanale e li applica.

## 7. Report
- **Giornaliero** (`state/journal/`): vedi il template in `processo/decisione-e-registrazione.md`.
- **Settimanale** (`state/reviews/weekly/YYYY-Www.md`): cruscotto del §5, tabella per setup e per asset, 3 lezioni, modifiche al playbook, stato del rischio, consumo di run e token.
- **Mensile** (`state/reviews/monthly/YYYY-MM.md`): come il settimanale, più il confronto con SPY e con i bot Python del proprietario (se disponibili), PSR, proposte motivate su limiti o dati (ad es. il piano dati a pagamento).
