from pyspark.sql import functions as F

rating_expr = (
  F.when(F.col("clicked_result").isin([1, 2, 3]), F.lit(3))
  .when(F.col("clicked_result") > 3, F.lit(2))
  .otherwise(F.lit(1))
)

result_df = search_queries.select(
  F.col("query_id"),
  rating_expr.alias("rating"),
)

result_df.show()
