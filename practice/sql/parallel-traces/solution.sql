SELECT DISTINCT
    e1.user_id AS user_id1,
    e2.user_id AS user_id2
FROM 
    experiments e1
JOIN 
    experiments e2 
    ON e1.exp_name = e2.exp_name                  -- Same experiment
   AND LOWER(e1.platform) = LOWER(e2.platform)    -- Same platform (case-insensitive)
   AND e1.variant <> e2.variant                  -- Different variants
   AND e1.user_id < e2.user_id                   -- Unique pair order (prevents self-matches & mirror duplicates)
ORDER BY 
    user_id1 ASC,
    user_id2 ASC;
