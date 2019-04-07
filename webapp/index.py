import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_dangerously_set_inner_html

from app import app
import people
import company
import html_utils
from html_utils import salary
import db_utils

# app.css.config.serve_locally = True
# app.scripts.config.serve_locally = False
# this is a copy of the above HTML
dash_navbar = html.Div(
    [
        html.Nav(
            [
                html.Img(src="assets/hermione2.png", height="2.5%", width="2.5%"),
                html.A("Project Hermione", href="#", className="navbar-brand", style={'padding': 10}),
                html.Button(
                    [
                        html.Span(className="navbar-toggler-icon")
                    ],
                    className="navbar-toggler",
                    type="button",
                    # this is how you add the wildcard data and aria attributes
                    **{
                        "data-toggle" : "collapse",
                        "data-target" : "#navbarColor01",
                        "aria-controls" : "navbarColor01",
                        "aria-expanded" : "false",
                        "aria-label" : "Toggle navigation"
                    }
                ),
                html.Div(
                    [
                        html.Ul(
                            [
                                html_utils.nav_list_item(html_utils.nav_link("Dashboard", "#"), active = True),
                                html_utils.nav_list_item(html_utils.nav_link("About", "#")),
                                html_utils.nav_list_item(html_utils.nav_link("Mission Statement", "#"))
                            ],
                            className="navbar-nav mr-auto"
                        )
                    ],
                    className="collapse navbar-collapse",
                    id="navbarColor01"
                )
            ],
            className="navbar navbar-expand-lg navbar-dark bg-primary"
        )
    ]
)

dropdownTitles = html.Div(
    [
        html.Div("Company", className="two columns"),
        html.Div("Title", className="two columns")
    ],
    className="row"
)

dropdownMenus = html.Div([
    html.Div(
        dcc.Dropdown(
            id="company_selector",
             options=[{'label': i, 'value': i} for i in db_utils.get_companies()],
            value=db_utils.get_companies()[0],
            clearable=False,
        ), className="two columns"),
        html_utils.dropdown_menu("title_selector", ["All", "Software Engineer 1", "Software Engineer 4", "Manager"])
    ],
    className="row",
    style={"marginBottom": "10"}
)

modal = html.Div([
  html.Div([
    html.Div([
      html.Div([
        html.H4("Report", className="modal-title"),
        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''<button type="button" class="close" data-dismiss="modal">&times;</button>''')
        ], className="modal-header"),
      html.Div([
        html.Form([
          html.Fieldset([
            html_utils.form_group("Company Name", "Enter Company Name", "wit_company"),
            html_utils.form_group("Number of Women in Tech", "Enter Number of Women in Tech", "wit"),
            html_utils.form_group("Number of Men in Tech", "Enter Number of Men in Tech", "mit"),
            html_utils.form_group("Number of Women in Tech Leadership", "Enter Number of Women in Tech Leadership", "wit_lead"),
            html_utils.form_group("Number of Men in Tech Leadership", "Enter Number of Men in Tech Leadership", "mit_lead"),
            html_utils.upload(),
            html.Div([], id="positions-list"),
            # html.Button("Add Position Salary", className="btn btn-outline-primary", id="add-position")
            ], id="hermione-fieldset")
          ])
        ], className="modal-body"),
      html.Div([
        html.Div([], id="placeholder-list"),
        html.Button("Add Position Salary", className="btn btn-primary", id="add-position-salary"),
        html.Button("Save", className="btn btn-secondary", **{"data-dismiss":"modal"}, id="save-data")
        # dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''<button id="save-data" type="button" class="btn btn-secondary" data-dismiss="modal">Save</button>''')
        ], className="modal-footer")
      ], className="modal-content")
    ],className="modal-dialog", style={"width": "1250px"})
  ],className="modal", id="myModal")

body = html.Div(
    [
        dropdownTitles,
        dropdownMenus,
        html.Span([dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''<form class="form-inline my-2 my-lg-0 report-statistics">
        <a class="btn btn-secondary my-2 my-sm-0" style="display:inline-block" data-toggle="modal" data-target="#myModal">Report Statistics</a>
      </form>''')]),
        modal,
        html.Div(id="people_row", children=people.layout, style={"marginBottom": "10"}),
        html.Div(id="company_row", children=company.layout)
    ],
    style={
        "margin": "2%", "margin-left":"100px"
    },
    className="hermione-body"
)

layout = html.Div(
    [
        dash_navbar,
        body
    ]
)

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True)
