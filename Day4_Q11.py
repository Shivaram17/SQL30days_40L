# -- select endpoint,
# -- AVG(daily_users) as avg_daily_active_users
# -- from
# --   ( 
# --   select endpoint,
# --   DATE(call_time) as call_day,
# --   count(distinct user_id) as daily_users
# --   from api_calls
# --   where strftime("%Y-%m", call_time) = "2026-06"
# --   group by endpoint, DATE(call_day)
# --   )
# -- group by endpoint
# -- order by endpoint;

from pyspark.sql import functions as F
result = (
          api_calls
          .withColumn("call_day", F.date(F.col("call_time")))
          .filter((F.col("call_time") >= "2026-06-01") & (F.col("call_time") <= "2026-06-30"))
          .groupBy("endpoint", F.date(F.col("call_time")))
          .agg(F.countDistinct("user_id").alias("daily_users"))
          .select("*")
        )

final_result = (result
                .groupBy("endpoint")
                .agg(F.avg("daily_users").alias("avg_daily_active_users"))
                .select("*")
                .orderBy("endpoint")
              )
final_result .show()


  
