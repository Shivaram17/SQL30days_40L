-- Average DQ Fail Rate
-- PySpark
-- Several downstream consumers are complaining about bad data but nobody knows which source tables are the worst offenders. Compute the average data quality check fail rate per table, 
-- but only surface tables where more than one validation rule has actually been evaluated. Show the table name and its average fail percentage.

select tbl_name,
avg(fail_pct) as avg_fail_pct
from dq_checks
group by tbl_name
having count(distinct rule) > 1
order by avg_fail_pct desc
