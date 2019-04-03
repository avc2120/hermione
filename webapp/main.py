from flask import Flask, request, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.run(debug=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import db_utils, data_fabricator

db_utils.create_all_tables()
data_fabricator.populate_db()

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/all_companies')
def get_all_companies():
    return jsonify([company.to_dict() for company in db_utils.get_all_companies()])

@app.route('/all_employees')
def get_all_employees():
    return jsonify([employee.to_dict() for employee in db_utils.get_all_employees()])

@app.route('/women_pct')
def get_women_pct():
    company = request.args.get('company')
    return jsonify(db_utils.get_women_pct(company))
