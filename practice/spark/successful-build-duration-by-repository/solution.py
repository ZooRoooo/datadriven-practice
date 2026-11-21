from pyspark.sql import functions as F

# Filter successful builds during January 2026
filter_df = ci_builds.filter(
  (F.col("status") == "success") &
  (F.col("built_at") >= "2026-01-01 00:00:00") &
  (F.col("built_at") < "2026-02-01 00:00:00")
)

# Calculate total duration for each repository
result_df = (
  filter_df
  .groupBy("repo_name")
  .agg(F.sum("dur_secs").alias("total_dur_secs"))
)

# Include all repositories and replace NULL with 0
all_repos = ci_builds.select("repo_name").distinct()

final_df = (
  all_repos
  .join(result_df, on="repo_name", how="left")
  .fillna(0, subset=["total_dur_secs"])
  .orderBy("repo_name", ascending=True)
)

final_df.show()
