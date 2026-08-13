results = (
          cdn_logs
          .filter(F.col("status") < 400)
          .select(F.col("edge_loc"))
          .dropDuplicates(F.col("edge_loc"))
          )
