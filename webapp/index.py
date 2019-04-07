import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_dangerously_set_inner_html

from app import app
import people
import company
import html_utils

app.css.config.serve_locally = True
app.scripts.config.serve_locally = False


#### NOTE: THIS IS NOT IN USE JUST HERE AS REFERENCE - MODIFY DASH_NAVBAR INSTEAD ####
navbar = html.Div([dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <img src='assets/hermione2.png') }}" height="2.5%" width="2.5%"></img>
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
#### NOTE: THIS IS NOT IN USE JUST HERE AS REFERENCE - MODIFY DASH_NAVBAR INSTEAD ####


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
            className="navbar navbar-expand-lg navbar-light bg-light"
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

dropdownMenus = html.Div(
    [
        html_utils.dropdown_menu("company_selector", ["Google", "Pinterest"]),
        html_utils.dropdown_menu("title_selector", ["All", "Software Engineer 1", "Software Engineer 4", "Manager"])
    ],
    className="row",
    style={"marginBottom": "10"}
)

body = html.Div(
    [
        dropdownTitles,
        dropdownMenus,
        html.Span([dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''<form class="form-inline my-2 my-lg-0">
        <a class="btn btn-secondary my-2 my-sm-0" style="display:inline-block" data-toggle="modal" data-target="#myModal">Report Disease</a>
      </form>
    <div class="modal" id="myModal">
    <div class="modal-dialog" style="width:1250px;">
      <div class="modal-content">

        <!-- Modal Header -->
        <div class="modal-header">
          <h4 class="modal-title">Report</h4>
          <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>

        <!-- Modal body -->
        <div class="modal-body modal-body-1">
          <form>
            <fieldset>
              <div class="form-group">
                <label>Company Name</label>
                <input type="text" class="form-control" id="modal_company_name" placeholder="Enter the company name" required>
              </div>
              <div class="form-group">
                <label>Number of Women in Tech</label>
                 <input type="text" class="form-control" id="modal_number_women" placeholder="Enter the number of women in tech" required>
              </div>
              <div class="form-group">
                <label>Age</label>
                <input type="text" class="form-control" id="age" placeholder="Enter the age of the patient">
              </div>
              <div class="form-group">
                <label>Hospital Location</label>
                <small id="hospitalHelp" class="form-text text-muted">Select the gender of the patient</small>
                <select class="custom-select" aria-describedby="hospitalHelp">
                  <option value="smmc" selected="">Saint Mary's Medical Center</option>
                  <option value="schc">Stanford Children's Health Center</option>
                </select>
              </div>

              <div class="form-group">
                <label>Date of first Symptoms</label>
                <input type="text" id="datepicker" placeholder="Date" required>
              </div>

              <div class="form-group">
                <div class="custom-control custom-switch">
                  <input type="checkbox" class="custom-control-input" id="customSwitch1">
                  <label class="custom-control-label" for="customSwitch1">Submit to CDC</label>
                </div>
              </div>
            </fieldset>
          </form>
        </div>
         <!-- Modal footer -->
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" id="hack-next">Next</button>
          <button type="button" class="btn btn-primary collapse" id="modal-close-button" data-dismiss="modal">Close</button>
        </div>

      </div>
    </div>
  </div>''')]),
        html.Div(id="people_row", children=people.layout, style={"marginBottom": "10"}),
        html.Div(id="company_row", children=company.layout)
    ],
    style={
        "margin": "2%"
    }
)

app.layout = html.Div(
    [
        dash_navbar,
        body
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
