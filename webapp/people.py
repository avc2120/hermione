import json
import math as Math

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
import data_fabricator
import base64
from app import app
from html_utils import indicator, df_to_table, create_chart
from chart_utils import donut_chart
import random

charts = html.Div(
    [
        html.Div(
            [
                html.Div("0", id="score", className="score_number"),
                html.Div(
                    [
                        html.Img(src='assets/certified.png', className="certification_image")
                    ],
                    className="overlay_image"
                )
            ],
            #html.H3("Gold Certified", style={"color":"white", "text-align":"center"})],
            className="three columns overlay_container",
            style={"backgroundColor": "#593196"}),
        create_chart("Overall Score", "score_pie"),
        create_chart("% Women", "pct_women_pie"),
        # create_chart("% Average Salary", "pct_avg_salary"),
        create_chart("% Women in Leadership", "pct_women_leader_pie"),
    ],
    className="row",
)

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
    charts
]

# add_company(name, maternity_weeks, paternity_weeks, lactation_rooms, mother_parking, gender_neutral_bathrooms, feminine_products, score)


@app.callback(Output("placeholder-list","children"),
    [Input("save-data","n_clicks")],
    [State("wit_company", "value"),
    State("wit", "value"),
    State("mit", "value"),
    State("wit_lead", "value"),
    State("mit_lead", "value"),
    State("maternity_weeks", "value"),
    State("paternity_weeks", "value")]
    )
def save_data(n_clicks, wit_company, wit, mit, wit_leadership, mit_leadership, maternity_weeks, paternity_weeks):
    if (wit and wit_company and mit and wit_leadership and mit_leadership):
        print('writing new company')
        data_fabricator.populate_employee_db(int(wit), "Software Engineer 1", 125000, 200000, 1, 5, "Female", wit_company, leadership = False)
        data_fabricator.populate_employee_db(int(mit), "Software Engineer 1", 125000, 200000, 1, 5, "Male", wit_company, leadership = False)
        data_fabricator.populate_employee_db(int(wit), "Software Engineer 4", 165000, 240000, 1, 5, "Female", wit_company, leadership = False)
        data_fabricator.populate_employee_db(int(mit), "Software Engineer 4", 165000, 240000, 1, 5, "Male", wit_company, leadership = False)
        data_fabricator.populate_employee_db(int(wit_leadership), "Manager", 225000, 400000, 5, 10, "Female", wit_company, leadership = True)
        data_fabricator.populate_employee_db(int(mit_leadership), "Manager", 225000, 500000, 5, 10, "Male", wit_company, leadership = True)
    if (wit_company and maternity_weeks and paternity_weeks):
        db_utils.add_company(wit_company, maternity_weeks, paternity_weeks, 5, 10, 4, 10, 52)

@app.callback(Output("positions-list", "children"),
    [Input("add-position-salary","n_clicks")],
    [State("positions-list", "children")]
    )
def add_position(n_clicks, children):
    if n_clicks != None and n_clicks > 0:
        if not children:
            return html_utils.salary("Software Engineer")
        else:
            return html.Div([
                children,
                html_utils.salary("Software Engineer")])

@app.callback(
    Output("score", "children"),
    [Input("company_selector", "value")]
)
def score_callback(company):
    result = {'Google': 95.00, 'Pinterest': 52.00}
    if company in result:
        return result[company]
    else:
        return random.randint(0,100)

@app.callback(
    Output("company_selector", "options"),
    [Input('save-data', 'n_clicks')])
def get_companies(options):
    print('in here alice')
    return [{'label': i, 'value': i} for i in db_utils.get_companies()]

@app.callback(
    Output("pct_women_label", "children"),
    [Input("company_selector", "value"), Input("title_selector", "value")]
)
def pct_women_callback(company, title):
    result = db_utils.get_women_pct(company, title)
    return "{0}%".format(round(result['percentage']))

@app.callback(
    Output("pct_women_leader", "children"),
    [Input("company_selector", "value")]
)
def pct_women_leader_callback(company):
    return 10.00 if company == "Pinterest" else 01.00

@app.callback(
    Output("pct_women_pie", "figure"),
    [Input("company_selector", "value"), Input("title_selector", "value")]
)
def pct_women_pie_callback(company, title):
    percentage_label = "{0}%".format(round(db_utils.get_women_pct(company, title)['percentage']))
    colors = ["#593196", "#eaeaea"]
    return donut_chart(db_utils.get_women_pct_df(company, title), colors, percentage_label)

@app.callback(
    Output("pct_women_leader_pie", "figure"),
    [Input("company_selector", "value")]
)
def pct_women_leader_pie_callback(company):
    dataframe = db_utils.get_women_pct_df(company, leadership = True)
    # this is hardcoded because female is always the first row
    female_count = dataframe.at[0, 'total']
    male_count = dataframe.at[1, 'total']
    percentage_label = "{0}%".format(round(female_count/(female_count + male_count) * 100))
    colors = ["#593196", "#eaeaea"]
    return donut_chart(dataframe, colors, percentage_label)

@app.callback(
    Output("score_pie", "figure"),
    [Input("company_selector", "value")]
)
def score_pie_callback(company):
    scores = {"Pinterest": 95, "Google": 52}
    if company in scores:
        score = scores.get(company)
    else:
        score = random.randint(0,100)
    data = [["score", score], ["not_score", (100 - score)]]
    dataframe = pd.DataFrame(data, columns = ["Label", "Score"])
    percentage_label = "{0}".format(score)
    colors = ["#593196", "#eaeaea"]
    return donut_chart(dataframe, colors, percentage_label)


@app.callback(
    Output("employee_table", "children"),
    [Input("company_selector", "value")]
)
def table_callback(company):
    return df_to_table(db_utils.get_all_employees_df(company))
