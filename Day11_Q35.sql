-- The merchandising team is benchmarking product quality across the catalog. For each category, they need the average customer rating rounded to one decimal place, but only for products that have actually received a rating.
--   Leave out any category with fewer than three rated products. List the results from highest average rating to lowest.

select category,
round(avg(rating),1) as avg_rating
from products
group by category
having avg_rating >= 2
order by avg_rating desc;
