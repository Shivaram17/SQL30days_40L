

# -- select p.category,
# -- count(Distinct t.transaction_id) as unique_transactions,
# -- sum(t.total_amount) as total_revenue 
# -- from transactions t
# -- inner join products p on t.product_id = p.product_id
# -- where t.transaction_date >= '2026-01-01' and t.transaction_date < '2027-01-01'
# -- group by p.category
# -- order by total_revenue desc;

results = ( 
            transactions.alias("t")
            .join(products.alias("p"), on = "product_id", how = "inner")
            .filter(
              (F.col("t.transaction_date") >= "2026-01-01") & 
              (F.col("t.transaction_date") < "2027-01-01")
              )
            .groupBy("category")
            .agg(
              F.countDistinct(
                F.col("t.transaction_id")).alias("unique_transactions")
                ,
              F.sum(
                F.col("t.total_amount")).alias("total_revenue")
              )
            .orderBy(
              F.col("total_revenue").desc()
              )
          )

results.show()
  
  











