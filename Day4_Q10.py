# The Ones Worth Paging
# PySpark
# The SRE team is building a triage chart covering the three severity levels that call for action:
# CRITICAL, ERROR, and WARN. Show each of these levels alongside the total number of log entries recorded for it.
from pyspark.sql import functions as F
result = (
          server_logs
          .filter(F.col("log_level").isin("CRITICAL","ERROR","WARN"))
          .groupBy("log_level")
          .agg(F.count("*").alias("total_count"))
          .select("log_level", "total_count")
          )

result.show()
