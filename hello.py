"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request, url_for
app = Flask(__name__)

'''with app.test_request_context('/form', method='POST'):
    assert request.path == '/form'
    assert request.method == 'POST'
'''
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login')
def login():
	return render_template('action.html')

@app.route('/form', methods=['POST'])
def form():
	name = request.form['name']
	age = request.form['age']
	ninja = request.form['ninja']
	if name == '' or age == '' or ninja == '':
		return render_template('error.html', error="At least one of the fields was empty!")
	else:
		try:
			int(age)
		except ValueError:
			return render_template('error.html', error="Age must be an integer")
		return render_template('form.html', name=name, age=age, ninja='Patrick Huston')

if __name__ == '__main__':
    app.run()