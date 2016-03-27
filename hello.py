"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login/', methods=['GET','POST'])
def login(name=None, age=None, patrick=None):
    return render_template('login.html', name=request.form['name'], age=request.form['age'], patrick=request.form['patrick'])

if __name__ == '__main__':
    #app.debug = True
    app.run()
