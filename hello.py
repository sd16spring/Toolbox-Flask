"""
Web application using Flask. User submits their name, age and favorite ninja,
and the webpage brings them to a form with all of the info.
"""
from flask import Flask, render_template, request
from jinja2 import Template
app = Flask(__name__)

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submission', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        if name!= '' and age != '' and request.form['favninja'] != '':
            if len(name) < 3:
                error = 'Error: Name too short.'
            elif has_numbers(name):
                error = 'Error: Name can\'t have numbers'
            else: 
                return render_template('submission.html', name=name, age=age)
        else:
            error = 'Error: Please fill out all fields'
    # the code below is executed if the login is invalid or the fields aren't
    #filled out
    return render_template('error.html', error=error)

if __name__ == '__main__':
    app.run()