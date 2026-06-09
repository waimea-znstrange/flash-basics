#===========================================================
# Flask App
#===========================================================

from flask import Flask, render_template
from dotenv import load_dotenv


# Create the app
app = Flask(__name__)


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

#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()

