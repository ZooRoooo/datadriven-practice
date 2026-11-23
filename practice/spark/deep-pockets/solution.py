from pyspark.sql import functions as F

filter_df = transactions.filter(
  (F.col("transaction_date") >= "2026-03-01 00:00:00") &
  (F.col("transaction_date") < "2026-04-01 00:00:00")
)

result_df = (
  filter_df.groupBy("user_id")
  .agg(F.sum("total_amount").alias("total_revenue"))
  .orderBy("user_id",ascending="True")
)

result_df.show()
