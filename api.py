from flask import * 
from settings import *
import random
import string
from sqlite3 import connect
Api = Blueprint(__name__, "db", "static", template_folder="templates")

@Api.route("/create-key", methods=["POST"])
def post_create_key():
    conn  = connect("db.sqlite3")
    curr = conn.cursor()
    if "expiry" in request.data:
        expiry = request.data.get("expiry")
    else:
        return jsonify({"code": 403, "message": "Expiry Days are missing."})
    try:
        expiry = int(expiry)
    except:
        return jsonify({"code": 403, "message": "Expiry days needs to be an Integer."})
    if "username" in request.data:
        username = request.data.get("username")
    else:
        return jsonify({"code": 403, "message": "Username is missing."})
    if "password" in request.data:
        password = request.data.get("password")
    else:
        return jsonify({"code": 403, "message": "Username is missing."})
    curr.execute(f"SELECT password FROM Users WHERE username='{username}'")
    if fernet.decrypt(curr.fetchall()[0][0].encode()).decode() != password:
        return jsonify({"code": 403, "message": "Username and Password aren't matching."})
    part1 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    part2 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    part3 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    key = part1 + "-" + part2 + "-" + part3
    curr.execute(f"INSERT INTO Keys VALUES('{session['username']}', '{key}', 0, '', {expiry})")
    conn.commit()
    curr.close()
    conn.close()
    return jsonify({"code": 200, "message": "Successfully added Key.", "key": key})
@Api.route("/create-key", methods=["GET"])
def get_create_key():
    if "username" not in session:
        flash("Not logged in.", "danger")
        return redirect(url_for("auth.login"))
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
    curr.execute(f"INSERT INTO Keys VALUES('{session['username']}', '{key}', 0, '', {expiry})")
    conn.commit()
    curr.close()
    conn.close()
    flash(f"Successfully created Key: {key}", "success")
    return redirect(url_for("routes.keys"))
@Api.route("/create-keys", methods=["POST"])
def post_create_keys():
    conn  = connect("db.sqlite3")
    curr = conn.cursor()
    if "expiry" in request.data:
        expiry = request.data.get("expiry")
    else:
        return jsonify({"code": 403, "message": "Expiry Days are missing."})
    try:
        expiry = int(expiry)
    except:
        return jsonify({"code": 403, "message": "Expiry days needs to be an Integer."})
    if "amount" in request.data:
        amount = request.data.get("amount")
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
        curr.execute(f"INSERT INTO Keys VALUES('{session['username']}', '{key}', 0, '', {expiry})")
    conn.commit()
    curr.close()
    conn.close()
    return jsonify({"code": 200, "message": "Successfully added Keys.", "keys": keys})
@Api.route("/create-keys", methods=["GET"])
def get_create_keys():
    if "username" not in session:
        flash("Not logged in.", "danger")
        return redirect(url_for("auth.login"))
    if "amount" in request.args:
        amount = request.args.get("amount")
    else:
        flash("Amount of keys is missing.", "danger")
        return redirect(url_for("routes.keys"))
    try:
        amount = int(amount)
    except:
        flash("Amount needs to be an Integer.", "danger")
        return redirect(url_for("routes.keys"))       
    if "expiry" in request.args:
        expiry = request.args.get("expiry")
    else:
        flash("Expiry Days of the Keys are missing.", "danger")
        return redirect(url_for("routes.keys"))
    try:
        expiry = int(expiry)
    except:
        flash("Expiry Days needs to be an Integer.", "danger")
        return redirect(url_for("routes.keys")) 
    keys = []
    for i in range(amount):
            part1 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
            part2 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
            part3 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
            keys.append(part1 + "-" + part2 + "-" + part3)
    conn  = connect("db.sqlite3")
    curr = conn.cursor()
    for key in keys:
        curr.execute(f"INSERT INTO Keys VALUES('{session['username']}', '{key}', 0, '', {expiry})")
    conn.commit()
    curr.close()
    conn.close()
    flash("Successfully created Keys.", "success")
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
        key = request.data.get("key")
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
        return redirect(url_for("auth.login"))
    if "key" in request.args:
        key = request.args.get("key")
    else:
        flash("Key is missing", "danger")
        return redirect(url_for("routes.keys"))
    conn  = connect("db.sqlite3")
    curr = conn.cursor()
    curr.execute(f"DELETE FROM Keys WHERE key='{key}'")
    conn.commit()
    curr.close()
    conn.close()   
    flash(f"Successfully deleted Key: {key}", "success") 
    return redirect(url_for("routes.keys"))
@Api.route("/manage-key")
def manage_key():
    return "lol"
@Api.route("/activate-key", methods=["POST"])
def post_activate_key():
    if "key" in request.data:
        key = request.data.get("key")
    else:
        return jsonify({"code": 403, "message": "Key is missing"})
    conn = connect("db.sqlite3")
    curr = conn.cursor()
    curr.execute(f"UPDATE Keys SET activated=1 WHERE Key='{key}'")
    conn.commit()
    curr.close()
    conn.close()
    return jsonify({"code": 200, "message": "Successfully activated Key"})
@Api.route("/activate-key", methods=["GET"])
def get_activate_key():
    if "key" in request.args:
        key = request.args.get("key")
    else:
        return jsonify({"code": 403, "message": "Key is missing"})
    conn = connect("db.sqlite3")
    curr = conn.cursor()
    curr.execute(f"UPDATE Keys SET activated=1 WHERE Key='{key}'")
    conn.commit()
    curr.close()
    conn.close()
    flash(f"Successfully activated Key: {key}", "success")
    return redirect(url_for("routes.keys"))
@Api.route("/deactivate-key", methods=["POST"])
def post_deactivate_key():
    return "lol"
@Api.route("/deactivate-key", methods=["GET"])
def get_deactivate_key():
    return "lol"

