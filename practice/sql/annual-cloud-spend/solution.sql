select YEAR(bill_date) as years,
sum(amount) as total_spend from cloud_costs
group by years 
order by years asc
