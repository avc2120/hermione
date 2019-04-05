import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_dangerously_set_inner_html
from dash.dependencies import Input, Output
from app import app
import pandas as pd

layout = [ html.Div([ html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='My Company', value='tab-1'),
        dcc.Tab(label='Leaderboard', value='tab-2'),
        dcc.Tab(label='Action Items', value='tab-3'),
    ]),
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
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div(children=[
             html.P(["hello this is test "], id='hello', style={'background-color': 'white'}),
             html.Div(
                [
                    dcc.Graph(
                        id="chalice",
                        style={"height": "100%", "width": "480%"},
                        config=dict(displayModeBar=False),
                        animate=True
                    ),
                    html.P(id="my_company_description", style={"fontSize": 40})
                ],
                className="three columns chart_div",
                id="my_company_graph"
            )
        ])
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
    Output("chalice", "figure"),
    [Input("company_selector", "value"), Input("title_selector", "value")]
)
def pct_women_pie_callback(company, title):
    my_company_description = "This is the description"
    colors = ["#007c1d", "#eaeaea"]
    return pie_chart(db_utils.get_women_pct_df(company, title), colors, my_company_description)
