results = ( cloud_costs
            .groupBy("svc_name")
            .agg(F.sum(F.col("amount")).alias("total_spend"))
            .filter(F.col("svc_name") == "EC2")
            .select("total_spend")
            )

results.show()
