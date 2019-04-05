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

def create_chart(title, id):
    return html.Div(
            [
                html.P(title),
                dcc.Graph(
                    id=id,
                    style={"height": "90%", "width": "98%"},
                    config=dict(displayModeBar=False),
                    animate=True
                )
            ],
            className="three columns chart_div"
        )
