from application import app
from flask import render_template
# create simple routes
# @ is a decorator
@app.route("/")
@app.route("/index")

def index():
    # render html template from templates folder
    return render_template("index.html")