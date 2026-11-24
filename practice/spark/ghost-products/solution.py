from pyspark.sql import functions as F

result_df = products.join(
  transactions,
  on="product_id",
  how="left_anti"
)

final_df = result_df.select("product_name") \
  .orderBy(F.col("product_name").asc())

final_df.show()
