-- The warehouse team is prepping inventory numbers for the quarterly review. They need to see how many products sit in each category, 
-- but only categories that carry more than eight items are worth discussing. Show the category and the product tally, sorted from largest category to smallest.

select category,
count(*) as product_count
from products
group by category
having product_count > 8
order by product_count desc;
