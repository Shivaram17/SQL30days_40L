Beyond the Signup
SQL
The product org tracks engagement trends month over month. For the last 6 months, show the count of unique active users and the average session duration per month. Only include months where the total number of sessions exceeded 3. Present the results chronologically.

select 
  strftime('%Y-%m', session_start) as month,
  count(distinct user_id) as active_users,
  avg(session_duration_sec) as avg_duration_sec
  from user_sessions
  where session_start >= DATE('2026-12-28', '-6 months')
  group by month
  having count(*) > 3
  order by month


