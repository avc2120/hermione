import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output
from app import app

layout = [ html.Div([ html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='My Company', value='tab-1'),
        dcc.Tab(label='Leaderboard', value='tab-2'),
        dcc.Tab(label='Action Items', value='tab-3'),
    ]),
    html.Div(id='tabs-content')
    ])
])]

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
        ])