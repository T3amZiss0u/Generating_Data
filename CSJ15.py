# CSJ 15-1 Simple Bar Graph
from plotly.graph_objs import Bar, Layout
from plotly import offline


# From CSJ 6-1 Annual Incidents of US Police Killings
killings_by_year = {
    2013: 1106,
    2014: 1050,
    2015: 1103,
    2016: 1071,
    2017: 1095,
    2018: 1143,
    2019: 1098,
    }
year = []
killings = []

for key, value in killings_by_year.items():
    year.append(key)
    killings.append(value)

data = [Bar(x=year, y=killings)]

x_axis_config = {'title': 'year', 'dtick': 1}
y_axis_config = {'title': 'Number of Police Killings'}
my_layout = Layout(title='US Police Killings by year',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='killings.html')
