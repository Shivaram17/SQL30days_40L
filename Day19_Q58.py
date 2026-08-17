
results = ( 
            api_calls
            .withColumn("endpoint", F.rtrim("endpoint"))
            .select("call_id", "endpoint")
            )
results.show()
