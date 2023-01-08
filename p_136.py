# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 10:15:45 2023

@author: xxu
"""
#Import the required packages
from bokeh.layouts import widgetbox
from bokeh.models import Slider
from bokeh.io import curdoc
#Create multiple slider widgets
slider_widget1 = Slider(start = 0, end = 100, step = 10, title = 'Slider 1')
slider_widget2 = Slider(start = 0, end = 50, step = 5, title = 'Slider 2')
slider_widget3 = Slider(start = 50, end = 100, step = 5, title = 'Slider 3')
#Create a layout for the widget
slider_layout = widgetbox(slider_widget1, slider_widget2, slider_widget3)
#Add the slider widget to the application
curdoc().add_root(slider_layout)