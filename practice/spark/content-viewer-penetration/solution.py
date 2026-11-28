from pyspark.sql import functions as F

user = users.alias("u")
context = content_views.alias("c")

total_user = users.count()

result_df = user.join(
  context,
  F.col("u.user_id") == F.col("c.user_id"),
  "inner"
).filter(
  F.col("c.viewed_at").isNotNull()
)

viewer_pct = (
  result_df.select("u.user_id").distinct().count() / total_user
) * 100

result_df = spark.createDataFrame(
  [(viewer_pct,)]
).toDF("viewer_pct")

result_df.show()
