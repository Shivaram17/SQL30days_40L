
# -- select 
# --   YEAR(bill_date) as fiscal_year,
# --   sum(amount) as total_spend,
# --   count(Distinct svc_name) as service_count
# -- from cloud_costs
# -- group by fiscal_year;
from pyspark.sql import functions as F

result = (
          cloud_costs
          .withColumn("fiscal_year", F.year(F.col("bill_date").cast("date")))
          .groupBy(F.col("fiscal_year"))
          .agg(
            F.sum("amount").alias("total_spend"),
            F.countDistinct("svc_name").alias("service_count")
            )
          .select("fiscal_year","total_spend", "service_count")
          )
result.show()







