from pyspark.sql import functions as F

# 2. Filter and select
results = (
    chat_msgs
    .filter(
        (F.col("sender_id").isin(2, 3)) | 
        (F.col("content").contains("2")) | 
        (F.col("content").contains("3"))
    )
    .select("msg_id", "channel", "sender_id", "content", "msg_type", "sent_at", "edited", "reply_to")
)
