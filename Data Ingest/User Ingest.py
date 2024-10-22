# Databricks notebook source
# MAGIC %sql
# MAGIC use catalog kristin;

# COMMAND ----------

# MAGIC %sql
# MAGIC use schema threat_detection;

# COMMAND ----------

df_alert = spark.table("kristin.threat_detection.alert")

# COMMAND ----------

df_alert.write.mode("overwrite").saveAsTable("kristin.threat_detection.alert")