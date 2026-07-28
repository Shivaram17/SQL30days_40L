





# -- select user_id,
# -- sum(total_amount) as lifetime_spend,
# -- count(*) as tx_count
# -- from transactions
# -- group by user_id
# -- having sum(total_amount) > 500
# -- order by sum(total_amount) desc;

from pyspark.sql import functions as F

result = ( 
          transactions
          .groupBy(F.col("user_id"))
          .agg(F.sum(F.col("total_amount")).alias("lifetime_spend"),
              F.count(F.col("*")).alias("tx_count")
          )
          .filter(F.col("lifetime_spend") > 500)
          .select("user_id","lifetime_spend", "tx_count")
          .orderBy(F.col("lifetime_spend").desc())
          )
          
result.show()
