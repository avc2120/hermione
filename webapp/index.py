import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from app import app, server


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
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],
    brand="Project Hermione",
    brand_href="#",
    sticky="top",
)

body = dbc.Container(
    [
        dbc.Row(
            html.Div(id="people_row", className="row", style={"margin": "2% 3%"})
        ),
        dbc.Row(
            html.Div(id="company_row", className="row", style={"margin": "2% 3%"})
        )
    ],
    className="mt-4",
)

app.layout = html.Div([navbar, body])

import people

@app.callback(Output("people_row", "children"))
def render_people():
    return people.layout

if __name__ == "__main__":
    app.run_server(debug=True)
