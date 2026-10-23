WITH transction_detail AS (
    SELECT 
        p.category,
        (t.quantity * p.price) AS total_spent 
    FROM transactions t 
    JOIN products p
        ON t.product_id = p.product_id
)
SELECT 
    category, 
    SUM(total_spent) AS total_spent 
FROM transction_detail
GROUP BY category 
ORDER BY category;
