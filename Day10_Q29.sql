select
sum(amount) as total_spend
from cloud_costs
group by svc_name
having svc_name = "EC2"
