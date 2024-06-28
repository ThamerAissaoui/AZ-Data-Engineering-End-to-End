# Databricks notebook source
# MAGIC %md
# MAGIC # Level 2 Transformations: bronze to silver

# COMMAND ----------

# MAGIC %md
# MAGIC Common transformations among companies is to transform the names of the coloumns according to a naming convention or policy, eg. : ProductName => product_name

# COMMAND ----------

# mouunting the gold container
dbutils.fs.ls("/mnt/gold/")

# COMMAND ----------

table_name = []
# iterate into the silver container
for i in dbutils.fs.ls('mnt/silver/SalesLT/'):
    #get the directory name and append it to the table
    table_name.append(i.name.split('/')[0])

# COMMAND ----------

table_name

# COMMAND ----------

for name in table_name:
    print(name)
    path  = '/mnt/silver/SalesLT/' + name
    print(path)
    df = spark.read.format('delta').load(path)


    # get the list of column names
    column_names = df.columns

    for old_col_name in column_names:
        # convert column name from ColumnN?mae ktro Column_Name format
        new_col_name = "".join(["_" + char if char.isupper() and not old_col_name[i - 1].isupper() else char for i, char in enumerate(old_col_name)]).lstrip("_")

        # Change the column name using withColumnRenamed and regexp_replace
        df = df.withColumnRenamed(old_col_name, new_col_name)

    output_path = '/mnt/gold/SalesLT/' +name +'/'
    df.write.format('delta').mode("overwrite").save(output_path)

# COMMAND ----------

display(df)
