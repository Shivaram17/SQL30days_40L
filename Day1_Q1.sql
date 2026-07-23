#Above Average Interactions
#SQL
#A downstream report shows a small set of power users drives most of the platform's session volume.
#Pull every user whose total session count exceeds the average session count across all users, and show their user ID alongside that total.

with cte as (select user_id,
count(*) as cnt
from user_sessions
group by user_id)

select user_id,
count(*) as total_sessions
from user_sessions
group by user_id
having count(*) > (
  select 
  avg(cnt)
  from cte)
  order by total_sessions desc;



