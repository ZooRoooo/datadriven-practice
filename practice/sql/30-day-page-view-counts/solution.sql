from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Initialize Spark session
spark = SparkSession.builder.appName("PageViewsCount").getOrCreate()

# 1. Filter for the year 2025 up to and including December 28
# Date format is TEXT ('YYYY-MM-DD' or timestamp string), so lexicographical string comparison works cleanly.
filtered_views = page_views.filter(
  col("viewed_at").between("2025-01-01", "2025-12-28 23:59:59")
)

# 2. Group by user_id and count total page views
result_df = filtered_views.groupBy("user_id").agg(
  count("view_id").alias("total_views")
)

# Show the results
result_df.show(truncate=False)
