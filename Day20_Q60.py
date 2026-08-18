
results = (
            content_views
            .join(content_items, on = "content_id", how = "inner")
            .groupBy("content_type")
            .agg(F.count(F.col("view_id")).alias("view_count"))
            )
