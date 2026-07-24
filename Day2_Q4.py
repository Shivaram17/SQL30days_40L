result = (
        user_sessions
        .filter( F.col("session_start") >= F.add_months(F.current_date(), - 6))
        .groupBy(F.date_trunc("month", "session_start").alias("month_new"))
        .agg(F.countDistinct("user_id").alias("active_users"),
          F.avg("session_duration_sec").alias("avg_duration_sec"),
          F.count("*").alias("total_sessions")
          )
        .filter(F.col("total_sessions") > 3)
        .drop("total_sessions")
        .orderBy("month_new")
          )
result.show()
