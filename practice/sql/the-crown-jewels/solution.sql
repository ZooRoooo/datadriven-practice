select p.product_name,sum(t.total_amount) as total_revenue
from products p inner join transactions t 
on p.product_id=t.product_id
group by product_name
order by total_revenue  desc
limit 5
