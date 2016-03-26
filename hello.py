from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

#@ is a decorator; the next part is executed --> app.route('/' hello_world)
@app.route('/') #'/' is the index of a page; tells Flask to run this function
def hello(): #for an incoming requests (GET)
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form['Name']
        age = request.form['Age']
        ninja = request.form['Favorite NINJA']
        if name == '' or age == '' or ninja == '':
            return render_template('error.html')
        return render_template('login.html',name=name,age=age,ninja=ninja)
    else:
        return render_template('error.html')

@app.route('/index',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(
        host = "127.0.0.1",
        port = int("7000")
        )
