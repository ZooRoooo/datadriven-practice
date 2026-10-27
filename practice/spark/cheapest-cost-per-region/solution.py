from pyspark.sql import SparkSession
from pyspark.sql.functions import col, min

# Initialize Spark session
spark = SparkSession.builder.appName("CheapestCostPerRegion").getOrCreate()

# Group by region and find the minimum cloud cost amount
result_df = (
  cloud_costs
  .groupBy("region")
  .agg(min("amount").alias("min_cost"))
)

# Show the results
result_df.show(truncate=False)
