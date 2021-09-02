# -*- coding: utf-8 -*-
import dataiku
from dataiku import spark as dkuspark
from pyspark import SparkContext
from pyspark.sql import SQLContext
import time

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)
time.sleep(3000)

# Read recipe inputs
corona1_prepared = dataiku.Dataset("Corona1_prepared")
corona1_prepared_df = dkuspark.get_dataframe(sqlContext, corona1_prepared)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a SparkSQL dataframe
pusparksleep_df = corona1_prepared_df # For this sample code, simply copy input to output

# Write recipe outputs
pusparksleep = dataiku.Dataset("pusparksleep")
dkuspark.write_with_schema(pusparksleep, pusparksleep_df)
