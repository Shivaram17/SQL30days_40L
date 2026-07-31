-- The Widest Net
-- SQL
-- The ad analytics team wants each campaign's true reach: how many different registered users clicked at least one of its ads,
-- counting a person once however many times they clicked. Keep campaigns that drew no clicks at all, and list the widest-reaching first.
  
select ad_campaign,
count(distinct case when clicked = 1 then user_id END) as users_reached
from ad_impressions
group by ad_campaign
order by users_reached desc;
