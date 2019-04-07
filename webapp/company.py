import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_dangerously_set_inner_html
from dash.dependencies import Input, Output
from app import app
import pandas as pd

import db_utils
from html_utils import create_chart
from chart_utils import bar_chart, stacked_bar_chart

layout = [ html.Div([ html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='My Company', value='tab-1', id="company_name"),
        dcc.Tab(label='Leaderboard', value='tab-2')
    ], className="row"),
    html.Div(id='tabs-content')
    ])
])]

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

@app.callback([Output('tabs-content', 'children'), Output("company_scores", "company"), Output("leaderboard", "company")],
              [Input('tabs', 'value'), Input("company_selector", "value")])
def render_content(tab, company):
    content = []
    if tab == 'tab-1':
        content = [
            html.Div(
                [
                 create_chart("{0} Scores".format(company), "company_scores", size = "twelve", height = 80, width = 98, title_position="top")
                 ],
                 className="row"
            )
        ]
    elif tab == 'tab-2':
        content = html.Div(
            [
             create_chart("Leaderboard", "leaderboard", size = "twelve", height = 80, title_position="top")
             ],
             className="row"
        )
    return content, company, company

@app.callback(
    Output("company_scores", "figure"),
    [Input("company_scores", "company")]
)
def company_scores_callback(company):
    dataframe = db_utils.get_company_scores(company)
    dataframe = dataframe.select_dtypes(['number'])
    my_company_description = "{0} Scores".format(company)
    colors = ["#593196"]
    label_overrides = ['Maternity Weeks Score', 'Paternity Weeks Score', 'Lactation Room Score', 'Expectant Mother Parking Spot Score', 'Gender Neutral Bathroom Score', 'Feminine Products Score']
    return bar_chart(dataframe, colors, my_company_description, label_overrides)

@app.callback(
    Output("leaderboard", "figure"),
    [Input("leaderboard", "company")]
)
def leaderboard_callback(company):
    dataframe = db_utils.get_company_scores(limit = 20)
    dataframe.drop('score', axis=1, inplace=True)
    # only works because first column is company name
    label_overrides = [company.replace("_"," ") for company in dataframe[dataframe.columns[0]].tolist()]
    # https://pinetools.com/gradient-generator
    colors = ["#593196", "#724cab", "#8b68c0", "#a483d5", "#bd9fea", "#d6bbff"]
    my_company_description = "Hermione Score Leaderboard"
    return stacked_bar_chart(dataframe, colors, my_company_description, label_overrides = label_overrides)

@app.callback(
    Output("company_name", "label"),
    [Input("company_selector", "value")]
)
def company_name_callback(company):
    return company
