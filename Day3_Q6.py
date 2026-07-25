# All Infra Regions
# PySpark
# Before provisioning a new availability zone, the infrastructure team
# needs to know which regions already have node presence. Pull a deduplicated list of every region currently represented in the node inventory.

result = (infra_nodes.select("region").distinct())

result.show()
