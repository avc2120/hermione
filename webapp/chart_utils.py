import math

import pandas as pd
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dateutil.parser
from plotly import graph_objs as go

# expects a dataframe with two columns
def donut_chart(dataframe, colors, title):

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
        textinfo="none",
        hoverinfo="value",
        direction="counterclockwise",
        sort=False
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

# expects a dataframe with only one row
def bar_chart(dataframe, colors, title, label_overrides = []):
    if len(dataframe.values) == 0:
        return {"data": [], "layout": []}
    column_values = label_overrides if len(label_overrides) != 0 else list(dataframe.columns.values)
    values = dataframe.values.tolist()[0]
    trace = go.Bar(
        x=column_values,
        y=values,
        marker = {"color": colors[0]}
    )

    layout = dict(
        showlegend=False,
        margin=dict(
            l=25,
            r=5,
            t=5,
            b=35
        ),
        animate=True
    )

    return dict(data=[trace], layout=layout)

# expects x dimension as first column
def stacked_bar_chart(dataframe, colors, title, label_overrides = []):
    if len(dataframe.values) == 0:
        return {"data": [], "layout": []}
    labels = label_overrides if len(label_overrides) != 0 else dataframe[dataframe.columns[0]].tolist()
    dataframe.drop(dataframe.columns[0], axis=1, inplace=True)
    traces = [
        go.Bar(
            x=labels,
            y=dataframe[column].tolist(),
            name=column.replace("_", " ").title() + " Score",
            marker = {"color": colors[index]}) for index,column in enumerate(dataframe.columns)
    ]

    data = traces

    layout = go.Layout(
        barmode='stack',
        margin=dict(
            l=25,
            r=5,
            t=5,
            b=65
        ),
    )

    return dict(data=traces, layout=layout)
