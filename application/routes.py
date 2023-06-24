from application import app

# create simple routes
# @ is a decorator
@app.route("/")
@app.route("/index")

def index():
    return "<h1>Hello, Evans! This is a first great step!</h1>"