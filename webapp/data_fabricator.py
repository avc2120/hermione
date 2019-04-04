import os
import random

from app import db
import db_utils

fortune_500 = [line.replace('\n','').replace(' ','_') for line in open('data/fortune_500_list.txt', 'r').readlines()]
studied_companies = ['Google', 'Pinterest']

def populate_db():
    populate_random_company_info()
    populate_software_4()

def populate_random_company_info():
    for company in fortune_500:
        name = company
        maternity_weeks = random.randint(10,20)
        paternity_weeks = random.randint(0,20)
        lactation_rooms = random.randint(0,50)
        mother_parking = random.randint(0,10)
        gender_neutral_bathrooms = random.randint(0,100)
        feminine_products = random.choice([True, False])
        db_utils.add_company(name, maternity_weeks, paternity_weeks, lactation_rooms, mother_parking, gender_neutral_bathrooms, feminine_products)

def populate_software_4():
    populate_employee_db(624, "Software Engineer 4", 125000, 175000, 3, 5, "Male", "Google")
    populate_employee_db(376, "Software Engineer 4", 130000, 180000, 4, 7, "Female", "Google")
    populate_employee_db(525, "Software Engineer 4", 130000, 150000, 3, 5, "Male", "Pinterest")
    populate_employee_db(475, "Software Engineer 4", 130000, 150000, 3, 5, "Female", "Pinterest")

def populate_employee_db(count, title, salary_min, salary_max, yoe_min, yoe_max, gender, company):
    for i in range(count):
        salary = random.randint(salary_min, salary_max)
        yoe = random.randint(yoe_min, yoe_max)
        db_utils.add_employee(title, salary, yoe, gender, company)
