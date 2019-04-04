import math

import pandas as pd
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dateutil.parser
from plotly import graph_objs as go

# expects a dataframe with two columns
def pie_chart(dataframe, annotation_text):

    column_values = list(dataframe.columns.values)
    labels = dataframe[column_values[0]].tolist()
    values = dataframe[column_values[1]].tolist()
    print("label: " + annotation_text)

    trace = go.Pie(
        labels=labels,
        values=values,
        hole=.5,
        marker={"colors": ["#007c1d", "#eaeaea"]},
        textinfo='none'
    )

    layout = dict(
        showlegend=False,
        margin=dict(
            l=10,
            r=10,
            t=10,
            b=10
        ),

        annotations= [
            dict(
                text=annotation_text,
                font=dict(
                    size=20
                ),
                x=0.5,
                y=0.5,
                showarrow=False
            )
        ]
    )

    return dict(data=[trace], layout=layout)
