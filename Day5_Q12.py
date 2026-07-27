


# -- with cte as (select 
# --   topic,offset,
# --   lag(offset) over(partition by topic order by CAST(offset AS integer)) as prev_offset,
# --   dense_rank() over(partition by topic order by CAST(offset AS integer)) as msg_rank,
# --   row_number() over(partition by topic order by CAST(offset AS integer)) as msg_row_num
# -- from stream_msgs
# -- )


# -- select *
# -- from cte
# -- where prev_offset IS NOT NULL
from pyspark.sql import Window
from pyspark.sql import functions as F

wind_spec = Window.partitionBy("topic").orderBy(F.col("offset").asc())

result = (
          stream_msgs
          .withColumn("prev_offset", F.lag("offset").over(wind_spec))
          .withColumn("msg_rank", F.dense_rank().over(wind_spec))
          .withColumn("msg_row_num", F.row_number().over(wind_spec))
          .filter(F.col("prev_offset").isNotNull())
           .select(F.col("topic"), F.col("offset"), F.col("prev_offset"), F.col("msg_rank"), F.col("msg_row_num"))
  )
result.show()

