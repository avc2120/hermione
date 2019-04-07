import os
import random

from app import db
import db_utils

fortune_500 = [line.replace('\n','').replace(' ','_') for line in open('data/fortune_500_list.txt', 'r').readlines()]
studied_companies = ['Google', 'Pinterest', 'LinkedIn', 'Workday']

def populate_db():
    populate_random_company_info()
    populate_software_1()
    populate_software_4()
    populate_manager_roles()

def populate_random_company_info():
    for company in fortune_500:
        name = company
        maternity_weeks = round(random.uniform(0.00,100.00),2)
        paternity_weeks = round(random.uniform(0.00,100.00),2)
        lactation_rooms = round(random.uniform(0.00,100.00),2)
        mother_parking = round(random.uniform(0.00,100.00),2)
        gender_neutral_bathrooms = round(random.uniform(0.00,100.00),2)
        feminine_products = round(random.uniform(0.00,100.00),2)
        score = maternity_weeks * .25 + paternity_weeks * .30 + lactation_rooms * .10 + mother_parking * .20 + gender_neutral_bathrooms * .10 + feminine_products * .05
        db_utils.add_company(name, maternity_weeks, paternity_weeks, lactation_rooms, mother_parking, gender_neutral_bathrooms, feminine_products, score)
    db_utils.add_company("Pinterest", 100.00, 94.10, 87.70, 91.60, 96.8, 100.00, 95.00)
    db_utils.add_company("LinkedIn", 95.00, 89.10, 82.70, 91.60, 96.8, 100.00, 93.72)

def populate_software_1():
    populate_employee_db(300, "Software Engineer 1", 110000, 120000, 0, 2, "Male", "Google")
    populate_employee_db(198, "Software Engineer 1", 115000, 125000, 0, 3, "Female", "Google")
    populate_employee_db(101, "Software Engineer 1", 95000, 110000, 0, 2, "Male", "Pinterest")
    populate_employee_db(82, "Software Engineer 1", 95000, 110000, 0, 2, "Female", "Pinterest")
    populate_employee_db(101, "Software Engineer 1", 92000, 120000, 0, 2, "Male", "LinkedIn")
    populate_employee_db(82, "Software Engineer 1", 93000, 110000, 0, 2, "Female", "LinkedIn")

def populate_software_4():
    populate_employee_db(624, "Software Engineer 4", 125000, 175000, 3, 5, "Male", "Google")
    populate_employee_db(376, "Software Engineer 4", 130000, 180000, 4, 7, "Female", "Google")
    populate_employee_db(525, "Software Engineer 4", 130000, 150000, 3, 5, "Male", "Pinterest")
    populate_employee_db(475, "Software Engineer 4", 130000, 150000, 3, 5, "Female", "Pinterest")
    populate_employee_db(101, "Software Engineer 1", 92000, 120000, 2, 4, "Male", "LinkedIn")
    populate_employee_db(82, "Software Engineer 1", 93000, 110000, 1, 2, "Female", "LinkedIn")

def populate_manager_roles():
    populate_employee_db(55, "Manager", 165000, 205000, 3, 5, "Male", "Google", True)
    populate_employee_db(12, "Manager", 155000, 200000, 4, 7, "Female", "Google", True)
    populate_employee_db(19, "Manager", 150000, 170000, 3, 5, "Male", "Pinterest", True)
    populate_employee_db(25, "Manager", 145000, 165000, 3, 5, "Female", "Pinterest", True)
    populate_employee_db(19, "Manager", 130000, 160000, 3, 5, "Male", "LinkedIn", True)
    populate_employee_db(25, "Manager", 125000, 165000, 3, 5, "Female", "LinkedIn", True)

def populate_employee_db(count, title, salary_min, salary_max, yoe_min, yoe_max, gender, company, leadership = False):
    for i in range(count):
        salary = random.randint(salary_min, salary_max)
        yoe = random.randint(yoe_min, yoe_max)
        db_utils.add_employee(title, salary, yoe, gender, company, leadership)
