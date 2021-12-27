from flask import *
from sqlite3 import connect
from settings import *
from functools import wraps
Auth = Blueprint(__name__, "db", "static", template_folder="templates")


def check_user_agent(check):
    @wraps(check)
    def wrap(*args, **kwargs):
        if str(request.user_agent) != user_agent and agent_needed:
            return jsonify({"code": "406", "message": "User Agent isnt the right."}), 406
        else:
            return check(*args, **kwargs)
    return wrap


@Auth.route("/login", methods=["GET", "POST"])
@check_user_agent
def login():
    if request.method == "GET":
        if "username" in session:
            return redirect("/")
        else:
            return render_template("login.html")
    elif request.method == "POST":
        conn = connect("db.sqlite3")
        curr = conn.cursor()
        try:
            username_email = request.form['username']
            password = request.form['password']
        except:
            flash("An Error occured.", "danger")
            curr.close()
            conn.close()
            return redirect("/login")
        if "@" in username_email:
            curr.execute(f"SELECT * FROM Users WHERE email='{username_email}'")
            data = curr.fetchall()
            if data == []:
                flash("Email isn't registered.", "danger")
                curr.close()
                conn.close()
                return redirect('/login')
        else:
            curr.execute(f"SELECT * FROM Users WHERE username='{username_email}'")
            data = curr.fetchall()
            if data == []:
                flash("User isn't registered.", "danger")
                curr.close()
                conn.close()
                return redirect('/login')
        if password == fernet.decrypt(data[0][2].encode()).decode():
            session["username"] = data[0][1]
            session["password"] = data[0][2]
            flash("Logged in successfully.", "success")
            curr.close()
            conn.close()
            return redirect("/")
        else:
            flash("User/Email and Password dont match or User doens't exist.", "danger")
            curr.close()
            conn.close()
            return redirect("/login")



@Auth.route("/signup", methods=["GET", "POST"])
@check_user_agent
def signup():
    if request.method == "GET":
        if "username" in session:
            return redirect("/")
        else:
            return render_template("signup.html")
    else:
        conn = connect("db.sqlite3")
        curr = conn.cursor()
        try:
            form = request.form
            username = form.get("username")
            email = form.get("email")
            password = form.get("password")
            password_a = form.get("password-a")
        except:
            flash("An Error occured.", "danger")
            curr.close()
            conn.close()
            return redirect("/signup")            
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
            flash("Passwords don't match.", "danger")
            error = True
        if len(password) < 9:
            flash("Password is too short", "danger")
            error = True
        if len(email) < 10:
            flash("Email is too short", "danger")
            error = True     
        if len(username) < 3:
            flash("Username is too short", "danger")
            error = True            
        if error:
            return render_template("signup.html")
        print(f"INSERT INTO Users VALUES('{email}', '{username}', '{fernet.encrypt(password.encode('utf-8')).decode('utf-8')}')")
        curr.execute(
            f"INSERT INTO Users VALUES('{email}', '{username}', '{fernet.encrypt(password.encode('utf-8')).decode('utf-8')}')")
        conn.commit()
        session["username"] = username
        session["password"] = password
        flash("Signed up successfully", "success")
        curr.close()
        conn.close()
        return redirect("/")



@Auth.route("/logout", methods=["GET", "POST"])
@check_user_agent
def logout():
    session.clear()
    return redirect("/")
