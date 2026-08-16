results = (
           users.alias("u")
           .join(user_sessions.alias("s"), how = "inner", on = "user_id")
           .join(devices.alias("d"), how = "inner", on = "device_id")
           .select("username", "device_type").distinct()
            )
