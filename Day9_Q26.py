

# -- select p.category,
# -- count(Distinct t.user_id) as unique_buyers,
# -- round(sum(t.total_amount),2) as total_revenue
# -- from transactions t
# -- join products p on t.product_id = p.product_id
# -- group by p.category
# -- having count(Distinct t.user_id) >= 3
# -- order by total_revenue desc

# from pyspark.sql import functions as F

# results = ( transactions.alias("t")
#             .join(products.alias("p"), on = "product_id", how = "inner")
#             .groupBy("p.category")
#             .agg(F.countDistinct("t.user_id").alias("unique_buyers"),
#               F.sum("t.total_amount").alias("total_revenue")
#               )
#             .filter(F.col("unique_buyers") >= 3)
#             .select("category", "unique_buyers", "total_revenue")
#             .orderBy(F.col("total_revenue").desc())
#             )

# results.show()

from pyspark.sql import functions as F

results = (
  transactions.alias("t")
  .join(products.alias("p"), on="product_id", how="inner")
  .groupBy("category")
  .agg(
    F.countDistinct("t.user_id").alias("unique_buyers"),
    F.round(F.sum("t.total_amount"),2).alias("total_revenue")
  )
  .filter(F.col("unique_buyers") >= 3)
  .orderBy(F.col("total_revenue").desc())
)

results.show()
































