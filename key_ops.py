from flask import * 
from settings import *
from datetime import datetime
from sqlite3 import connect
Key_Ops = Blueprint(__name__, "db", "static", template_folder="templates")
