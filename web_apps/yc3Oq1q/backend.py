from bokeh.io import curdoc
from bokeh.plotting import figure

#Import data
import dataiku
dataset = dataiku.Dataset("xlsx")
df = dataset.get_dataframe()

x = df['S']
y = df['SAMI'
      
p = figure()
p.line(x=x, y=y)]