
-- Authors Deploying to Dev and Production
-- SQL
-- The release engineering team wants to identify authors who ship to both the dev and production environments 
-- (case-insensitive match). Show each qualifying author and how many of those two environments they have deployed to, listed alphabetically.



with cte as (
select * from deploy_logs
where env_name in ("dev", "production")
)
select  
  author,
  count(Distinct env_name)
from cte
group by author;
