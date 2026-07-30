
# -- select Distinct product_name
# --  from products
# -- where price >=5 and price <=20
result = ( products
           .filter((F.col("price") >= 5) & (F.col("price") <=20))
           .select(F.Distinct(F.col("product_name")))
          )
result.show()
