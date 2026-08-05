
select 
  svc_name,
  count(*) as total_alerts,
  count(case when lower(severity) = "critical" then 1 end) as critical_count,
  count(case when lower(severity) = "high_count" then 1 end) as high_count,
  sum(case when ack_by IS NULL then 1 else 0 end) as unacked_count,
  round( 1 * count(*) / count(distinct status), 2) as avg_per_status
from alert_events
group by svc_name
order by total_alerts desc
