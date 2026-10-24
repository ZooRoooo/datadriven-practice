import pyspark.sql.functions as F

# Assuming 'api_tokens_df' is your input DataFrame
result_df = (
  api_tokens
  # Extract the second character of the scope column (1-indexed in PySpark)
  .withColumn("second_char", F.substring(F.col("scope"), 2, 1))
  # Apply the multi-level sorting rules
  .orderBy(
    F.col("second_char").asc(),  # 1. Alphabetically by the second character of scope
    F.col("issued").asc(),       # 2. Earliest issued to latest
    F.col("token_id").asc()      # 3. Lowest token_id first for ties
  )
  # Select only the required columns for the audit trail
  .select("token_id", "scope")
)
