from pyspark import functions as F

result_df= user_sessions \
          .withColumn("session_date",F.to_date("session_start"))\
          .groupBy("session_date")\
          .agg(
              F.count("user_id").alias("total_sessions"),
              F.countDistinct("user_id").alias("unique_users")            
            ) \
          .orderBy(F.col("session_date"),ascending=True)
          
result_df.show()
