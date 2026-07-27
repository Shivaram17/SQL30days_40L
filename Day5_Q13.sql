-- New vs Returning User Share
-- PySpark
-- A user is 'new' in the month of their very first event in event_data; in every subsequent month they are 'returning'.
-- For each month, compute the ratio of new users and returning users to total active users. Return the month, new user ratio, and returning user ratio.

with first_month as (
  select user_id,
        min(strftime('%Y-%m', event_timestamp)) AS first_month
  from event_data
  group by user_id
  ),
monthly_users as (
  SELECT DISTINCT
          strftime('%Y-%m', e.event_timestamp) AS month,
          e.user_id,
          f.first_month
      FROM event_data e
      JOIN first_month f
        ON e.user_id = f.user_id
)

select month,
count(case when month = first_month then 1 end) * 1.0/count(*) as new_user_ratio,
count(case when month > first_month then 1 end) * 1.0/count(*) as returnig_user_ratio
from monthly_users
group by month
order by month;
