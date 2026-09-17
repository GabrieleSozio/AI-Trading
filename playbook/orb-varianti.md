# orb-varianti — Varianti dell'Opening Range Breakout (facoltative)

**Non sono obbligatorie.** Sono alternative che il Trader può scegliere *al posto* di `orb-sip`, quando le condizioni del giorno le rendono preferibili. Se le usi, scrivi nel log **quale variante e perché**, e nel campo `setup` metti l'id esatto della variante.

**Contesto comune:** stessi filtri di selezione di `orb-sip` (prezzo > 5 USD, ATR14 > 0,50, volume medio > 1M, catalizzatore verificato, RVOL alto, spread < 0,2%), stessa uscita entro le 15:50 ET, stessa protezione all'ingresso.

**Dati sulle finestre del range** (percentuale di giornate in cui la rottura del range ha raggiunto il target prima dello stop, fonte: studi citati in `knowledge/strategie/azioni-intraday.md` §1 e materiale divulgativo): range di 5 minuti ~53,8%, 15 minuti ~51,0%, 30 minuti ~49,4%. Più lungo è il range, meno falsi segnali ma ingresso più tardi e stop più largo: è un compromesso, non un miglioramento.

---

## `orb15-conferma` — range di 15 minuti con conferma
- **stato:** sperimentale | **asset:** azioni, ETF | **finestra:** 09:45-10:30 ET
- **quando preferirla:** apertura confusa, molte inversioni nei primi 5 minuti, feed IEX poco affidabile sul volume dei primi minuti.
- **ingresso:** si aspetta la chiusura della candela a 15 minuti; si entra alla rottura dell'estremo del range **solo se** la candela di rottura chiude oltre il livello e il prezzo è dalla parte giusta del VWAP.
- **stop:** estremo opposto del range, oppure 10-25% dell'ATR14 se più vicino.
- **costo:** ingresso più tardi e stop più largo, quindi posizione più piccola.
- **da registrare:** ampiezza del range in % e in ATR, volume della candela di rottura.

## `orb-retest` — rottura con ritorno sul livello
- **stato:** sperimentale | **asset:** azioni, ETF | **finestra:** 09:40-11:00 ET
- **quando preferirla:** il prezzo è già scappato oltre il range (ingresso diretto troppo lontano dallo stop) oppure il titolo è molto volatile.
- **ingresso:** dopo la rottura si aspetta che il prezzo torni sul livello rotto e lo **tenga** (candela di reazione a favore, volume in calo durante il ritorno). Si entra sulla ripartenza.
- **stop:** sotto il minimo della candela di reazione (per i long), comunque dentro il limite di rischio.
- **vantaggio:** stop molto più stretto, quindi più R per lo stesso rischio in dollari.
- **rischio:** molti retest non arrivano mai e il trade non parte. Va registrato come `no_trade` con motivo `retest_mai_arrivato`, per misurare quante occasioni fa perdere.

## `orb-fallito` — rottura fallita, ingresso opposto
- **stato:** sperimentale | **asset:** azioni, ETF | **finestra:** 09:40-11:00 ET
- **logica:** una rottura che rientra subito nel range intrappola chi è entrato; il movimento opposto è spesso rapido.
- **ingresso:** il prezzo rompe un estremo del range, **rientra** dentro il range entro poche candele e poi rompe **l'estremo opposto**. Si entra lì.
- **stop:** oltre l'estremo del falso breakout.
- **vincolo importante:** se la direzione risultante è ribassista su un singolo titolo, l'unico strumento disponibile è una put (lo short non è possibile con questo conto). Spesso il premio non ci sta nel tetto: in quel caso si rinuncia e si registra `no_trade`.
- **da registrare:** quante candele è durata la falsa rottura, il volume del rientro.

## `orb-inverso` — tesi ribassista senza short
- **stato:** sperimentale | **asset:** ETF inversi (SH, PSQ, RWM, DOG) o put | **finestra:** 09:35-10:30 ET
- **quando:** rottura ribassista del range su un indice (SPY, QQQ, IWM) con SPY sotto VWAP e contesto macro coerente.
- **ingresso:** stop buy sull'**ETF inverso** quando rompe il massimo del proprio range di apertura (cioè quando l'indice rompe al ribasso il proprio minimo). Livelli sempre letti sul grafico dell'ETF inverso.
- **stop e target:** calcolati sull'ATR dell'ETF inverso.
- **attenzione:** volumi e spread degli inversi sono peggiori dell'ETF originale: verifica lo spread prima dell'ingresso e usa ordini limit o stop-limit se supera lo 0,2%.

## `orb-indice-leva` — ORB su Nasdaq-100 con ETF a leva
- **stato:** sperimentale | **asset:** TQQQ (rialzo) o SQQQ (ribasso) | **finestra:** 09:35-10:30 ET
- **logica:** l'ORB sugli indici, da solo, ha evidenza debole (la replica su QQQ dà Sharpe vicino a zero, vedi `knowledge/strategie/azioni-intraday.md`). Ha senso solo con un contesto forte: dato macro delle 08:30 ET, uscita netta dalla "noise area" di `etf-noise`, forte partecipazione settoriale.
- **perché gli ETF a leva:** con 550 USD, QQQ costa troppo per una posizione sensata; TQQQ e SQQQ hanno prezzo per quota basso e si comprano **long** in entrambe le direzioni.
- **dimensione:** il mandato limita il rischio all'**1% dell'equity** quando si usano ETF 3x. Lo stop va calcolato sull'ATR dell'ETF a leva (circa 3 volte quello dell'indice).
- **da evitare:** tenerli oltre la giornata, e usarli nei giorni di mercato laterale.

---

**Come si valutano.** Restano `sperimentale` finché il Coach non ha almeno ~20 trade per variante nelle statistiche di `state/memory/playbook-stats.md`. Prima di allora la dimensione segue la fascia "setup sperimentale" di `knowledge/rischio/sizing.md`.
