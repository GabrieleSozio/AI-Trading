# Setup: conto paper, ambiente cloud e routine

Da fare una volta sola, nell'ordine. I passaggi segnati con 👤 li fai tu; quelli con 🤖 li fa Claude.

## 1. 👤 Conto paper Alpaca da 500 USD
1. Su app.alpaca.markets passa alla modalità **Paper**.
2. Clicca sul numero del conto paper in alto a sinistra, scegli **Open New Paper Account** e imposta il saldo iniziale a **500**.
3. Nel nuovo conto paper genera le **API Keys** (Key ID e Secret). Tienile a portata di mano e **non incollarle in chat**.
4. Verifica che le opzioni siano abilitate (i conti paper hanno il livello 3 di default) e che le crypto siano disponibili.

## 2. 👤 Ambiente cloud "ai-trading"
Su claude.ai/code apri il selettore dell'ambiente (icona a nuvola), poi crea un nuovo ambiente.
1. **Nome:** `ai-trading`
2. **Network access:** `Custom`. In **Allowed domains** inserisci:
   ```
   paper-api.alpaca.markets
   data.alpaca.markets
   api.alternative.me
   api.coingecko.com
   www.deribit.com
   api.hyperliquid.xyz
   api.kraken.com
   api.exchange.coinbase.com
   www.federalreserve.gov
   www.bls.gov
   www.bea.gov
   cdn.cboe.com
   data.sec.gov
   efts.sec.gov
   www.sec.gov
   ```
   Spunta **"Also include default list of common package managers"** (serve per pip e GitHub).
3. **Environment variables:** nessuna. Le chiavi non vanno messe qui.
4. **Setup script:**
   ```bash
   command -v jq >/dev/null || (apt-get update -qq && apt-get install -y -qq jq)
   pip install --quiet pandas numpy scipy quantstats pandas_market_calendars feedparser || true
   ```
5. Salva. Poi **riapri l'ambiente in modifica**: la sezione API credentials compare solo sugli ambienti già creati.
6. In **API credentials** clicca **Add credential**:
   - **Name:** `Alpaca paper`
   - **Allowed websites:** `paper-api.alpaca.markets` e `data.alpaca.markets`
   - **Custom headers:**
     - riga 1: Name `APCA-API-KEY-ID`, Prefix **vuoto**, Value = Key ID
     - riga 2: Name `APCA-API-SECRET-KEY`, Prefix **vuoto**, Value = Secret
   - Clicca **Connect**.
   - Se il modulo accetta un solo header, crea due credenziali con gli stessi siti, una per ciascun header. Il test del passo 4 dirà se funziona.
7. ⚠ Usa **solo le chiavi del conto paper**, mai quelle di un conto reale.

## 3. Creazione delle routine
**Opzione consigliata (🤖 + 👤):**
1. 🤖 Claude crea le 6 routine da questa chat, con prompt, orari UTC e modello già impostati, e le lascia **in pausa**.
2. 👤 Su claude.ai/code/routines apri ciascuna routine, clicca la matita e:
   - in **Repositories** aggiungi `GabrieleSozio/AI-Trading`;
   - come **ambiente** scegli `ai-trading`;
   - in **Connectors** rimuovi tutto (non servono);
   - verifica che il modello sia Opus 5;
   - salva.

**Alternativa (tutto 👤):** crei tu ogni routine con **New routine**, incollando il testo che nei file di `routines/` segue la riga `---PROMPT---`. Poi Claude imposta gli orari UTC esatti.

## 4. Test
1. 👤 Sulla routine "AI-Trading · 00 Test connessione" clicca **Run now**.
2. 🤖 Claude legge il risultato (`state/logs/test-<data>.md`) e corregge ciò che serve (allowlist, credenziali, pacchetti).
3. Ripetere finché è tutto OK.

## 5. Avvio
1. 🤖 Prima settimana consigliata: una giornata di prova, con avvio manuale di CIO e Trader a mercato aperto oppure con le routine attive per un giorno solo, poi revisione insieme.
2. 👤 / 🤖 Attivazione delle routine (toggle "Repeats").
3. 🤖 Promemoria automatico per il **2/11/2026**: le cron dei giorni di borsa vanno spostate di +1h UTC per la fine dell'ora legale USA.

## Note
- Una run con stato verde non significa che il compito sia riuscito: il Coach segnala le anomalie in cima al diario.
- Le routine usano lo stesso limite di utilizzo delle chat: negli orari delle run conviene non fare sessioni pesanti.
- Consumo e run rimanenti: claude.ai/settings/usage e claude.ai/code/routines.
