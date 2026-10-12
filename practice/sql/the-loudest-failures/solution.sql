select err_type, count(err_type) as err_count from 
err_tracks group by err_type 
order by err_count desc
