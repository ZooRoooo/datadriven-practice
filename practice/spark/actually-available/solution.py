from pyspark.sql import functions as F
in_stock_df =(
  products.filter(F.col("in_stock")==True)
                     .agg(F.count("in_stock").alias("in_stock_count"))
)
in_stock_df.show()
