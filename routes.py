import re
from flask import * 
from sqlite3 import connect

r = Blueprint(__name__, "db", "static", template_folder="templates")
@r.route("/")
def index():
    if "username" in session:
        return render_template("index.html", logged_in="1", username=session['username'])
    else: 
        return render_template("index.html", logged_in="0") 