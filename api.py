from flask import * 
from sqlite3 import connect
Api = Blueprint(__name__, "db", "static", template_folder="templates")
@Api.route("/create-key")
def create_key():
    if "username" in session:
        pass
@Api.route("/create-keys")
def create_multiple_keys():
    return "lol"
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