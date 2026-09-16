# Lezioni dalla ricerca sugli agenti LLM che fanno trading

Sintesi di studi ed esperimenti dal vivo (2024-2026). Sono i difetti tipici del "tipo di trader" che sei: tienili presenti.

## Cosa dicono i dati
- **Alpha Arena (nof1, stagione 1, crypto perpetui, 10-20x di leva):** 6 modelli di punta con lo stesso prompt. Risultati: Qwen3 Max +22,3% (circa 43 trade in tutto, meno di 3 al giorno, win rate 30,2%), DeepSeek +4,9%, Claude Sonnet 4.5 −30,8%, Grok 4 −45,3%, Gemini 2.5 Pro −56,7%, GPT-5 −62,7%. Ha vinto chi aveva stop e take profit più stretti; ha perso chi faceva molto trading (Gemini) o molti short (GPT-5, Grok). Il prompt obbligava ogni posizione ad avere target, stop e condizione di invalidazione. [iWeaver](https://www.iweaver.ai/blog/alpha-arena-ai-trading-season-1-results/), [Algogene](https://algogene.com/community/post/297)
- **StockBench (2025):** in 4 mesi, con decisioni giornaliere su titoli del Dow, la maggior parte degli agenti LLM **non ha battuto** il buy & hold. Hanno sottoperformato nelle fasi di calo e fatto meglio in quelle di rialzo. I modelli "reasoning" non erano migliori degli "instruct" e generavano più errori di formato. Con un portafoglio più ampio (da 5 a 30 titoli) le prestazioni peggioravano. Notizie e fondamentali aiutavano: senza notizie il rendimento del modello migliore passava da 1,9% a 1,4%. [arXiv 2510.02209](https://arxiv.org/html/2510.02209v2)
- **LiveTradeBench (2025, 50 giorni dal vivo):** i punteggi generali dei modelli **non predicono** i risultati nel trading. Le abilità non si trasferiscono da un mercato all'altro, e ogni modello mostra un proprio "stile" implicito. [arXiv 2511.03628](https://arxiv.org/html/2511.03628v1)
- **KTD-Fin (2026):** i rendimenti degli agenti erano spiegati soprattutto dall'esposizione passiva a mercato e fattori di stile, con **poca evidenza di alpha** nella scelta dei titoli. Con ticker e date nascosti, gli agenti smettevano di fare trading "a memoria". [arXiv 2605.28359](https://arxiv.org/html/2605.28359v1)
- **TradingAgents (2024):** l'architettura a ruoli (analisti, dibattito bull/bear, trader, risk team, fund manager) funziona meglio con **report strutturati** tra i ruoli, perché nelle chat libere l'informazione si degrada (effetto "telefono senza fili"). [arXiv 2412.20138](https://arxiv.org/abs/2412.20138)

## Regole che ne derivano
1. **Pochi trade, selettivi.** Ogni trade deve avere un catalizzatore o un vantaggio che sai spiegare in una frase.
2. **Piano d'uscita prima dell'ingresso:** target, stop e condizione di invalidazione, tutti scritti.
3. **Non razionalizzare le perdite.** Lo stop è sul server; non spostarlo più lontano, mai.
4. **Diffida dei ricordi di addestramento:** la "storia" che conosci di un ticker non è un dato di oggi. Decidi con i dati di oggi.
5. **Separa beta e alpha:** confronta sempre i risultati con SPY. Guadagnare in un mercato che sale non dimostra abilità.
6. **Attenzione allo short:** è stato la causa di molte perdite negli esperimenti. Va fatto solo con un catalizzatore negativo chiaro e con forza relativa negativa.
7. **Output strutturati:** piani, decisioni e passaggi tra ruoli si scrivono nei formati di `processo/decisione-e-registrazione.md`, niente prosa libera.
8. **Calibrazione:** registra le probabilità stimate. Se i trade dati al 60% vincono il 35% delle volte, sei troppo ottimista: riduci la dimensione finché la calibrazione non migliora.
9. **Umiltà statistica:** 20 trade non dimostrano niente (vedi `performance/metriche-e-valutazione.md`).
