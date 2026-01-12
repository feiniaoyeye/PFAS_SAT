# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:13:57 2020

@author: msmsa
"""
import json
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio


def plot_sankey(data_json, fileName=None):
    with open(data_json) as json_file:
        data = json.load(json_file)

    layout = go.Layout(title_text=data['title_text'],
                       font_size=data['font_size'],
                       hoverlabel=data['hoverlabel'])
    data_ = go.Sankey(valueformat=data['valueformat'],
                      valuesuffix=data['valuesuffix'],
                      node=data['node'],
                      link=data['link'])
    fig = go.Figure(data=[data_], layout=layout)
    output_file = fileName if fileName else 'plot.html'
    pio.write_html(fig, file=output_file, auto_open=True)


class NpEncoder(json.JSONEncoder):
    # https://stackoverflow.com/a/57915246/10420147
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super().default(obj)
