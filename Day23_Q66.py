
results = (
            api_tokens
            .filter(
              (F.col("issued") >= "2026-01-01") & (F.col("issued") < "2027-01-01")
              )
            .select(F.countDistinct("owner_id").alias("distinct_owner"))
            )

results.show()
