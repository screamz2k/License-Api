from flask import * 
from settings import *
from routes import r
from auth import Auth
app = Flask(__name__, None, "static")
app.secret_key = secret_key
app.register_blueprint(r)
app.register_blueprint(Auth)

if __name__ == "__main__":
    app.run(debug=True)