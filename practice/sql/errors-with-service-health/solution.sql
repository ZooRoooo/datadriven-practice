select e.err_id,e.err_type,e.message,e.svc_name,e.severity,e.count,e.first_at,
s.status,s.latency,s.uptime from err_tracks e inner join svc_health s
on  e.svc_name=s.svc_name
