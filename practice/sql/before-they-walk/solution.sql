select u.user_id,u.username,
sum(t.total_amount) as lifetime_spend
from users u  inner join 
transactions t on  u.user_id=t.user_id
group by u.user_id,
u.username
order by lifetime_spend desc
limit 10;
