results = (
          api_tokens
          .filter(~F.col("scope").startswith("read"))
          .select(F.countDistinct("owner_id").alias("non_read_owner_count"))
          )
