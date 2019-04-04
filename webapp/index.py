import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
import people


##########
# LAYOUT #
##########
# app.layout = html.Div(children=[
#     html.H1(children='Hermione Dashboard', style={
#         'textAlign': 'center',
#     })
# ])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("About", href="#")),
        dbc.NavItem(dbc.NavLink("Pricing", href="#")),
        dcc.Dropdown(
            id="company_selector",
            options=[
                {
                    "label": "Google",
                    "value": "Google"},
                {
                    "label": "Pinterest",
                    "value": "Pinterest",
                },
                {
                    "label": "All",
                    "value": "All",
                },
            ],
            value="Google",
        ),
    ],
    brand="Project Hermione",
    brand_href="#",
    sticky="top",
)

body = html.Div(
    [
        html.Div(id="people_row"),
        html.Div(id="company_row"),

    ]
)

app.layout = html.Div(
    [
        navbar,
        body,
        html.Link(href="https://use.fontawesome.com/releases/v5.2.0/css/all.css",rel="stylesheet"),
        html.Link(href="https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css",rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
        html.Link(href="https://cdn.rawgit.com/amadoukane96/8a8cfdac5d2cecad866952c52a70a50e/raw/cd5a9bf0b30856f4fc7e3812162c74bfc0ebe011/dash_crm.css", rel="stylesheet")
    ]
)

@app.callback(
    Output("people_row", "children"),
    [Input("company_selector", "value")]
)
def render_people(company):
    return people.layout

@app.callback(
    Output("company_row", "children"),
    [Input("company_selector", "value")]
)
def render_company(company):
    return people.layout


if __name__ == "__main__":
    app.run_server(debug=True)
