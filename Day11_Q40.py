
results = ( 
            chat_msgs
            .groupBy("channel")
            .agg(
              F.count("*").alias("total_messages"),
              F.countDistinct("sender_id").alias("unique_senders"),
              F.round(100.0 * (F.sum(F.when(F.col("edited") == 1, 1).otherwise(0)) / F.count("*"))).alias("edited_pct")
              )
            .filter(F.col("total_messages") > 4)
            .orderBy(F.col("total_messages").desc())
              
            )
  
