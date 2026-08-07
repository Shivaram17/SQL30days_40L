-- The Quiet Outlier
-- An SRE is chasing a latency outlier but wants to set aside the readings that show up constantly across normal traffic.
-- Among the latency values that appear no more than twice in all API calls, surface the largest one.

with rare_latencies as
  (
    select latency
    from api_calls
    group by latency
    having count(*) <= 2
  )

select max(latency) as max_unique_latency
 from rare_latencies 
