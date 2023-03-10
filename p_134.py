# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 10:05:15 2023

@author: xxu
"""
#Import the required packages
from bokeh.layouts import widgetbox
from bokeh.models import Slider
from bokeh.io import curdoc
#Create a slider widget
slider_widget = Slider(start = 0, end = 100, step = 10, title = 'Single Slider')
#Create a layout for the widget
slider_layout = widgetbox(slider_widget)
#Add the slider widget to the application
curdoc().add_root(slider_layout)