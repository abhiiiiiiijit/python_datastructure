SET cte_max_recursion_depth=10000000;
with recursive cte_days(    task_id,
    start_date,
    end_date, days) as (
    select *, 1 as days
    from projects
    union all
    select 
    d.task_id,
    d.start_date,
    p.end_date,
    d.days + 1 as days
    from  cte_days d
    inner join projects p
    on d.end_date = p.start_date
    
), cte_srt as (
    select start_date,
          max(end_date) end_date,
        max(days) as days

from cte_days
group by start_date
)
    select min(start_date),
          end_date 

from cte_srt
group by end_date

order by max(days) , min(start_date)

;

WITH PSEQ AS (SELECT Task_ID, Start_Date, End_Date, 
              DATE_SUB(Start_Date,INTERVAL (ROW_NUMBER() OVER (ORDER BY Start_Date)) DAY) AS PGroup 
              FROM Projects)

SELECT
    MIN(Start_Date) AS PStart,
    MAX(End_Date) AS PEnd
FROM
    PSEQ
GROUP BY
    PGroup
ORDER BY COUNT(*) ASC, MIN(Start_Date) ASC
;