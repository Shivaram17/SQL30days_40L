segmented = ( 
            api_calls
            .filter(F.col("call_time").isNotNull())
            .withColumn("day_of_week",  F.dayofweek("call_time") - 1)
            .withColumn("time_segment", 
              F.when(F.hour("call_time") < 12, "Morning")
              .when(F.hour("call_time") <= 15, "Early Afternoon")
              .otherwise("Late Afternoon")
              )
            .groupBy("day_of_week", "time_segment")
            .agg(F.count("*").alias("call_count"))
          )
window_spec = Window.orderBy(F.col("call_count").desc())

results = ( segmented
            .withColumn("rnk", F.dense_rank().over(window_spec))
            .filter(F.col("rnk") <= 2)
            .select("day_of_week", "time_segment", "call_count")
            )

results.show()
