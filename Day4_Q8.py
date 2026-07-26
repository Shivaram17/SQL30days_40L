
from pyspark.sql import functions as F

result = (
          deploy_logs
          .filter(F.col("env_name").isin("dev", "Production"))
          .groupBy("author")
          .agg(F.countDistinct("env_name").alias("env_count"))
          .select("author", "env_count")
          )
result.show()
