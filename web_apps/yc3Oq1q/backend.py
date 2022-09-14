from bokeh.io import curdoc
#Import data
import dataiku
dataset = dataiku.Dataset("dnb_api_prepared")
df = dataset.get_dataframe()