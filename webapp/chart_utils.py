import math

import pandas as pd
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dateutil.parser

def pie_chart(dataframe):
    labels = []
    values = []

    # compute % for each leadsource type
    for case_type in types:
        nb_type = df[df["LeadSource"] == case_type].shape[0]
        values.append(nb_type / nb_leads * 100)

    trace = go.Pie(
        labels=types,
        values=values,
        marker={"colors": ["#264e86", "#0074e4", "#74dbef", "#eff0f4"]},
    )

    layout = dict(margin=dict(l=15, r=10, t=0, b=65), legend=dict(orientation="h"))
    return dict(data=[trace], layout=layout)
