results = ( 
            api_calls
            .groupBy("latency")
            .agg(
              F.count(F.col("latency")).alias("cnt")
              )
            .filter(
              F.col("cnt") <=2
              )
            .select(
              F.max(F.col("latency")).alias("max_unique_latency")
              )
            )
