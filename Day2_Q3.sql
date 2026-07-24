Active Campaigns
SQL
The advertising team is evaluating campaign performance for the quarterly review. For each ad campaign, show the number of impressions served, the total revenue generated, and the click-through rate as a percentage rounded to one decimal place. Only include campaigns with more than five impressions, presented from highest click-through rate to lowest.








select ad_campaign,
count(*) as impressions,
sum(revenue) as total_revenue,
round(100.0 * sum(clicked)/count(*), 1) as ctr
from ad_impressions
group by ad_campaign
having impressions > 5
order by ctr desc;
