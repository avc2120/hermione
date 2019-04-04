import json
import math

import pandas as pd
import flask
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.plotly as py
from plotly import graph_objs as go
import html_utils
from app import app, indicator

dropdownMenu = html.Div(
    dbc.DropdownMenu(
        nav=True,
        in_navbar=True,
        label="Menu",
        children=[
            dbc.DropdownMenuItem("Google"),
            dbc.DropdownMenuItem("Pinterest"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("All"),
        ],
    ),
)

indicators = html.Div(
    [
        indicator(
            "#00cc96", "Score", "score"
        ),
        indicator(
            "#119DFF", "% Women", "pct_women"
        ),
        indicator(
            "#EF553B", "% Women - Leadership", "pct_women_leader",
        ),
        indicator(
            "#EF553B", "% Women New Hire", "pct_women_new"
        )
    ],
    className="row",
)

# charts = html.Div(
#     [
#         html.Div(
#             [
#                 html.P("Leads count per state" ),
#                 dcc.Graph(
#                     id="map",
#                     style={"height": "90%", "width": "98%"},
#                     config=dict(displayModeBar=False),
#                 ),
#             ],
#             className="four columns chart_div"
#         ),
#
#         html.Div(
#             [
#                 html.P("Leads by source"),
#                 dcc.Graph(
#                     id="lead_source",
#                     style={"height": "90%", "width": "98%"},
#                     config=dict(displayModeBar=False),
#                 ),
#             ],
#             className="four columns chart_div"
#         ),
#
#         html.Div(
#             [
#                 html.P("Converted Leads count"),
#                 dcc.Graph(
#                     id="converted_leads",
#                     style={"height": "90%", "width": "98%"},
#                     config=dict(displayModeBar=False),
#                 ),
#             ],
#             className="four columns chart_div"
#         ),
#     ],
#     className="row",
#     style={"marginTop": "5"},
# )
#
# table = html.Div(
#     id="leads_table",
#     className="row",
#     style={
#         "maxHeight": "350px",
#         "overflowY": "scroll",
#         "padding": "8",
#         "marginTop": "5",
#         "backgroundColor":"white",
#         "border": "1px solid #C8D4E3",
#         "borderRadius": "3px"
#     },
# )

layout = [
    dropdownMenu,
    indicators
]

# updates left indicator based on df updates
@app.callback(
    Output("score", "children")
)
def left_leads_indicator_callback():
    return 50.00
