







# -- select session_id,
# -- user_id, session_duration_sec
# -- from user_sessions
# -- where session_duration_sec < 100 and year(session_start) = 2026;


results = (
          user_sessions
          .filter( (F.col("session_duration_sec") < 100) &
             ((F.col("session_start") >= "2026-01-01") & 
            (F.col("session_start") < "2027-01-01"))
            )
          .select("session_id", "user_id", "session_duration_sec")
          )
