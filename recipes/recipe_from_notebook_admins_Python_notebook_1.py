# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
from dataiku import spark as dkuspark
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
from pyspark.ml.stat import Correlation
from pyspark.ml.feature import VectorAssembler
from pyspark.sql.types import StructType, StructField, StringType

import math
import pandas as pd
import numpy as np

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
fitness = dataiku.Dataset("FITNESS")
fitness_df = dkuspark.get_dataframe(sqlContext, fitness)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
fitness_df = fitness_df.dropna()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
column_names = fitness_df.columns
corr_method = dataiku.get_custom_variables()["corr_method"]
vector_col = "corr_features"

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
corr_method

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# convert to vector column first
assembler = VectorAssembler(inputCols=fitness_df.columns, outputCol=vector_col)
df_vector = assembler.transform(fitness_df).select(vector_col)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
matrix = Correlation.corr(df_vector, vector_col, method=corr_method)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
type(matrix)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
matrix.show(truncate=False)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
cor_np = matrix.collect()[0]["pearson({})".format(vector_col)].values
cor_np

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
type(cor_np)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dim = int(math.sqrt(len(cor_np)))
cor_mat = cor_np.reshape((dim,dim))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
cor_mat

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Approach 1. - Failed
df_spark = sqlContext.createDataFrame(pd.DataFrame(cor_mat))
df_spark.show()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Approach 2. - Failed
corr_data= pd.DataFrame(cor_mat, index= column_names,columns = column_names).reset_index()
corr_pyspark_df = spark.createDataFrame(corr_data)
corr_pyspark_df.show()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
corr_pyspark = dataiku.Dataset("corr_pyspark")
dkuspark.write_with_schema(corr_pyspark, df_spark)