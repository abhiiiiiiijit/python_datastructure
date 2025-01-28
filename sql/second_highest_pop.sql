-- select distinct population from cities
-- order by population desc
-- OFFSET  1 
-- limit 1


-- select population
-- from cities as c1
-- where 1 = (select count(1) from cities as c2 where c1.population<c2.population )

with cte_rank as(
select 
population,
DENSE_RANK() over(order by population desc ) as r_c
from cities as c1

)
select population
from cte_rank
where r_c = 2


