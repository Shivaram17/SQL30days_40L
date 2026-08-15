select msg_id,channel,sender_id,content,msg_type,sent_at,edited,reply_to
 from chat_msgs
 where sender_id in (2,3)
 or content LIKE '%2%'
 or content LIKE '%3%'
