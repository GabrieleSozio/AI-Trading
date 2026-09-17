# SEC EDGAR: i documenti che muovono i prezzi (gratis, senza chiave)

EDGAR è l'archivio pubblico dei documenti che le società USA devono depositare. È **gratuito, senza API key, già nella allowlist** (`www.sec.gov`, `data.sec.gov`, `efts.sec.gov`) e ha un vantaggio decisivo: il documento appare online **entro pochi secondi** dal deposito, prima che la notizia sia scritta da chiunque.

## 1. Regole d'accesso (obbligatorie)
- Serve sempre un header **User-Agent** con un contatto, altrimenti EDGAR risponde 403.
- Massimo **10 richieste al secondo**. Metti una pausa fra le chiamate.
```bash
UA="AI-Trading <email-di-contatto>"
s() { curl -sS --max-time 20 -H "User-Agent: $UA" -H "Accept-Encoding: gzip, deflate" --compressed "$@"; }
```

## 2. Quali documenti contano davvero (in ordine di utilità per noi)
| Modulo | Cosa segnala | Perché conta la mattina |
|---|---|---|
| **8-K voce 2.02** | risultati trimestrali | catalizzatore vero, spesso depositato prima dell'apertura |
| **8-K voce 5.02** | uscita o arrivo di CEO/CFO | movimento immediato, spesso violento |
| **8-K voci 1.01 / 7.01 / 8.01** | contratto importante, comunicato allegato | qualità del catalizzatore |
| **424B5, S-3 takedown, offerte ATM** | l'azienda emette **nuove azioni** = diluizione | è la spiegazione più pulita di un crollo mattutino: **mai comprare la forza di un titolo che ha appena depositato un 424B5**; è invece un ottimo motivo per una tesi ribassista (put) |
| **SC 13D** | un investitore attivista sale sopra il 5% con intenti | può muovere il titolo; il 13G (passivo) quasi mai |
| **SC TO-T** | offerta pubblica d'acquisto | il prezzo si ancora all'offerta: **niente momentum, da evitare** |
| **Form 4** | acquisti e vendite di dirigenti e consiglieri | vedi §4: contesto, non catalizzatore |
| **13F** | portafogli dei fondi | trimestrale e con 45 giorni di ritardo: **inutile** |

Liste utili come **blacklist**: titoli sospesi (`https://www.sec.gov/litigation/suspensions`) e "threshold securities list".

## 3. Come si guarda (ricette pronte)
```bash
# a) Tutti i depositi di oggi, per tipo di modulo (indice giornaliero)
s "https://www.sec.gov/Archives/edgar/daily-index/2026/QTR3/form.20260917.idx" | awk '$1=="8-K"||$1=="424B5"||$1=="SC 13D"'

# b) Ultimi depositi di una società (Atom), es. CIK di Apple
s "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000320193&type=8-K&count=10&output=atom" | grep -E "<title>|<updated>"

# c) Elenco completo dei depositi di una società in JSON (comprende data e ora)
s "https://data.sec.gov/submissions/CIK0000320193.json" | jq '.filings.recent | [.form, .filingDate, .accessionNumber] | transpose | .[0:10]'

# d) Ricerca full-text (endpoint non ufficiale, può cambiare)
s "https://efts.sec.gov/LATEST/search-index?q=%22at-the-market%22&forms=424B5&dateRange=custom&startdt=2026-09-16&enddt=2026-09-17" | jq '.hits.hits[]._source | {ciks,display_names,file_date}'
```
Il CIK di un ticker si trova una volta sola in `https://www.sec.gov/files/company_tickers.json`.

## 4. Form 4 (insider): come si usa davvero
**Evidenza.** Gli acquisti degli insider hanno potere predittivo, ma su **mesi**, non ore: Cohen-Malloy-Pomorski 2012 misurano ~1,8%/mese per i soli acquisti "opportunistici" (il 64% è routine e non predice nulla); Lakonishok-Lee 2001 trovano che le **vendite non predicono niente** e che la reazione nel giorno del deposito è ~0,1-0,2%. Uno studio 2024 sui depositi 2018-2023 misura +0,21% il giorno del deposito e +0,33% il giorno dopo, con guadagni in dollari **non statisticamente significativi** e concentrati nei titoli meno liquidi.
**Timing.** L'obbligo è entro 2 giorni lavorativi e i depositi si concentrano **dopo la chiusura**: alle 9:30 la notizia è vecchia di ore e già nel prezzo.

**Regola operativa (peso basso, mai un trade da solo):**
1. Contano solo: codice transazione **P** (acquisto sul mercato), casella **10b5-1 non spuntata** (cioè non pre-programmato), ruolo **CEO/CFO/direttore**, e meglio se **cluster**: almeno 2 insider diversi entro 5 giorni.
2. Da questo nasce un flag per simbolo: `insider_cluster_buy_30d = sì/no`.
3. Il flag serve **solo a confermare** un catalizzatore già presente (può giustificare la dimensione piena o un target un po' più ambizioso) e come **veto**: non si costruisce una tesi ribassista su un titolo che i dirigenti stanno comprando.
4. Non genera mai un ingresso da solo. Se è l'unico motivo, si registra `no_trade`.

Gli aggregatori gratuiti (openinsider, secform4) non hanno API ufficiale e si rompono spesso; Quiver e Finnhub hanno limiti di licenza. Meglio EDGAR diretto.

## 5. Quando guardarlo, senza sprecare token
- **CIO (pre-apertura):** per i 5-10 candidati del giorno, controlla se esiste un deposito nelle ultime 24 ore. Un 424B5 su un candidato long lo **elimina**; un 8-K 2.02 o 5.02 ne rafforza il catalizzatore.
- **Trader / Position Manager:** solo su richiesta, quando un movimento non ha spiegazione nelle notizie.
- **Coach:** nessun uso.
- Una chiamata all'indice giornaliero più una o due verifiche mirate bastano: niente scansioni dell'intero archivio.
