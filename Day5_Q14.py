

from pyspark.sql import functions as F

# First month for each user
first_month = (
    event_data
    .groupBy("user_id")
    .agg(
        F.min(F.date_format("event_timestamp", "yyyy-MM")).alias("first_month")
    )
)

# Distinct active users per month
monthly_users = (
    event_data
    .select(
        F.date_format("event_timestamp", "yyyy-MM").alias("month"),
        "user_id"
    )
    .distinct()
    .join(first_month, on="user_id")
)

# Calculate ratios
result = (
    monthly_users
    .groupBy("month")
    .agg(
        (
            F.count(F.when(F.col("month") == F.col("first_month"), True))
            / F.count("*")
        ).alias("new_user_ratio"),

        (
            F.count(F.when(F.col("month") > F.col("first_month"), True))
            / F.count("*")
        ).alias("returning_user_ratio")
    )
    .orderBy("month")
)

result.show()


