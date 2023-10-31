# importing modules from flask library
from flask import Flask, render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions

# default route or 'URL'
@app.route("/")
def home():

    name = "Hemi"
    age = "17"

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/Father")
def home():

    name = "Jake"
    age = "49"

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/Mother")
def home():

    name = "huni"
    age = "42"

    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/Friends")
def home():

    name = "piya"
    age = "16"

    return render_template('friend.html' , name = name , age = age)
# run the file
app.run(debug=True)
