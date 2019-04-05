import math

import pandas as pd
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dateutil.parser
from plotly import graph_objs as go

# expects a dataframe with two columns
def pie_chart(dataframe, colors, title):

    column_values = list(dataframe.columns.values)
    labels = dataframe[column_values[0]].tolist()
    values = dataframe[column_values[1]].tolist()

    trace = go.Pie(
        labels=labels,
        values=values,
        hole=.5,
        marker={"colors": colors},
        title= {
            "text": title,
            "font": {
                "size": 50
            }
        },
        textinfo="none"
    )

    layout = dict(
        sort=True,
        showlegend=False,
        margin=dict(
            l=10,
            r=10,
            t=0,
            b=0
        ),
    )

    return dict(data=[trace], layout=layout)
