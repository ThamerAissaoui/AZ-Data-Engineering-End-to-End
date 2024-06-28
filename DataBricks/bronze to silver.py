# Databricks notebook source
# MAGIC %md
# MAGIC # Level 1 Transformations

# COMMAND ----------

dbutils.fs.ls("/mnt/bronze/SalesLT/")

# COMMAND ----------

dbutils.fs.ls("/mnt/silver/")

# COMMAND ----------

input_path = '/mnt/bronze/SalesLT/Address/Address.parquet'
df = spark.read.format('parquet').load(input_path)
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC Cleanse the date column from each column containing date in wrong format, removing the timestamp keeping only the date in the right format!

# COMMAND ----------

# MAGIC %md
# MAGIC Side Note: %programming language, %  is called magic cell to execute besically any code from any programmimg language

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT 1 AS column1

# COMMAND ----------

table_name = []
# iterate into the bronze container
for i in dbutils.fs.ls('mnt/bronze/SalesLT/'):
    #get the directory name and append it to the table
    table_name.append(i.name.split('/')[0])



# COMMAND ----------

table_name

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType
# now we have the table neames lets iterate to that taqble and do the tansformation 

for i in table_name:
    path = '/mnt/bronze/SalesLT/' + i + '/' + i + '.parquet'
    df = spark.read.format('parquet').load(path)
    column = df.columns

    for col in column:
        if "Date" in col or "date" in col:
            df = df.withColumn(col, date_format(from_utc_timestamp(df[col].cast(TimestampType()), "UTC"), "yyyy-MM-dd"))
    output_path = '/mnt/silver/SalesLT/' +i +'/'
    #delta format for the silver conrtainer, delta is build ontop of parquet formnat, it is developed by databricks
    df.write.format('delta').mode("overwrite").save(output_path)




# COMMAND ----------

display(df)
