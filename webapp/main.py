from flask import Flask, request, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import json

server = Flask(__name__)
app = dash.Dash(__name__, server=server)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(server)

import db_utils, data_fabricator

db_utils.create_all_tables()
data_fabricator.populate_db()

##########
# LAYOUT #
##########
app.layout = html.Div(children=[
    html.H1(children='Hermione Dashboard', style={
        'textAlign': 'center',
    })
])


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
