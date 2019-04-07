import os, sys, random, json
from datetime import datetime, timedelta
from sqlalchemy import func
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Boolean
from app import db
import pandas as pd
import time

###########
# Company #
###########

class Company(db.Model):
    __tablename__ = 'companies'
    name = Column(String(250), primary_key=True, unique=True, nullable=False)
    maternity_weeks = Column(Float, default=0.00)
    paternity_weeks = Column(Float, default=0.00)
    lactation_rooms = Column(Float, default=0.00)
    mother_parking = Column(Float, default=0.00)
    gender_neutral_bathrooms = Column(Float, default=0.00)
    feminine_products = Column(Float, default=0.00)
    score = Column(Float, default=0.00)

    def to_dict(self):
        data = {}
        data['name'] = self.name
        data['maternity_weeks'] = self.maternity_weeks
        data['paternity_weeks'] = self.paternity_weeks
        data['lactation_rooms'] = self.lactation_rooms
        data['mother_parking'] = self.mother_parking
        data['gender_neutral_bathrooms'] = self.gender_neutral_bathrooms
        data['feminine_products'] = self.feminine_products
        data['score'] = self.score
        return data

    def to_json(self):
        return json.dumps(self.to_dict())

def add_company(name, maternity_weeks, paternity_weeks, lactation_rooms, mother_parking, gender_neutral_bathrooms, feminine_products, score):
    company = Company(name = name, maternity_weeks = maternity_weeks, paternity_weeks = paternity_weeks, lactation_rooms = lactation_rooms, mother_parking = mother_parking, gender_neutral_bathrooms = gender_neutral_bathrooms, feminine_products = feminine_products, score = score)
    db.session.add(company)
    db.session.commit()

def get_all_companies():
    print(pd.read_sql_query(db.session.query(Company).statement, db.engine))
    return Company.query.all()

def get_all_companies_df():
    return pd.read_sql_query(db.session.query(Company).statement, db.engine)

def get_company_scores(company = "All", limit = 0):
    query = db.session.query(Company).order_by(Company.score.desc())
    if company != "All":
        query = query.filter(Company.name == company)
    if limit != 0:
        query = query.limit(limit)
    return pd.read_sql_query(query.statement, db.engine)

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
    leadership = Column(Boolean, default=False)

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

def add_employee(title, salary, yoe, gender, company, leadership = False):
    employee = Employee(title = title, salary = salary, yoe = yoe, gender = gender, company = company, leadership = leadership)
    db.session.add(employee)
    db.session.commit()

def build_employee_query(company = "All", title = "All"):
    query = db.session.query(Employee)
    if company != "All":
        query = query.filter(Employee.company == company)
    if title != "All":
        query = query.filter(Employee.title == title)
    return query

def build_info_query(company):
    query = db.session.query(Info)
    if company != "All":
        query = query.filter(Employee.company == company)
    return query

def get_all_employees(company = "All"):
    return build_employee_query(company = company).all()

def get_all_employees_df(company = "All", title = "All"):
    query = build_employee_query(company, title)
    return pd.read_sql_query(query.statement, db.engine)

def get_women_pct(company = "All", title = "All"):
    result = {}
    base_query = build_employee_query(company, title)
    result['female_count'] = base_query.filter_by(gender = "Female").count()
    result['total_count'] = base_query.count()
    result['percentage'] = result['female_count'] / result['total_count'] * 100
    return result

def get_companies():
    time.sleep(0.5)
    base_query = build_employee_query().with_entities(Employee.company).distinct().all()
    return [i[0] for i in base_query]

def get_women_pct_df(company = "All", title = "All", leadership = False):
    query = db.session.query(Employee.gender, db.func.count(Employee.id).label('total'))
    if company != "All":
        query = query.filter(Employee.company == company)
    if title != "All":
        query = query.filter(Employee.title == title)
    if leadership == True:
        query = query.filter(Employee.leadership == True)
    return pd.read_sql_query(query.group_by(Employee.gender).statement, db.engine)

def create_all_tables():
    # statement here to create all the tables
    db.create_all()
