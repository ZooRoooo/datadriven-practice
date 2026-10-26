SELECT 
    COALESCE(ack_by, 'unassigned') AS responder,
    COUNT(*) AS total_alerts
FROM alert_events
GROUP BY COALESCE(ack_by, 'unassigned')
ORDER BY total_alerts;
