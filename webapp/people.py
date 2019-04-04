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
import db_utils
import html_utils
from app import app
from html_utils import indicator, df_to_table

indicators = html.Div(
    [
        indicator(
            "#00cc96", "Score", "score"
        ),
        html.Div(
                [
                    html.P("Leads by source"),
                    dcc.Graph(
                        id="pct_women",
                        style={"height": "90%", "width": "98%"},
                        config=dict(displayModeBar=False),
                    ),
                ],
                className="four columns chart_div"
            ),
        indicator(
            "#EF553B", "% Women Leaders", "pct_women_leader"
        ),
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

table = html.Div(
    id="employee_table",
    className="row",
    style={
        "maxHeight": "350px",
        "overflowY": "scroll",
        "padding": "8",
        "marginTop": "5",
        "backgroundColor":"white",
        "border": "1px solid #C8D4E3",
        "borderRadius": "3px"
    }
)

layout = [
    indicators,
    table
]

@app.callback(
    Output("score", "children"),
    [Input("company_selector", "value")]
)
def score_callback(company):
    return 50.00 if company == "Pinterest" else 45.00

@app.callback(
    Output("pct_women", "children"),
    [Input("company_selector", "value")]
)
def pct_women_callback(company):
    result = db_utils.get_women_pct(company)
    return result['percentage']

@app.callback(
    Output("pct_women_leader", "children"),
    [Input("company_selector", "value")]
)
def pct_women_leader_callback(company):
    return 10.00 if company == "Pinterest" else 01.00

@app.callback(
    Output("employee_table", "children"),
    [Input("company_selector", "value")]
)
def table_callback(company):
    return df_to_table(db_utils.get_all_employees_df(company))
