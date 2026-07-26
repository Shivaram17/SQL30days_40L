-- Annual Cloud Spend Summary
-- SQL
-- The annual infrastructure review needs a slide showing how cloud spend and service sprawl have grown.
-- For each fiscal year, report the total amount spent and how many unique services appeared on the bill.


select 
  YEAR(bill_date) as fiscal_year,
  sum(amount) as total_spend,
  count(Distinct svc_name) as service_count
from cloud_costs
group by fiscal_year;






