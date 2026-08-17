with segmented as (
select 
  cast(strftime('%w', call_time) as integer ) as day_of_week,
  case
      when cast(strftime('%H', call_time) as integer) < 12 THEN 'Morning'
      when cast(strftime('%H', call_time) as integer) <= 15 THEN 'Early Afternoon'
      else 'Late Afternoon'
     end as time_segment,
  count(*) as call_count
from api_calls
where call_time is not null
group by day_of_week, time_segment
),
ranked as (
    select *,
    dense_rank() over(order by call_count desc) as rnk
    from segmented
    )

select day_of_week,
time_segment,
call_count
from ranked
where rnk <=2;
