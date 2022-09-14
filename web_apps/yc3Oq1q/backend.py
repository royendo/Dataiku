from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import column
from bokeh.io import curdoc

import dataiku

# load the dataframe from a CSV file
dataset = dataiku.Dataset("xlsx_wait")
df = dataset.get_dataframe()

# extract the columns
Date = df['SAMI']
Close = df['Poids UO']

# create the data source
source = ColumnDataSource(data=
{
    'x' : Date,
    'y' : Close
})

# called when the Select item changes in value
def update_plot(attr, old, new):
    if new == 'Close':
        # update the data source
        source.data['y'] = Close
        p.yaxis.axis_label = 'Close'



p = figure(x_axis_type='datetime') # display the x-axis as dates

p.line('x',
       'y',
       source=source)

p.title.text = 'AAPL Stock Prices'
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Close'

curdoc().add_root(p)
curdoc().title = "First Graph"