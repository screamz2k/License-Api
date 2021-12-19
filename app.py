from flask import * 
from settings import *
from routes import Routes
from auth import Auth
app = Flask(__name__, None, "static")
app.secret_key = secret_key
app.register_blueprint(Routes)
app.register_blueprint(Auth)

if __name__ == "__main__":
    app.run(debug=True)