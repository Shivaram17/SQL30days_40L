from pyspark.sql import functions as F

result = (
    ad_impressions
    .groupBy("ad_campaign")
    .agg(
        F.count("*").alias("impressions"),
        F.sum("revenue").alias("total_revenue"),
        F.round(
            F.lit(100.0) * F.sum("clicked") / F.count("*"),
            1
        ).alias("ctr")
    )
    .filter(F.col("impressions") > 5)
    .orderBy(F.col("ctr").desc())
)

result.show()
