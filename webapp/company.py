import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_dangerously_set_inner_html
from dash.dependencies import Input, Output
from app import app
import pandas as pd

import db_utils
from html_utils import create_chart
from chart_utils import bar_chart

layout = [ html.Div([ html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='My Company', value='tab-1', id="company_name"),
        dcc.Tab(label='Leaderboard', value='tab-2'),
        dcc.Tab(label='Action Items', value='tab-3'),
    ], className="row"),
    html.Div(id='tabs-content')
    ])
])]

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')


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
        return html.Div([
            html.Div(children=[
            html.H4(children='US Agriculture Exports (2011)'),
            generate_table(df)
        ])

        ])
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
    [Input("company_selector", "value")]
)
def company_scores_callback(company):
    dataframe = db_utils.get_company_scores(company)
    dataframe = dataframe.select_dtypes(['number'])
    dataframe = dataframe.drop('score', axis=1)
    my_company_description = "{0} Scores".format(company)
    colors = ["#007c1d", "#eaeaea"]
    label_overrides = ['Maternity Weeks Score', 'Paternity Weeks Score', 'Lactation Room Score', 'Expectant Mother Parking Spot Score', 'Gender Neutral Bathroom Score', 'Feminine Products Score']
    print(dataframe)
    return bar_chart(dataframe, colors, my_company_description, label_overrides)

@app.callback(
    Output("company_name", "label"),
    [Input("company_selector", "value")]
)
def company_name_callback(company):
    return company
