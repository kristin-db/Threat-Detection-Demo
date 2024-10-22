# Databricks notebook source
# MAGIC %sql
# MAGIC use catalog kristin;

# COMMAND ----------

# MAGIC %sql
# MAGIC use schema threat_detection;

# COMMAND ----------

df_url_filtering = spark.table("kristin.threat_detection.url_filtering")

# COMMAND ----------

df_url_filtering.write.mode("overwrite").saveAsTable("kristin.threat_detection.url_filtering")