result = ( repo_commits
           .groupBy("author")
           .agg(F.countDistinct(F.col("repo_name")).alias("repo_count"))
           .filter(F.col("repo_count") > 1)
           .select(F.lower(F.col("author")).alias("author"), F.col("repo_count")).distinct()
          )

result.show()

 





