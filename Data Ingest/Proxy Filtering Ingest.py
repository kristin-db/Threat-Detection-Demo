# Databricks notebook source
# MAGIC %sql
# MAGIC use catalog kristin;

# COMMAND ----------

# MAGIC %sql
# MAGIC use schema threat_detection;

# COMMAND ----------

df_antivirus = spark.table("kristin.threat_detection.antivirus")

# COMMAND ----------

df_antivirus.write.mode("overwrite").saveAsTable("kristin.threat_detection.antivirus")