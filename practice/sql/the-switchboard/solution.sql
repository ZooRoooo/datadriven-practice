with LatestFlag As(
select flag_name,enabled,
row_number() over(
partition by flag_name
order by updated desc) as rn
from feat_flags)
select 
flag_name,
case when enabled=1  then 1 else 0 end as enabled_flag,
case when enabled=0  then 1 else 0 end as disabled_flag
from LatestFlag
where rn=1
order by flag_name;
