from flask import * 
from settings import *
import random
import string
from sqlite3 import connect
Api = Blueprint(__name__, "db", "static", template_folder="templates")



class Functions():
    def check_date_format(self, date:str):
        date_splitted  = date.split("-")
        if len(date_splitted) < 3 or len(date[0]) != 4 or len(date[1]) != 2:
            return False
        try:
            test = int(date.replace("-", ""))
        except ValueError:
            return False
        else:
            return True



@Api.route("/create-key", methods=["POST"])
def post_create_key():
    conn  = connect("db.sqlite3")
    curr = conn.cursor()
    if "expiry" in request.data:
        expiry = request.data.get("expiry")
    else:
        return jsonify({"code": 403, "message": "Expiry Date is missing."})
    if "username" in request.data:
        username = request.data.get("username")
    else:
        return jsonify({"code": 403, "message": "Username is missing."})
    if "password" in request.data:
        password = request.data.get("password")
    else:
        return jsonify({"code": 403, "message": "Username is missing."})
    if not Functions.check_date_format(expiry):
        return jsonify({"code": 403, "message": "Date format should be YYYY-MM--DD"})
    curr.execute(f"SELECT password FROM Users WHERE username='{username}'")
    if fernet.decrypt(curr.fetchall()[0][0].encode()).decode() != password:
        return jsonify({"code": 403, "message": "Username and Password aren't matching."})
    part1 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    part2 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    part3 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    key = part1 + "-" + part2 + "-" + part3
    curr.execute(f"INSERT INTO Keys VALUES('{session['username']}', '{key}', '0', '', '{expiry}')")
    conn.commit()
    curr.close()
    conn.close()
    return jsonify({"code": 200, "message": "Successfully added Key.", "key": key})
@Api.route("/create-key", methods=["GET"])
def get_create_key():
    if "username" not in session:
        flash("Not logged in.", "danger")
        return redirect(url_for("routes.keys"))
    if "expiry" in request.args:
        expiry = request.args.get("expiry")
    else:
        flash("Input Expiry Date of the Keys.", "danger")
        return redirect(url_for("routes.keys"))
    part1 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    part2 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    part3 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    key = part1 + "-" + part2 + "-" + part3
    conn  = connect("db.sqlite3")
    curr = conn.cursor()
    curr.execute(f"INSERT INTO Keys VALUES('{session['username']}', '{key}', '0', '', '{expiry}')")
    conn.commit()
    curr.close()
    conn.close()
    return redirect(url_for("routes.keys"))
@Api.route("/create-keys", methods=["POST"])
def post_create_keys():
    conn  = connect("db.sqlite3")
    curr = conn.cursor()
    if "expiry" in request.data:
        expiry = request.data.get("expiry")
    else:
        return jsonify({"code": 403, "message": "Expiry Date is missing."})
    if "amount" in request.data:
        amount = request.data.get("expiry")
    else:
        return jsonify({"code": 403, "message": "Amount is missing."})
    if "username" in request.data:
        username = request.data.get("expiry")
    else:
        return jsonify({"code": 403, "message": "Username is missing."})
    if "password" in request.data:
        password = request.data.get("expiry")
    else:
        return jsonify({"code": 403, "message": "Password is missing."})
    if not Functions.check_date_format(expiry):
        return jsonify({"code": 403, "message": "Date format should be YYYY-MM--DD"})
    curr.execute(f"SELECT password FROM Users WHERE username='{username}'")
    if fernet.decrypt(curr.fetchall()[0][0].encode()).decode() != password:
        return jsonify({"code": 403, "message": "Username and Password aren't matching."})
    keys = []
    for i in range(amount):
            part1 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
            part2 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
            part3 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
            keys.append(part1 + "-" + part2 + "-" + part3)
    for key in keys:
        curr.execute(f"INSERT INTO Keys VALUES('{session['username']}', '{key}', '0', '', '{expiry}')")
    conn.commit()
    curr.close()
    conn.close()
    return jsonify({"code": 200, "message": "Successfully added Keys.", "keys": keys})
@Api.route("/create-keys", methods=["GET"])
def get_create_keys():
    if "username" not in session:
        flash("Not logged in.", "danger")
        return redirect(url_for("routes.keys"))
    if "amount" in request.args:
        amount = request.args.get("amount")
    else:
        flash("Amount of keys is missing.", "danger")
        return redirect(url_for("routes.keys"))
    if "expiry" in request.args:
        expiry = request.args.get("expiry")
    else:
        flash("Expiry Date of the Keys is missing.", "danger")
        return redirect(url_for("routes.keys"))
    if not Functions.check_date_format(expiry):
        return jsonify({"code": 403, "message": "Date format should be YYYY-MM--DD"})
    keys = []
    for i in range(amount):
            part1 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
            part2 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
            part3 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
            keys.append(part1 + "-" + part2 + "-" + part3)
    conn  = connect("db.sqlite3")
    curr = conn.cursor()
    for key in keys:
        curr.execute(f"INSERT INTO Keys VALUES('{session['username']}', '{key}', '0', '', '{expiry}')")
    conn.commit()
    curr.close()
    conn.close()
    return redirect(url_for("routes.keys"))
@Api.route("/delete-key", methods=["POST"])
def post_delete_key():
    conn  = connect("db.sqlite3")
    curr = conn.cursor()
    if "username" in request.data:
        username = request.data.get("expiry")
    else:
        return jsonify({"code": 403, "message": "Username is missing."})
    if "password" in request.data:
        password = request.data.get("expiry")
    else:
        return jsonify({"code": 403, "message": "Password is missing."})
    if "key" in request.data:
        key = request.data.get("expiry")
    else:
        return jsonify 
    curr.execute(f"SELECT password FROM Users WHERE username='{username}'")
    if fernet.decrypt(curr.fetchall()[0][0].encode()).decode() != password:
        return jsonify({"code": 403, "message": "Username and Password aren't matching"})
    curr.execute(f"DELETE FROM Keys WHERE key='{key}'")
    conn.commit()
    curr.close()
    conn.close() 
@Api.route("/delete-key", methods=["GET"])
def get_delete_key():
    if "username" not in session: 
        flash("Not logged in.", "danger")
        return redirect(url_for("routes.keys"))
    if "key" in request.args:
        key = request.args.get("expiry")
    else:
        flash("Key is missing", "danger")
        return redirect(url_for("routes.keys"))
    conn  = connect("db.sqlite3")
    curr = conn.cursor()
    curr.execute(f"DELETE FROM Keys WHERE key='{key}'")
    conn.commit()
    curr.close()
    conn.close()    
@Api.route("/manage-key")
def manage_key():
    return "lol"
@Api.route("/view-key")
def view_key():
    return "lol"
@Api.route("/activate-key", methods=["POST"])
def post_activate_key():
    return "lol"
@Api.route("/activate-key", methods=["GET"])
def get_activate_key():
    return "lol"
@Api.route("/deactivate-key", methods=["POST"])
def post_deactivate_key():
    return "lol"
@Api.route("/deactivate-key", methods=["GET"])
def get_deactivate_key():
    return "lol"

