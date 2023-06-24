# import the flask class
from flask import Flask

# create an app
# __name__ is the special name for the current application/variable being rendered
app = Flask(__name__)

# import the routes file with the routing patterns
from application import routes