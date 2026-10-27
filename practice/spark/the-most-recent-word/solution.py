from pyspark.sql import SparkSession
from pyspark.sql.functions import col, unix_timestamp, row_number, countDistinct, substring
from pyspark.sql.window import Window

# Initialize Spark session
spark = SparkSession.builder.appName("MostRecentWord").getOrCreate()

# 1. Convert text date to numeric timestamp and extract the calendar month (YYYY-MM)
df_processed = dq_checks.withColumn(
  "run_at_num", unix_timestamp(col("run_at"), "yyyy-MM-dd HH:mm:ss")
).withColumn(
  "year_month", substring(col("run_at"), 1, 7) # Extracts 'YYYY-MM'
)

# 2. Calculate the number of distinct calendar months per table using a standard groupBy
months_df = (
  df_processed
  .groupBy("tbl_name")
  .agg(countDistinct("year_month").alias("months_checked"))
)

# 3. Find the most recent check per table using a window function
window_spec = Window.partitionBy("tbl_name").orderBy(col("run_at_num").desc())
latest_df = (
  df_processed
  .withColumn("rn", row_number().over(window_spec))
  .filter(col("rn") == 1)
)

# 4. Join the latest check info with the months_checked summary
final_df = (
  latest_df
  .join(months_df, "tbl_name")
  .select("tbl_name", "rule", "run_at", "months_checked")
)

# Show the final output
final_df.show(truncate=False)
