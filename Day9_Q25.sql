-- Category Buyers
-- The merchandising team is deciding how to concentrate their next promotional push. For each product category, they need to know how many unique customers made a purchase and how much revenue those purchases generated in total. Only include categories that have attracted at least three unique buyers ,
-- niche categories with a smaller audience aren't in scope. Rank from the most revenue to the least.

select p.category,
count(Distinct t.user_id) as unique_buyers,
round(sum(t.total_amount),2) as total_revenue
from transactions t
join products p on t.product_id = p.product_id
group by p.category
having count(Distinct t.user_id) >= 3
order by total_revenue desc
