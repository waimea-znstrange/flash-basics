#===========================================================
# Flask App
#===========================================================

from flask import Flask, render_template
from dotenv import load_dotenv


# Create the app
app = Flask(__name__)

    
cats = [
    {
        "id":13,
        "name":"Zeb",
    },
    {   "id":14,
        "name":"Trinh",
    },
    
    {
        "id":15,
        "name":"David"
    } 
]

def get_cat(id):
    return next((item for item in cats if item["id"] == id), None)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Welcome!
#-----------------------------------------------------------
@app.get("/")
def show_welcome():
    return render_template("pages/home.jinja")


#-----------------------------------------------------------
# Demo
#-----------------------------------------------------------
@app.get("/demo")
def show_demo_message():
    return render_template("pages/demo.jinja")

#-----------------------------------------------------------
# Matching an ID
#-----------------------------------------------------------
@app.get("/thing/<int:id>")
def show_message_with_id(id):
    print(f"Found ID: {id}")

    return render_template("pages/id.jinja", id=id)

#-----------------------------------------------------------
# Lists of data
#-----------------------------------------------------------
@app.get("/cats")
def show_message_with_list():

    return render_template("pages/cats.jinja", cats=cats)

#-----------------------------------------------------------
# Specific Cat
#-----------------------------------------------------------
@app.get("/cat/<int:id>")
def show_a_cat(id):
    cat = get_cat(id)

    if cat:
        return render_template("pages/cat.jinja", cat=cat)
    else:
        abort(404)

#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()

