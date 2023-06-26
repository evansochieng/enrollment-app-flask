from application import app
from flask import render_template
# create simple routes
# @ is a decorator
@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    # render html template from templates folder
    return render_template("index.html")

@app.route("/login")
def login():
    # render html template from templates folder
    return render_template("login.html")

@app.route("/courses")
def courses():
    # render html template from templates folder
    return render_template("courses.html")

@app.route("/register")
def register():
    # render html template from templates folder
    return render_template("register.html")