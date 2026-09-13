results = ( 
            transactions
            .join(products, on = "product_id", how = "inner")
            .groupBy("user_id")
            .agg(F.countDistinct("category").alias("category_count"))
            .orderBy(F.col("category_count").desc())
            )
