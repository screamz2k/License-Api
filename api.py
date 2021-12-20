from flask import * 
import random
import string
from sqlite3 import connect
Api = Blueprint(__name__, "db", "static", template_folder="templates")
@Api.route("/create-key", methods=["POST"])
def create_key():
    if "username" not in session:
        return jsonify({"code": 403, "message": "Not logged in."})
    try:
        expiry = request.form.get["expiry"]
    except:
        return jsonify({"code": 403, "message": "Expiry Date is missing"})
    part1 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    part2 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    part3 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    key = part1 + "-" + part2 + "-" + part3
    conn  = connect("db.sqlite3")
    curr = conn.cursor()
    curr.execute(f"INSERT INTO Keys VALUES('{session['username']}', '{key}', '0', {None}, {expiry}")
    conn.commit()
    curr.close()
    conn.close()
    return jsonify({"code": 200, "message": "Successfully added Key", "key": key})
@Api.route("/create-keys")
def create_multiple_keys():
    if "username" not in session:
        return jsonify({"code": 403, "message": "Not logged in."})
    try:
        expiry = request.form.get["expiry"]
    except:
        return jsonify({"code": 403, "message": "Expiry Date is missing"})
    try:
        amount = request.form.get["amount"]
    except:
        return jsonify({"code": 403, "message": "Amount is missing"})
    keys = []
    for i in range(amount):
            part1 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
            part2 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
            part3 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
            keys.append(part1 + "-" + part2 + "-" + part3)
            print(part1 + "-" + part2 + "-" + part3)
    conn  = connect("db.sqlite3")
    curr = conn.cursor()
    for key in keys:
        curr.execute(f"INSERT INTO Keys VALUES('{session['username']}', '{key}', '0', {None}, {expiry}")
        conn.commit()
    curr.close()
    conn.close()
    return jsonify({"code": 200, "message": "Successfully added Keys", "keys": keys})
@Api.route("/delete-key")
def delete_key():
    return "lol"
@Api.route("/manage-key")
def manage_key():
    return "lol"
@Api.route("/view-key")
def view_key():
    return "lol"
@Api.route("/activate-key")
def activate_key():
    return "lol"
@Api.route("/deactivate-key")
def deactivate_key():
    return "lol"