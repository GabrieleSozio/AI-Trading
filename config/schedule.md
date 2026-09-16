# Orari e fusi

Le cron delle routine sono in **UTC**. L'ora di New York (ET) fa fede per il mercato.

| Ruolo | ET | UTC (EDT, fino al 31/10/2026) | UTC (EST, dal 2/11/2026) | Roma (fino al 24/10) |
|---|---|---|---|---|
| CIO | 08:40 | 12:40 | 13:40 | 14:40 |
| Trader | 09:20 (attivo fino a ~10:10) | 13:20 | 14:20 | 15:20 |
| Position Manager | 11:30 | 15:30 | 16:30 | 17:30 |
| Closer + Coach | 15:45 (coach dopo le 16:05) | 19:45 | 20:45 | 21:45 |
| Desk crypto (orario fisso in UTC) | sab e dom 11:00 (10:00 dal 2/11) | 15:00 | 15:00 | 17:00 (16:00 dal 25/10) |

## Cambi d'ora
- **Europa**: fine ora legale il 25/10/2026. Dal 25/10 al 1/11 Roma è 5 ore avanti a New York invece di 6.
- **USA**: fine ora legale il 1/11/2026. Da lunedì 2/11 le cron vanno spostate di +1h UTC.
- Inizio ora legale USA 2027: 14/03/2027; Europa: 28/03/2027.

## Regole per gli agenti
- Non fidarti dell'orario di avvio: le run possono partire qualche minuto dopo. Usa sempre `GET /v2/clock` e aspetta con `sleep` l'orario utile.
- Mezze giornate (nel 2026: 27/11, giorno dopo Thanksgiving, e 24/12): chiusura alle 13:00 ET. Il Closer legge `GET /v2/calendar` e anticipa la chiusura.
- Festivi: `GET /v2/clock` restituisce `is_open=false` e il prossimo `next_open` non è oggi. Le run di borsa escono subito.
