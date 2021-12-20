from flask import * 
from sqlite3 import connect
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
        conn = connect("db.sqlite3")
        curr = conn.cursor()
        keys = []
        curr.execute(f"SELECT * FROM Keys WHERE username='{session['username']}'")
        for key in curr.fetchall():
            if key[0] == "0":
                key[0] = False
            else:
                key[0] = True
            keys += {'id': key[0], 'name': key[1], 'address': key[2], 'expiry': key[3]},
        return render_template("keys.html", logged_in="1", username=session['username'], keys=keys)
    else:
        flash("You need to be logged in.", "danger") 
        return redirect("/login")
        