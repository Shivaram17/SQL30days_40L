
with cte as (
select u.user_id, t.transaction_id, t.product_id, t.quantity, p.category
from users u 
  join transactions t on u.user_id = t.user_id
  join products p on t.product_id = p.product_id
  where category is not NULL
  )
  
  select user_id,
  count(distinct category) as category_count
  from cte
  group by user_id
  having count(distinct category) > 1
  order by category_count desc;
