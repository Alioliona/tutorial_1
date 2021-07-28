from faker import Faker
import csv
from statistics import mean
import requests


def open_file():
    file = open('requirements.txt')
    return file.read()


def generate_users(number=100):
    fake = Faker()
    users = []
    for i in range(number):
        user = fake.first_name() + ' ' + fake.email()
        users.append(user)

    return (str(users))


def conv_diction():
    with open('hw (2) (1).csv') as File:
        reader = csv.DictReader(File)
        height_arr = []
        weight_arr = []
        for row in reader:
            height_item = row.get(' "Height(Inches)"')
            weight_item = row.get(' "Weight(Pounds)"')
            height_arr.append(float(height_item)*2.54) #converting to cm
            weight_arr.append(float(weight_item)*0.453592) #converting to kg

        res_height = round(mean(height_arr),2)
        res_weight = round(mean(weight_arr), 2)
        return("Average height: " + str(res_height) + "; average weight: " + str(res_weight))


def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    return ("Astronauts currently in space: " + str(r.json()["number"]))




