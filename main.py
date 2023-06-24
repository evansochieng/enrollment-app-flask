# import the flask class
from flask import Flask

# create an app
# __name__ is the special name for the current application/variable being rendered
app = Flask(__name__)

# create simple routes
# @ is a decorator
@app.route("/")
@app.route("/home")

def index():
    return "<h1>Hello, Evans! This is a first great step!</h1>"