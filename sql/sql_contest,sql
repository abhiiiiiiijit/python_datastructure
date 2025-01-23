with cte_min_date as(
select min(submission_date)min_date from submissions
)
,
cte_each_day_unique_hacker as (
select 
    submission_date,
    hacker_id
    
    from submissions 
    where submission_date = (select min_date from cte_min_date)
    union all
    select 

    s.submission_date,
    s.hacker_id
    from cte_each_day_unique_hacker cs
    inner join submissions s on cs.hacker_id = s.hacker_id and
    s.submission_date = dateadd(day,1,cs.submission_date)
    
), cte_unique as(
    select 
   submission_date,
    count(distinct hacker_id) count_h

    from cte_each_day_unique_hacker
     group by submission_date
), cte_cnt_sub as (
    select 
   submission_date,
    hacker_id,
  count(hacker_id) count_h

    from submissions
    group by submission_date, hacker_id
    -- having count(hacker_id) = count(hacker_id)
), cte_max_sub as (
select 
   submission_date,
    max(count_h) max_cnt
   from cte_cnt_sub
   group by submission_date
  --  having max(count_h) = count_h
    
), cte_max_sub_hacker as (
select 
    ccs.submission_date,
    min(ccs.hacker_id) as hacker_id
    from cte_cnt_sub ccs
    inner join cte_max_sub cms on ccs.submission_date = cms.submission_date
    and ccs.count_h = cms.max_cnt
    group by ccs.submission_date
)
select 
cu.submission_date,
cu.count_h,
cmsh.hacker_id,
h.name

from cte_unique cu
inner join cte_max_sub_hacker cmsh on cu.submission_date = cmsh.submission_date
inner join hackers h on cmsh.hacker_id = h.hacker_id
order by 1



--where submission_date = '2016-03-03' and hacker_id = 18105
