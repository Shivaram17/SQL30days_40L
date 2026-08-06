-- The merchandising team needs a 2026 sales overview by product category.
-- For each category with at least one sale, show the number of unique transactions and total revenue, sorted from highest revenue to lowest.

select p.category,
count(Distinct t.transaction_id) as unique_transactions,
sum(t.total_amount) as total_revenue 
from transactions t
inner join products p on t.product_id = p.product_id
where t.transaction_date >= '2026-01-01' and t.transaction_date < '2027-01-01'
group by p.category
order by total_revenue desc;
