from bokeh.io import curdoc
#Import data
import dataiku
dataset = dataiku.Dataset("xlsx")
df = dataset.get_dataframe()