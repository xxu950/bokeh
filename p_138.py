# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 10:17:58 2023

@author: xxu
"""
#Import the required packages
from bokeh.models import Slider, ColumnDataSource
from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.plotting import figure
from numpy.random import random
#Create data for the plot
initial_points = 500
data_points = ColumnDataSource(data = {'x': random(initial_points), 'y':
random(initial_points)})
#Create the plot
plot = figure(title = "Random scatter plot generator")
plot.diamond(x = 'x', y = 'y', source = data_points, color = 'red')
#Create the slider widget
slider_widget = Slider(start = 0, end = 10000, step = 10, value = initial_points,
title = 'Slide right to increase number of points')
#Define the callback function
def callback(attr, old, new):
    points = slider_widget.value
    data_points.data = {'x': random(points), 'y': random(points)}
slider_widget.on_change('value', callback)
#Create a layout for the application
layout = row(slider_widget, plot)
#Add the layout to the application
curdoc().add_root(layout)