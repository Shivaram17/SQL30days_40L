results = (
          products
          .join(transactions, how = "left", on = "product_id")
          .groupBy("product_name")
          .agg(
            F.sum(F.when(F.col("category") == "Electronics", F.col("total_amount"))).alias("electronics_total")
            )
          .orderBy(F.col("electronics_total").desc(),  F.col("product_name"))
          .fillna(0, subset=["electronics_total"])
          )
