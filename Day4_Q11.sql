-- Who's Holding Up Traffic
-- PySpark
-- The API product team wants to understand typical daily traffic per endpoint during June 2026. For each endpoint, what was the average number of unique users hitting it on a given day that month?




select endpoint,
AVG(daily_users) as avg_daily_active_users
from
  ( 
  select endpoint,
  DATE(call_time) as call_day,
  count(distinct user_id) as daily_users
  from api_calls
  where strftime("%Y-%m", call_time) = "2026-06"
  group by endpoint, DATE(call_day)
  )
group by endpoint
order by endpoint;

  
