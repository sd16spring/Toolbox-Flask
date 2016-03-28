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
    
@app.route('/answers/', methods=['GET','POST'])
def answers(name=None, age=None, fav=None):
    return render_template('answers.html', name=request.form['name'], age=request.form['age'], fav=request.form['fav'])


if __name__ == '__main__':
    app.debug = True
    app.run()
