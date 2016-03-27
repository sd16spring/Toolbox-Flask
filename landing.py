"""
Simple web app using flask
"""

from flask import Flask
app = Flask(__name__)
from flask import render_template, request, url_for

def valid_login(username, userage, userfav):
    if username and userage and userfav:
        return True

def is_patrick(userfav):
    acceptable_names_for_patrick = ['Patrick', 'patrick', 'p-ricky', 'p-swizzle',
                                     'ptrk', 'baby pat', 'p hust']
    if userfav in acceptable_names_for_patrick:
        return True
    else:
        return False

def log_the_user_in(username):
    return "hello " + username + "!!!"

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():

    error = None
    if valid_login(request.form['user_name'],
                   request.form['user_age'],
                   request.form['user_fav']):
        # check to see if their favorite ninja is patrick
        if not is_patrick(request.form['user_fav']):
            # return request.form['user_fav'] + "you suck!"
            error_message = "You chose the wrong ninja"
            return render_template('index.html', error_message = error_message)
        name = request.form['user_name']
        age = request.form['user_age']
        return render_template('succes.html', name=name, age=age)
    else:
        error_message = "You forgot to fill out a field"
        return render_template('index.html', error_message = error_message)


if __name__ == '__main__':
    app.debug = True
    app.run()
