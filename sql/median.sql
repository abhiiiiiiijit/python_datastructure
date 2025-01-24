with cte_rn as (
    select lat_n, 
           row_number() over(order by lat_n) as row_n,
           count(*) over() as total_count
    from station
)
select round(avg(lat_n), 4) as median
from cte_rn
where row_n in (floor((total_count + 1) / 2.0), ceiling((total_count + 1) / 2.0));


