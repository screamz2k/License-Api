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
        keyss = []
        curr.execute(f"SELECT * FROM Keys WHERE username='{session['username']}'")
        for keys in curr.fetchall():
            keys = list(keys)
            keys.pop(0)
            print(keys[3])
            if keys[1] == 0:
                keys[1] = False
            else:
                keys[1] = True
            keyss += {'name': keys[0], 'active': keys[1],  'address': keys[2], 'expiry': keys[3]},
        return render_template("keys.html", logged_in="1", username=session['username'], keys=keyss)
    else:
        flash("You need to be logged in.", "danger") 
        return redirect("/login")
        