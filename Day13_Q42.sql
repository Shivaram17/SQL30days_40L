from pyspark.sql import functions as F
results = ( 
  chat_msgs
  .withColumn(
    "word_count", F.size(F.split(F.col("content")))
    )
  .select("msg_id", "word_count")
  )

results.show()
