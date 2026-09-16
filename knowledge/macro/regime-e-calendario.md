# Regime di mercato e calendario macro

Il CIO classifica ogni mattina il **regime** e lo scrive in testa al piano. Il regime influenza quali setup preferire e quanto rischiare.

## 1. Scheda del regime (compilarla ogni giorno)
| Dimensione | Come si misura | Valori |
|---|---|---|
| Trend | SPY e QQQ rispetto alle medie a 20 e 50 giorni; futures pre-market | up / down / laterale |
| Volatilità | livello del VIX e variazione dal giorno prima; ATR di SPY | bassa (<15) / normale (15-20) / alta (20-30) / stress (>30) |
| Ampiezza | quanti settori sono positivi; IWM rispetto a SPY | ampia / stretta |
| Tassi e dollaro | rendimento del Treasury a 10 anni, DXY | in salita / stabili / in discesa |
| Rischio evento | dati macro di oggi, FOMC, utili delle mega cap, scadenze opex | nessuno / medio / alto |
| Crypto | trend di BTC, funding, Fear & Greed | risk-on / neutro / risk-off |

Soglie del VIX indicative e condivise nella pratica, **non leggi**: contano soprattutto le **variazioni** (un VIX che passa da 14 a 19 in un giorno pesa più di un VIX stabile a 22).

## 2. Cosa cambia con il regime
| Regime | Tende a funzionare | Attenzione |
|---|---|---|
| Trend up, volatilità bassa o normale | ORB long, gap and go, pullback su VWAP | short solo con un catalizzatore forte |
| Trend down, volatilità alta | short o put selettivi, gap fade dei rimbalzi | movimenti violenti in entrambe le direzioni: dimezza la dimensione, stop più larghi con meno azioni |
| Laterale, volatilità bassa | pochi trade; mean reversion verso il VWAP | gli ORB falliscono spesso |
| Stress (VIX > 30) | solo trade A+, oppure stare fermi | spread larghi, halt, correlazioni tutte a 1 |
| Giorno con evento macro alle 8:30 | reazione dopo il dato: conferma o rifiuto del gap | primi minuti caotici |
| Giorno FOMC (14:00 ET) | mattina compressa: dimensione ridotta | essere flat o molto ridotti prima delle 14:00 |

Queste associazioni sono conoscenza pratica comune, non leggi. Il Coach le verifica con le statistiche per regime in `state/memory/playbook-stats.md`.

## 3. Calendario da controllare ogni mattina
- **Dati USA (08:30 ET):** CPI, PPI, occupazione (NFP, primo venerdì del mese), richieste di disoccupazione (ogni giovedì), vendite al dettaglio, PCE.
- **Alle 10:00 ET:** ISM, fiducia dei consumatori, JOLTS: attenzione per i trade aperti in quel momento.
- **FOMC:** date ufficiali su federalreserve.gov. Comunicato alle 14:00 ET, conferenza stampa alle 14:30.
- **Utili:** chi riporta prima dell'apertura (i titoli in gioco oggi) e dopo la chiusura (evitare di aprire posizioni su quei titoli oggi).
- **Opex:** terzo venerdì del mese (scadenza mensile delle opzioni): flussi e "pinning" vicino agli strike importanti.
- **Festività e mezze giornate:** `GET /v2/calendar`.
- **Evidenza FOMC:** il "pre-FOMC drift" documentato da Lucca e Moench (rialzo nelle 24 ore prima del comunicato) risulta attenuato negli studi successivi. [NY Fed](https://www.newyorkfed.org/research/staff_reports/sr512.html), [Studio 2024](https://www.tandfonline.com/doi/full/10.1080/00036846.2024.2322573)

## 4. Fonti per il calendario (vedi `dati/fonti-dati.md`)
federalreserve.gov (FOMC), bls.gov (CPI, occupazione), bea.gov (PIL, PCE), ricerca web "economic calendar today", calendario utili (Nasdaq, Finnhub), FRED (serie storiche: VIX, tassi, spread).
