import os, sys, random, json
from datetime import datetime, timedelta
from sqlalchemy import func
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Boolean
from app import db
import pandas as pd

###########
# Company #
###########

class Company(db.Model):
    __tablename__ = 'companies'
    name = Column(String(250), primary_key=True, unique=True, nullable=False)
    maternity_weeks = Column(Integer, default=0)
    paternity_weeks = Column(Integer, default=0)
    lactation_rooms = Column(Integer, default=0)
    mother_parking = Column(Integer, default=0)
    gender_neutral_bathrooms = Column(Integer, default=0)
    feminine_products = Column(Boolean, default=False)

    def to_dict(self):
        data = {}
        data['name'] = self.name
        data['maternity_weeks'] = self.maternity_weeks
        data['paternity_weeks'] = self.paternity_weeks
        data['lactation_rooms'] = self.lactation_rooms
        data['mother_parking'] = self.mother_parking
        data['gender_neutral_bathrooms'] = self.gender_neutral_bathrooms
        data['feminine_products'] = self.feminine_products
        return data

    def to_json(self):
        return json.dumps(self.to_dict())


def add_company(name, maternity_weeks, paternity_weeks, lactation_rooms, mother_parking, gender_neutral_bathrooms, feminine_products):
    company = Company(name = name, maternity_weeks = maternity_weeks, paternity_weeks = paternity_weeks, lactation_rooms = lactation_rooms, mother_parking = mother_parking, gender_neutral_bathrooms = gender_neutral_bathrooms, feminine_products = feminine_products)
    db.session.add(company)
    db.session.commit()

def get_all_companies():
    print(pd.read_sql_query(db.session.query(Company).statement, db.engine))
    return Company.query.all()

def get_all_companies_df():
    return pd.read_sql_query(db.session.query(Company).statement, db.engine)

############
# Employee #
############
class Employee(db.Model):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    title = Column(String(64))
    salary = Column(Integer)
    yoe = Column(Integer)
    gender = Column(String(15))
    company = Column(String(50))

    def to_dict(self):
        data = {}
        data['title'] = self.title
        data['salary'] = self.salary
        data['yoe'] = self.yoe
        data['gender'] = self.gender
        data['company'] = self.company
        return data

    def to_json(self):
        return json.dumps(self.to_dict())

def add_employee(title, salary, yoe, gender, company):
    employee = Employee(title = title, salary = salary, yoe = yoe, gender = gender, company = company)
    db.session.add(employee)
    db.session.commit()

def get_all_employees():
    return Employee.query.all()

def get_women_pct(company):
    result = {}
    result['female_count'] = Employee.query.filter_by(company = company, gender = "Female").count()
    result['total_count'] = Employee.query.count()
    result['percentage'] = result['female_count'] / result['total_count'] * 100
    return result

def create_all_tables():
    # statement here to create all the tables
    db.create_all()
