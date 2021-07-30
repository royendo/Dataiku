# -*- coding: utf-8 -*-
import dataiku
from dataiku import spark as dkuspark
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

# Read recipe inputs
fitness = dataiku.Dataset("FITNESS")
fitness_df = dkuspark.get_dataframe(sqlContext, fitness)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a SparkSQL dataframe
outputtest_df = fitness_df # For this sample code, simply copy input to output

# Write recipe outputs
outputtest = dataiku.Dataset("outputtest")
dkuspark.write_with_schema(outputtest, outputtest_df)
