-- Big Spenders
-- SQL
-- Marketing is launching a loyalty tier program and needs to identify high-value customers. For each user, calculate their total spending and the number of transactions they have made.
-- Only include users whose lifetime spending exceeds five hundred dollars. List them from highest spender to lowest.


select user_id,
sum(total_amount) as lifetime_spend,
count(*) as tx_count
from transactions
group by user_id
having sum(total_amount) > 500
order by sum(total_amount) desc;
