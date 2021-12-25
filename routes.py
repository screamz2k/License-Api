from flask import * 
from sqlite3 import connect
from auth import check_user_agent
Routes = Blueprint(__name__, "db", "static", template_folder="templates")

@Routes.route("/")
@check_user_agent
def index():
    if "username" in session:
        return render_template("index.html", logged_in="1", username=session['username'])
    else: 
        return render_template("index.html", logged_in="0") 
@Routes.route("/keys")
@check_user_agent
def keys():
    if "username" in session:
        conn = connect("db.sqlite3")
        curr = conn.cursor()
        keys = []
        curr.execute(f"SELECT * FROM Keys WHERE username='{session['username']}' ORDER BY Expiry DESC")
        for key in curr.fetchall():
            key = list(key)
            key.pop(0)
            print(key[3])
            if key[1] == 0:
                key[1] = False
            else:
                key[1] = True
            if key[3] > 1000:
                key[3] = "Lifetime"
            else:
                key[3] = str(key[3]) + " Days"
            keys += {'name': key[0], 'active': key[1],  'address': key[2], 'days': key[3]},
        return render_template("keys.html", logged_in="1", username=session['username'], keys=keys)
    else:
        flash("You need to be logged in.", "danger") 
        return redirect("/login")
        