select * from alert_events
WHERE strftime('%Y', 	fired_at) = '2026'
and  lower(severity) IN ('high', 'critical');
