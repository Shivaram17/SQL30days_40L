results =(
          page_views
          .filter(
          (F.col("viewed_at") >= "2026-11-28") & (F.col("viewed_at") < "2026-12-29")
          )
          .groupBy("user_id")
          .agg(F.count("*").alias("total_views"))
          .orderBy(F.col("total_views").desc(), "user_id")
          )
