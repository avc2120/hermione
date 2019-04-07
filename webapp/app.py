from flask import Flask, request, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import dash
import plotly.graph_objs as go
import json
import dash_bootstrap_components as dbc
import dash_html_components as html


external_scripts = [
    {'src': 'https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'},
    {'src': 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js'},
    {'src': 'https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js'}
]

external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/flatly/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-T5jhQKMh96HMkXwqVMSjF3CmLcL1nT9//tCqu9By5XSdj7CwR0r+F3LTzUdfkkQf',
        'crossorigin': 'anonymous'
    }
]

server = Flask(__name__)
# https://github.com/facultyai/dash-bootstrap-components/blob/master/dash_bootstrap_components/themes.py
app = dash.Dash(__name__, server=server, external_scripts=external_scripts, external_stylesheets=[dbc.themes.PULSE])
app.config.suppress_callback_exceptions = True
app.title = "Project Hermione"
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"


db = SQLAlchemy(server)

import db_utils, data_fabricator

db_utils.create_all_tables()
data_fabricator.populate_db()

@server.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@server.route('/all_companies')
def get_all_companies():
    return jsonify([company.to_dict() for company in db_utils.get_all_companies()])

@server.route('/all_companies_df')
def get_all_companies_df():
    return db_utils.get_all_companies_df()

@server.route('/all_employees')
def get_all_employees():
    return jsonify([employee.to_dict() for employee in db_utils.get_all_employees()])

@server.route('/women_pct')
def get_women_pct():
    company = request.args.get('company')
    return jsonify(db_utils.get_women_pct(company))
