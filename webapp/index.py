import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_dangerously_set_inner_html

from app import app
import people
import company

navbar = html.Div([dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <img src='hermione2.png') }}" height="38" width="34"></img>
    <a class="navbar-brand" href="#">&nbsp;&nbsp;Project Hermione</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarColor01">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">About</a>
        </li>
      </ul>
    </div>
  </nav>''')])

dropdownTitles = html.Div(
    [
        html.Div("Company", className="two columns"),
        html.Div("Title", className="two columns")
    ],
    className="row"
)
dropdownMenus = html.Div(
    [
        html.Div(
            dcc.Dropdown(
                id="company_selector",
                options=[
                    {
                        "label": "Google",
                        "value": "Google"},
                    {
                        "label": "Pinterest",
                        "value": "Pinterest",
                    }
                ],
                value="Google",
                clearable=False

            ),
            className="two columns",

        ),
        html.Div(
            dcc.Dropdown(
                id="title_selector",
                options=[
                    {
                        "label": "Software Engineer 1",
                        "value": "Software Engineer 1"
                    },
                    {
                        "label": "Software Engineer 4",
                        "value": "Software Engineer 4",
                    },
                    {
                        "label": "Leadership",
                        "value": "Manager"
                    },
                    {
                        "label": "All",
                        "value": "All",
                    },
                ],
                value="All",
                clearable=False
            ),
            className="two columns",

        ),
    ],
    className="row",
    style={"marginBottom": "10"}
)

body = html.Div(
    [
        dropdownTitles,
        dropdownMenus,
        html.Div(id="people_row", children=people.layout, style={"marginBottom": "10"}),
        html.Div(id="company_row", children=company.layout),
    ],
    style={
        "margin": "2%"
    }
)


app.layout = html.Div(
    [
        # html.Link(href="https://use.fontawesome.com/releases/v5.2.0/css/all.css",rel="stylesheet"),
        # this is the charting css one from the dash example
        html.Link(href="https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css",rel="stylesheet"),
        html.Link(href="https://cdn.rawgit.com/amadoukane96/8a8cfdac5d2cecad866952c52a70a50e/raw/cd5a9bf0b30856f4fc7e3812162c74bfc0ebe011/dash_crm.css", rel="stylesheet"),
        # html.Link(href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"),
        # html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
        # html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
        # html.Link(href="https://codepen.io/chriddyp/pen/bWLwgP.css", rel="stylesheet"),
        html.Link(href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"),
        html.Link(href="https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/flatly/bootstrap.min.css", rel="stylesheet"),
        navbar,
        body
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
