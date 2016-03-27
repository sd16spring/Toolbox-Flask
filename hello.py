"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import render_template, request, redirect
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/')
def hello_world():
	print 'Hi'
	#return 'Hello World!'
	return render_template('register.html')

@app.route('/Register', methods=['GET', 'POST']) # The most useful
def register(name=None, age=None):
	print "In Register"
	if request.method == 'POST':
		print "In Post thing"
		return render_template('info.html')
	print "Rendering register.html"
	return render_template('register.html')

@app.route('/Info', methods=['GET', 'POST'])
#@app.route('/Info/<name>/<age>', methods=['GET, POST'])
def info():
	print request.method
	if request.method == 'POST':
		return render_template('info.html', name=request.form['name'], age=request.form['age'])
	return 'Nope'

if __name__ == '__main__':
	app.run()
