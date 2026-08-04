

results = ( products
            .groupBy("category")
            .agg(F.count("*").alias("product_count"))
            .filter(F.col("product_count") > 8)
            .orderBy(F.col("product_count").desc())
            )
results.show()
