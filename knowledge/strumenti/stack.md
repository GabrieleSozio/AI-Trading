# Stack di strumenti (tutti gratuiti)

**Regola d'oro:** il codice fa da **calcolatrice e raccoglitore di dati**, non decide. Nessuno script sceglie trade o regole: le decisioni restano degli agenti.

## 1. Già disponibili nella sessione cloud
| Strumento | A cosa serve |
|---|---|
| `curl` + `jq` | chiamate REST ad Alpaca e alle altre fonti; filtrare il JSON prima di leggerlo |
| `python3` | calcoli: dimensione, indicatori, statistiche |
| `git` | memoria condivisa: legge e scrive lo stato del repo |
| WebSearch / WebFetch | notizie, calendari, contesto |
| Sotto-agente (Agent) | Risk Officer indipendente con contesto ridotto |

## 2. Librerie Python utili (da installare con lo script di setup dell'ambiente, così restano in cache)
| Libreria | Uso |
|---|---|
| `pandas`, `numpy` | serie di prezzi, ledger CSV |
| `pandas_market_calendars` o `exchange_calendars` | calendari di borsa (in alternativa a `/v2/calendar`) |
| `scipy` | Black-Scholes, statistiche, test |
| `py_vollib` (facoltativa) | prezzi e greche delle opzioni, IV implicita |
| `quantstats` | metriche di performance e report (Sharpe, Sortino, drawdown, confronto con SPY) |
| `feedparser` | feed RSS (comunicati, notizie) |

Setup script suggerito per l'ambiente:
```bash
pip install --quiet pandas numpy scipy quantstats pandas_market_calendars feedparser
```
(serve la allowlist di default per i package manager, cioè PyPI).

## 3. Calcoli standard (da incollare ed eseguire nella shell)
```python
# ATR a 14 giorni da barre giornaliere [{h,l,c}, ...]
def atr(b, n=14):
    tr=[max(x['h']-x['l'], abs(x['h']-p['c']), abs(x['l']-p['c'])) for p,x in zip(b,b[1:])]
    return sum(tr[-n:])/n

# VWAP intraday da barre [{h,l,c,v}]
def vwap(b):
    pv=sum((x['h']+x['l']+x['c'])/3*x['v'] for x in b); v=sum(x['v'] for x in b); return pv/v if v else None

# Volume relativo del range di apertura (stesso feed per oggi e per lo storico!)
def rvol(v_oggi, v_storici): return v_oggi / (sum(v_storici)/len(v_storici))

# Black-Scholes (call) per stimare il prezzo equo con feed indicativo
from math import log, sqrt, exp
from scipy.stats import norm
def bs_call(S,K,T,r,iv):
    d1=(log(S/K)+(r+iv*iv/2)*T)/(iv*sqrt(T)); d2=d1-iv*sqrt(T)
    return S*norm.cdf(d1)-K*exp(-r*T)*norm.cdf(d2), norm.cdf(d1)   # prezzo, delta
# T in anni: per le 0DTE usa i minuti residui / (390*252)
```

## 4. Strumenti valutati e scartati (per ora)
- **Server MCP di Alpaca:** ufficiale e completo, ma gira solo in locale (stdio) e vuole le chiavi nelle variabili d'ambiente. Nelle routine cloud usiamo REST con curl e la funzione `j` (credenziali dalle variabili d'ambiente, mai stampate). [GitHub](https://github.com/alpacahq/alpaca-mcp-server)
- **TradingAgents** (framework multi-agente open source): utile come riferimento architetturale, non come dipendenza. [GitHub](https://github.com/tauricresearch/tradingagents)
- **yfinance:** API non ufficiale e instabile.
- **Piano dati Alpaca Algo Trader Plus** (99 USD/mese: SIP e OPRA reali): da valutare dopo 3-4 settimane se il feed IEX o indicative si dimostra un limite concreto (documentarlo nella revisione mensile).

## 5. Possibili estensioni future
- Dashboard (Artifact) che legge `state/ledger/*.csv` dal repo: equity, drawdown, statistiche per setup e per agente.
- Notifiche push dalle routine a fine giornata con il riepilogo del diario.
