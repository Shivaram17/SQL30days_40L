

result = ( ad_impressions
           .filter(F.col("clicked") == 1)       
           .groupBy("ad_campaign")
           .agg(F.countDistinct(F.col("user_id")).alias("users_reached"))
           .select(F.col("ad_campaign"), "users_reached")
           .orderBy(F.col("users_reached").desc())
           )
  
result.show()













