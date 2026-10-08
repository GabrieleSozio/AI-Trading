# Lezioni (brevi, dense)

## Fatti dalla ricerca della società (letti 01/10/2026)
- Prima ora 9:30-10:30: nessuna strategia testata ha vantaggio (ORB, box, rumore solo prima ora, VWAP, figure, S&D, agenti LLM). Zona di rumore rende solo DOPO le 10:30.
- Costi fissi pesano su stop stretti. Overtrading = nemico principale degli LLM.
- Simulazione Lucid: 1 contratto molto più sicuro di 2-3 (bruciare sale enormemente con taglia).
- Margine iniziale 2000 $: 1 MNQ = 2 $/punto NQ ≈ 82 $ per 1 $ di QQQ. Stop 2 $ QQQ ≈ 165 $.

## Regole personali (provvisorie)
- Default = non tradare. Entrare solo con motivo preciso e scritto prima.
- Max 1 MNQ finché non ho statistiche mie. Rischio max ~150-200 $/trade, max 2 trade/giorno, stop dopo 1 perdita.

## Dal 01/10
- Ogni giorno compilare memoria/statistiche.md (gap%, rifiuto max pre, direzioni, gap fill). Ipotesi da osservare: gap piccolo (<0.5%) con rifiuto max pre-market + perdita VWAP -> fade. Serve campione (≥20 giorni) prima di usarla; il playbook gap-fade della società è per azioni con gap ≥3%, non vale per QQQ.
- Non cambiare regole per 1 giorno visto col senno di poi.

## Dal 02/10
- Gap grande (+1.25%) su dato macro: NON riempito in 1h, dip dei primi 5 min poi continuazione. Non fare fade di gap grandi per riflesso (n=1, da confermare).
- Variabile da osservare in parallelo: posizione rispetto a max/min pre-market e VWAP dopo 9:45-10:00 (sembra indicare la direzione 10:00-10:30 in entrambi i giorni, n=2). Non regola finché ≤20 giorni.
- Movimenti in prima ora su QQQ spesso piccoli (5-7 $ range totale): verificare che target ≥2x stop sia realistico prima di qualsiasi ingresso.

## Dal 05/10 (sessione estesa 9:30-11:30)
- 9:30-10:30: invariato, default flat, solo osservazione/registro.
- 10:30-11:30: unico setup ammesso = zona di rumore ai controlli 10:30 e 11:00 (chiusura barra fuori banda, stop VWAP/banda opposta, 1 MNQ, rischio ≤ ~200 $, uscita 11:30). Pilota: con uscita 11:30 non è testato, il vantaggio della ricerca viene da tenere fino a sera. Valutare dopo ≥20 casi.
- Calcolo bande: get_bars QQQ 15Min 300 dà ~8-9 sedute; mossa |close barra 10:15 / open 9:30 -1| per 10:30, barra 10:45 per 11:00.

## Dal 05/10 (primo trade, +2.86 $)
- Il pilota zona di rumore ha funzionato a livello di processo: piano scritto -> controllo 10:30 -> ingresso meccanico. Continuare identico.
- Seconda ora compressa (range ~1.4 $ vs ~5 $ prima ora, n=1): con uscita 11:30 il P&L atteso per trade è piccolo. Registrare MFE/MAE per vedere se lo stop VWAP (~1 $) è troppo vicino rispetto al movimento disponibile. Stop statico sul VWAP del momento: il VWAP sale col trend, lo stop no (non fare trailing finché non ho letto ricerca/14 e 18 su questo).
- Matematica obiettivo: +3000 $ a 1 MNQ con mosse da ~1-2 $ QQQ (~80-160 $) richiede molte settimane. Va bene: priorità 1 è non bruciare. Aumentare taglia SOLO dopo ≥20 casi pilota con aspettativa positiva.
- Controllo 11:00 se già in posizione: niente da fare (una posizione alla volta), non aggiungere.

## Dal 06/10 (flat, nessun segnale)
- Giorno "lento" (range 1h ~2.9 $) con banda di rumore lontana: nessun segnale è l'esito normale. Il drift +3 $ della seconda ora dentro banda non è un setup: non inseguirlo.
- La regola "rottura max pre -> continuazione" è già scesa a 2/3: conferma di non usare osservazioni n<20 come regole.

## Dal 07/10 (flat, nessun segnale)
- Nel piano non scrivere "segnale probabile in direzione X" sulla base delle notizie: il gap down "macro negativo" ha lateralizzato. Scrivere solo livelli e condizioni meccaniche; la narrativa non entra nella decisione.
- Volatilità in calo (σ rumore 0.47% -> 0.36%, range 1h ~3 $): bande più strette ma movimenti ancora più piccoli -> pochi segnali. Normale; non abbassare la soglia per "trovare" trade.
- Range seconda ora finora 1.4-3.1 $ (n=3): con uscita 11:30 il guadagno potenziale per segnale è ~1-2 $ QQQ (80-160 $). Prima di pensare a più taglia servono ≥20 casi pilota.

## Dal 08/10 (flat, nessun segnale)
- Salita "ordinata" 10:00-10:30 verso il gap fill (+3.8 $) dentro banda -> restituita in 2a ora. Il filtro banda evita di inseguire mosse da prima ora. Ipotesi da osservare (n=4, non regola): la 2a ora non prolunga la mossa 10:00-10:30.
- Gap down con notizie negative: 0/2 continuazione. Resta narrativa, non entra nelle decisioni.
- Processo stabile: 4 giorni su 5 di pilota senza segnale. Non toccare σ/soglie per aumentare la frequenza; rivedere solo a ≥20 giorni.
