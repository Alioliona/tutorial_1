from flask import Flask, request
from utils import open_file
from utils import generate_users
from utils import conv_diction
from utils import space

app = Flask('MyFirstApp')

@app.route('/requirements/')
def view_require():
     return open_file()

@app.route('/generate-users/')
def gen_users():
    query_params = request.args
    number = query_params.get('number') or ''

    min_number = 1
    default_number = 100

    if number.isdigit():
        number = int(number)
        if number < min_number:
            number = default_number

    else:
        number = default_number

    return generate_users(number)

@app.route('/mean/')
def average_data():
    return conv_diction()

@app.route('/astronauts/')
def astr_num():
    return space()

if __name__ == '__main__':
    app.run()

def add():
    pass