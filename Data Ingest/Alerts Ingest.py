# Databricks notebook source
# MAGIC %sql
# MAGIC use catalog kristin;

# COMMAND ----------

# MAGIC %sql
# MAGIC use schema threat_detection;

# COMMAND ----------

df_users = spark.table("kristin.threat_detection.users")

# COMMAND ----------

df_users.write.mode("overwrite").saveAsTable("kristin.threat_detection.users")