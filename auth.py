from flask import * 
from sqlite3 import connect
Auth = Blueprint(__name__, "db", "static", template_folder="templates")
@Auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if "username" in session:
            return redirect("/")
        else:
            return render_template("login.html")

@Auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        if "username" in session:
            return redirect("/")
        else:
            return render_template("signup.html")
    else:
        conn = connect("db.sqlite3")
        curr = conn.cursor()
        form = request.form
        username = form.get("username")
        email = form.get("email")
        password = form.get("password")
        password_a = form.get("password-a")
        error = False
        curr.execute(f"SELECT * FROM Users WHERE username='{username}'")
        if curr.fetchall() != []:
            flash("Username is already assigned", "danger")
            error = True
        curr.execute(f"SELECT * FROM Users WHERE username='{username}'")
        if curr.fetchall() != []:
            flash("Email is already assigned", "danger")
            error = True
        if password != password_a:
            flash("Passwords don't match.")
            error = True
        if error:    
            return render_template("signup.html")
        else:
            return redirect("/")
@Auth.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect("/")