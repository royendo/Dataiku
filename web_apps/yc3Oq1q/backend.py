from bokeh.io import curdoc
from bokeh.plotting import figure, show, output_file

#Import data
import dataiku
dataset = dataiku.Dataset("xlsx")
df = dataset.get_dataframe()

x = df['S']
y = df['SAMI']
print(x)
print(y)
p = figure(width=300, height=300)
p.line(x=x, y=y)
output_file("foo.html")

show(p)