









select channel,
count(*) as total_messages,
count(Distinct sender_id) as unique_senders,
round(100.0 * sum(case when edited = 1 then 1 else 0 end ) / count(*), 1) as edited_pct
from chat_msgs
group by channel
having count(*) > 4
order by total_messages desc;
