# Registro delle decisioni di progetto

| Data | Decisione | Motivo |
|---|---|---|
| 16/09/2026 | Routine cloud (non locali), piano Pro (5 run al giorno) | nessuna dipendenza dal PC; limite giornaliero di run |
| 16/09/2026 | Flusso completamente AI: il codice solo come calcolatrice e fonte dati | requisito del proprietario |
| 16/09/2026 | Ricerca e trading su Opus 5 (CIO, Trader, Position Manager, Risk Officer) | qualità del ragionamento |
| 16/09/2026 | Multi-asset: azioni, ETF, opzioni, crypto | l'AI sceglie lo strumento migliore |
| 16/09/2026 | Rischio per trade variabile, deciso dall'AI, con tetti tecnici larghi e circuit breaker a livelli | requisito del proprietario più protezione da errori gravi |
| 16/09/2026 | Nessuna posizione overnight o nel weekend, **tranne le crypto** | requisito del proprietario |
| 16/09/2026 | Desk crypto leggero sabato e domenica | gestire le crypto rimaste aperte |
| 16/09/2026 | Repo GitHub `AI-Trading` come memoria condivisa e storico | le routine cloud non vedono il PC |
| 16/09/2026 | Mezze giornate: il Position Manager chiude l'intraday | il Closer delle 15:45 arriverebbe dopo la chiusura delle 13:00 |
| 16/09/2026 | Blocco a −25% dal massimo con riduzioni progressive a −10% e −15% (vedi simulazioni) | distingue un sistema buono da uno cattivo senza fermare quello buono per puro rumore |
| 17/09/2026 | Niente short di azioni ed ETF: il ribasso si esprime con ETF inversi long o put/put spread | Alpaca richiede 2.000 USD di equity per margine e short (403 sul conto da 550) |
| 17/09/2026 | Restare a 550 USD invece di aprire un conto paper più grande | si vuole misurare il processo con il capitale reale del progetto; il passaggio a 2.500-3.000 USD resta un'opzione |
| 17/09/2026 | Gambe di protezione di azioni ed ETF con `time_in_force: gtc` | se una routine salta, target e stop restano attivi invece di scadere alla chiusura |
| 17/09/2026 | Gestione dell'uscita a scelta dell'agente fra `fixed`, `breakeven` e `trailing`, registrata in `exit_mgmt` | permette di confrontare i tre modi con i dati invece di deciderlo a priori |
| 17/09/2026 | Varianti ORB (`orb15-conferma`, `orb-retest`, `orb-fallito`, `orb-inverso`, `orb-indice-leva`) aggiunte come schede **facoltative** | ampliano le scelte dell'apertura senza imporre una strategia fissa |
| 17/09/2026 | Tetto del premio opzioni confermato all'8% dell'equity | con 550 USD alzarlo aumenterebbe la perdita singola senza aprire strutture molto migliori |
| 17/09/2026 | Correzione: il conto non ha vincolo T+1 (limited margin, PDT abolita il 04/06/2026) | il capitale si riusa più volte al giorno; il limite vero è il capitale nominale |
| 17/09/2026 | SEC EDGAR come seconda fonte di catalizzatori (8-K 2.02/5.02, 424B5 e ATM, 13D) | gratuita, senza chiave, appare entro secondi dal deposito; il 424B5 spiega i crolli mattutini meglio di qualunque notizia |
| 17/09/2026 | Form 4 (insider) solo come conferma e veto, con peso basso | l'evidenza è su orizzonti mensili; nel giorno del deposito il movimento è ~0,2-0,3% e i depositi arrivano dopo la chiusura |
| 17/09/2026 | Aggiunti tre modificatori di contesto: notturno-vs-diurno, prima mezz'ora di SPY, giorni a cavallo del cambio mese | hanno evidenza pubblicata solida e si calcolano con i dati Alpaca già disponibili |
| 17/09/2026 | Aggiunti halt Nasdaq (come protezione), calendario utili Nasdaq e calendario FDA | evitano ingressi su titoli bloccati o con eventi in arrivo |
| 17/09/2026 | Nessun cambio del fornitore dati: Alpaca resta la fonte primaria | verificate 10 alternative gratuite nel 2026: nessuna offre SIP in tempo reale o dati opzioni completi; Polygon/Massive ora dà solo fine giornata |
| 17/09/2026 | Lista esplicita di segnali scartati (put/call pubblico, gamma 0DTE, momentum post-halt, SSR, upgrade analisti, short volume FINRA, OFI/VPIN su IEX, 13F) | evidenza contraria o dati gratuiti troppo in ritardo: evita di sprecare token |

## Da fare prima del primo avvio
- [ ] Nuovo conto paper Alpaca da 500 USD e chiavi API
- [ ] Ambiente cloud dedicato: API credentials (header Alpaca) + rete Custom (domini in `knowledge/dati/fonti-dati.md`) + setup script
- [x] Prompt delle routine (`routines/`, 16/09/2026)
- [x] Guida di setup (`docs/04-setup-ambiente-e-routine.md`)
- [ ] Creazione delle routine con il repo `AI-Trading` come fonte, modello Opus 5 dove previsto
- [ ] Prima run manuale di test ("Run now") a mercato chiuso, poi una a mercato aperto
