from flask import Flask,render_template,flash
from flask import request
from flask_bootstrap import Bootstrap
from wtforms import Form,TextField,TextAreaField,StringField

#App config
DEBUG = True
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)
app.config['SECERET_KEY'] = 'SuperSecretKey'

@app.route('/')
def hello_world():
    print(request.method)
    print(request.headers)
    return 'Hello, World!'

@app.route('/user/<name>')
def hello_world1(name):
    return 'Welcome, %s' % format(name)

@app.route('/about')
@app.route('/about1')
def about():
    var1 = "Ram ram ji. Jai shree ram"
    return render_template('index.html', myvar = var1)

@app.route('/dinner/')
@app.route('/dinner/<food>')
def eat(food=None):
    return render_template('food.html',food=food)

@app.route('/dinner1/')
@app.route('/dinner1/<food>')
def eat1(food=None):
    return render_template('food1.html',food=food, list=["pizza","bharta","bhindi"])

@app.errorhandler(404)
def errorhandle(error):
    return render_template('pagenotfound.html'), 404

if __name__ == '__main__':
    app.run(debug=True)