select creator_id,
avg(duration_seconds) as avg_duration
from content_items 
group by creator_id
having sum(duration_seconds)>3600
order by avg_duration desc
