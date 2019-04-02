from flask import Flask, request, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import docusign_client, here_client
import json

app = Flask(__name__)
app.run(debug=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html', longitude=longitude, latitude=latitude)
