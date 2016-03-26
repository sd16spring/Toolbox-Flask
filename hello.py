"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__, template_folder='Templates')#Toolbox-Flask/Templates is just Templates

@app.route('/', methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/test')
def test(): #what this is called actualy doesn't matter. It's the route and the stuff that's returned
    return 'Test!'

@app.route('/formdata.asp', methods = ['GET','POST'])
def formdata():
    info = {}
    if request.method=="POST":
        if request.form["Name"] and request.form["Age"] and request.form["Patrick"]:
            return render_template('formdata.html', name=request.form["Name"],age=request.form["Age"],favninja=request.form["Patrick"])
        return render_template('error.html')

        # return info["Name"]
    else:
        if info["Name"]:
            return info["Name"]
        return "0"

if __name__ == '__main__':
    app.run(debug=True)
