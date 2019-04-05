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
        dcc.Tab(label='Leaderboard', value='tab-2'),
        dcc.Tab(label='Action Items', value='tab-3'),
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

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value'), Input("company_selector", "value")])
def render_content(tab, company):
    if tab == 'tab-1':
        return html.Div(
            [
             create_chart("{0} Scores".format(company), "company_scores", size = "twelve", height = 100)
             ],
             className="row"
        )
    elif tab == 'tab-2':
        return html.Div(
            [
             create_chart("Leaderboard", "leaderboard", size = "twelve", height = 100)
             ],
             className="row"
        )
    elif tab == 'tab-3':
        return html.Div([
             dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
        <h2>Example body text</h2>
<p>Nullam quis risus eget <a href="#">urna mollis ornare</a> vel eu leo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nullam id dolor id nibh ultricies vehicula.</p>
<p><small>This line of text is meant to be treated as fine print.</small></p>
<p>The following snippet of text is <strong>rendered as bold text</strong>.</p>
<p>The following snippet of text is <em>rendered as italicized text</em>.</p>
<p>An abbreviation of the word attribute is <abbr title="attribute">attr</abbr>.</p>
<div class="progress">
  <div class="progress-bar" style="width: 60%;"></div>
</div>
    ''')
        ])

@app.callback(
    Output("company_scores", "figure"),
    [Input("company_selector", "value"), Input('tabs-content', 'children')]
)
def company_scores_callback(company, tab):
    dataframe = db_utils.get_company_scores(company)
    dataframe = dataframe.select_dtypes(['number'])
    dataframe = dataframe.drop('score', axis=1)
    print(dataframe)
    my_company_description = "{0} Scores".format(company)
    colors = ["#007c1d", "#eaeaea"]
    label_overrides = ['Maternity Weeks Score', 'Paternity Weeks Score', 'Lactation Room Score', 'Expectant Mother Parking Spot Score', 'Gender Neutral Bathroom Score', 'Feminine Products Score']
    return bar_chart(dataframe, colors, my_company_description, label_overrides)

@app.callback(
    Output("leaderboard", "figure"),
    [Input("company_selector", "value")]
)
def leaderboard_callback(company):
    print("well hello")
    dataframe = db_utils.get_company_scores()
    print(dataframe)
    my_company_description = "Hermione Score Leaderboard"
    colors = ["#007c1d", "#eaeaea"]
    return stacked_bar_chart(dataframe, colors, my_company_description)

@app.callback(
    Output("company_name", "label"),
    [Input("company_selector", "value")]
)
def company_name_callback(company):
    return company
