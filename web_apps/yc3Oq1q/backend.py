from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import column
from bokeh.io import curdoc

# load the dataframe from a CSV file
df = pd.read_csv('AAPL.csv', parse_dates=['Date'])

# extract the columns
Date = df['Date']
Close = df['Close']
AdjClose = df['Adj Close']

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
    else:
        source.data['y'] = AdjClose
        p.yaxis.axis_label = 'Adj Close'

# display a selection menu
menu = Select(options=[('Close','Close'), ('Adj Close','Adj Close')],
              value='Close',
              title = 'AAPL Stocks')

# callback when the Select menu changes its value
menu.on_change('value', update_plot)

p = figure(x_axis_type='datetime') # display the x-axis as dates

p.line('x',
       'y',
       source=source,
       color='green',
       width=3)

p.title.text = 'AAPL Stock Prices'
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Close'

curdoc().theme = 'night_sky'
curdoc().add_root(column(menu, p))
curdoc().title = "First Graph"