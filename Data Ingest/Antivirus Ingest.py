# Databricks notebook source
# MAGIC %sql
# MAGIC use catalog kristin;

# COMMAND ----------

# MAGIC %sql
# MAGIC use schema threat_detection;

# COMMAND ----------

df_sharepoint = spark.table("kristin.threat_detection.sharepoint")

# COMMAND ----------

df_sharepoint.write.mode("overwrite").saveAsTable("kristin.threat_detection.sharepoint")