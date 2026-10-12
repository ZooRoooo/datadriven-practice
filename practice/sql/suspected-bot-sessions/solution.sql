select session_id,user_id,session_duration_sec from user_sessions
where session_duration_sec<100
and session_start between '2026-01-00 00:00:00' and '2026-12-31 59:59:59';
