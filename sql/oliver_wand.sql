select id,age,coins_needed,power from
(
select distinct  w.id, wp.age,min(w.coins_needed) over(partition by wp.age,w.power ) as coins_needed,w.power 
,row_number() over(partition by wp.age,w.power order by w.coins_needed) as r_n
from wands as w
inner join Wands_Property as wp on w.code = wp.code
where wp.is_evil = 0 ) as i_q
where r_n = 1
order by power desc, age desc
