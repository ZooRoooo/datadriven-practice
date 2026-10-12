select nspace,pod_name,mem_used from k8s_pods
where mem_used is not null 
group by pod_name
order by mem_used  asc 
limit 5;
