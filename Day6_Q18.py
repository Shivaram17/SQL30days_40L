from pyspark.sql import functions as F

# Team 1 statistics
team1_df = (
    matches
    .select(
        F.col("team1").alias("team"),
        F.when(F.col("winner") == F.col("team1"), 1).otherwise(0).alias("won"),
        F.when(F.col("winner") != F.col("team1"), 1).otherwise(0).alias("lost")
    )
)

# Team 2 statistics
team2_df = (
    matches
    .select(
        F.col("team2").alias("team"),
        F.when(F.col("winner") == F.col("team2"), 1).otherwise(0).alias("won"),
        F.when(F.col("winner") != F.col("team2"), 1).otherwise(0).alias("lost")
    )
)

# UNION ALL
team_stats = team1_df.unionByName(team2_df)

# Aggregate
result = (
    team_stats
    .groupBy("team")
    .agg(
        F.count("*").alias("played"),
        F.sum("won").alias("won"),
        F.sum("lost").alias("lost")
    )
    .orderBy(
        F.col("won").desc(),
        F.col("played").desc()
    )
)

result.show()
