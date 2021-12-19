from flask import * 
from sqlite3 import connect
r = Blueprint(__name__, "db", "static", template_folder="templates")
conn = connect("db.sqlite3")
@r.route("/")
def index():
    if "username" in session:
        return render_template("index.html", logged_in="1", username=session['username'])
    else: 
        return render_template("index.html", logged_in="0") 

@r.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if "username" in session:
            return redirect("/")
        else:
            return render_template("login.html")

@r.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        if "username" in session:
            return redirect("/")
        else:
            return render_template("signup.html")
    else:
        return jsonify(request.data)

@r.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect("/")