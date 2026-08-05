from pyspark.sql import functions as F

results = (
  alert_events
  .groupBy("svc_name")
  .agg(
    F.count("*").alias("total_alerts"),

    F.count(
      F.when(F.lower(F.col("severity")) == "critical", 1)
    ).alias("critical_count"),

    F.count(
      F.when(F.lower(F.col("severity")) == "high", 1)
    ).alias("high_count"),

    F.sum(
      F.when(F.col("ack_by").isNull(), 1).otherwise(0)
    ).alias("unacked_count"),
    
    F.round(
      F.count("*")/F.countDistinct("status"), 2).alias("avg_per_status")
    )
  .orderBy("total_alerts").desc()
)


results.show()
