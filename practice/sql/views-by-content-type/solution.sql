
SELECT
  e.content_type,
  COUNT(c.view_id) AS view_count
FROM content_views c
INNER JOIN content_items e 
  ON c.content_id = e.content_id
GROUP BY e.content_type
ORDER BY e.content_type;
