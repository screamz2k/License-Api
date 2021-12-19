from flask import * 
from sqlite3 import connect
from functools import wraps
Routes = Blueprint(__name__, "db", "static", template_folder="templates")
@Routes.route("/")
def index():
    if "username" in session:
        return render_template("index.html", logged_in="1", username=session['username'])
    else: 
        return render_template("index.html", logged_in="0") 
@Routes.route("/keys")
def keys():
    if "username" in session:
        return render_template("index.html", logged_in="1", username=session['username'])
    else:
        flash("You need to be logged in.", "danger") 
        return redirect("/login")