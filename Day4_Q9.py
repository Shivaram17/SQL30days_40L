

from pyspark import functions as F

result = ( 
          dq_checks
          .groupBy("tbl_name")
          .agg(F.avg("fail_pct").alias("avg_fail_pct"),
            F.countDistinct("rule").alias("rule_count"))
          .filter(F.col("rule_count") > 1)
          .select("tbl_name", "avg_fail_pct")
          .orderBy(F.col("avg_fail_pct").desc())
          )
result.show()
