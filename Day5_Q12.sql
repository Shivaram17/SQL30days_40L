-- Alert Severity
-- SQL
-- The streaming infrastructure team is analyzing message ordering within each topic. For each message, show its offset, the previous message's offset within the same topic,
-- its dense rank by offset within the topic, and its sequential row number within the topic. Only include messages that have a predecessor in the same topic.




with cte as (select 
  topic,offset,
  lag(offset) over(partition by topic order by CAST(offset AS integer)) as prev_offset,
  dense_rank() over(partition by topic order by CAST(offset AS integer)) as msg_rank,
  row_number() over(partition by topic order by CAST(offset AS integer)) as msg_row_num
from stream_msgs
)


select *
from cte
where prev_offset IS NOT NULL

