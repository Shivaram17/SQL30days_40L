


results = ( 
            infra_nodes
            .filter(F.col('region').isin('us-east-1', 'us-west-2', 'eu-west-1', 'eu-central-1', 'ap-southeast-1','ap-northeast-1')
              )
            .groupBy('region')
            .agg(F.count(F.col('region')).alias('node_count'))
            .orderBy(F.col('node_count').desc(), F.col('region'))
  
        )
              
              
  
