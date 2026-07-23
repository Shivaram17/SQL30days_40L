--Above Average Product Prices
--SQL
--The finance team defines a product's base price as the lowest transaction amount ever recorded for it. 
--They want to flag products whose base price runs above the average base price across all products. Return the product ID and its base price.

with cte as (
select product_id,
min(total_amount) as base_price
from transactions 
group by product_id)

select product_id, base_price
from cte
where base_price > (select avg(base_price) from cte);
