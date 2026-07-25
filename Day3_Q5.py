



















# -- select count(Distinct t.user_id) as active_users_with_transactions
# -- from transactions t
# -- left join users u on t.user_id = u.user_id
# -- where u.account_status = 'active' and
# --  (t.transaction_date >= '2026-04-01' and  t.transaction_date <= '2026-04-30')
# -- group by t.user_id;
# from pyspark.sql import functions as F
# result = (transactions
#           .join(users, on='user_id', how = 'left')
#           .filter(
#             (F.col('account_status') == 'active') &
#             (F.col('transaction_date').substr(1,7) == F.lit('2026-04'))
#           ))

result = (
  transactions
  .join(
    users,
    on="user_id",
    how="left"
  )
  .filter(
    (F.col("account_status") == "active") &
    (F.col("transaction_date") >= F.lit("2026-04-01")) &
    (F.col("transaction_date") < F.lit("2026-05-01"))
  )
  .agg(F.countDistinct("user_id").alias("active_users_with_transactions"))
)

result.show()
