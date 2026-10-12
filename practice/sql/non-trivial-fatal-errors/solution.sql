SELECT
  err_id,
  message,
  svc_name,
  CASE
    WHEN LENGTH(message) < 25 THEN 'short'
    WHEN LENGTH(message) BETWEEN 25 AND 35 THEN 'mid'
    ELSE 'long'
  END AS length_category
FROM err_tracks
WHERE LOWER(severity) = 'fatal'
  AND LENGTH(message) >= 25;
