SELECT 
  msg_id
  message,
  (LENGTH(TRIM(content)) - LENGTH(REPLACE(TRIM(content), ' ', ''))) + 1 AS word_count
FROM chat_msgs
WHERE message IS NOT NULL 
  AND TRIM(message) <> '';
