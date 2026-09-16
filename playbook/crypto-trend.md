# crypto-trend — Trend e pullback su crypto liquide
- **stato:** sperimentale | **asset:** BTC/USD, ETH/USD, SOL/USD | **finestra:** qualsiasi (run del CIO, del Closer o del desk weekend)
- **condizioni:** trend rialzista su 4h (massimi e minimi crescenti, prezzo sopra la media a 20 periodi su 4h); pullback verso un supporto o la media; funding non estremo; Fear & Greed non in euforia estrema.
- **ingresso:** limit sul pullback (maker) o rottura del massimo della barra a 1h di rimbalzo.
- **stop:** sotto lo swing low (stop_limit GTC sul server, subito dopo il fill).
- **uscita:** target ≥ 2R e ≥ 2% (per coprire le commissioni); il desk può alzare lo stop sotto il nuovo swing low.
- **dimensione:** qty calcolata con il fattore 1,5 (salti di prezzo); esposizione ≤ 50% dell'equity.
- **da registrare:** timeframe, funding, F&G, commissioni pagate, R netto.
