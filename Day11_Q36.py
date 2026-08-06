results = ( 
            products
            .groupBy("category")
            .agg(
                  F.round(F.avg("rating"),1).alias("avg_rating")
              )
            .filter(F.col("avg_rating") >= 2)
            .orderBy(F.col("avg_rating").desc())
        )

results.show()
