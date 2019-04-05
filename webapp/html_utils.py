import math

import pandas as pd
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dateutil.parser

# return html Table with dataframe values
def df_to_table(df):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in df.columns])] +

        # Body
        [
            html.Tr(
                [
                    html.Td(df.iloc[i][col])
                    for col in df.columns
                ]
            )
            for i in range(len(df))
        ]
    )

#returns top indicator div
def indicator(color, text, id_value):
    return html.Div(
        [
            html.P(
                text,
                className="twelve columns indicator_text"
            ),
            html.P(
                id = id_value,
                className="indicator_value"
            ),
        ],
        className="three columns indicator",
    )

def nav_link(text, url):
    return html.A(text, href=url, className="nav-link")

def nav_list_item(children, active=False):
    return html.Li(
        [
            children
        ],
        className="nav-item {0}".format("active" if active else "")
    )

def dropdown_menu(id, items, clearable=False, className="two columns"):
    return html.Div(
        dcc.Dropdown(
            id=id,
            options=[{"label": item, "value": item} for item in items],
            value=items[0],
            clearable=clearable,
        ),
        className=className,

    )

def create_chart(title, id, size = "three", height = 80, default_figure = { 'data': [], 'layout': []}):
    return html.Div(
            [
                html.H4(title, className="chart-title",style={"height": "10%", "width": "98%"}),
                dcc.Graph(
                    id=id,
                    style={"height": "{0}%".format(height), "width": "98%"},
                    config=dict(displayModeBar=False),
                    animate=True,
                    figure=default_figure
                )
            ],
            className="{0} columns chart_div".format(size)
        )
