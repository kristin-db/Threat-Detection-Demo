# Databricks notebook source
# MAGIC %sql
# MAGIC use catalog kristin;

# COMMAND ----------

# MAGIC %sql
# MAGIC use schema threat_detection;

# COMMAND ----------

df_email = spark.table("kristin.threat_detection.email")

# COMMAND ----------

df_email.write.mode("overwrite").saveAsTable("kristin.threat_detection.normalized")