from flask import * 
from dotenv import load_dotenv
from os import getenv
from routes import r
load_dotenv()
app = Flask(__name__, None, "static")
app.secret_key = getenv("secret_key")
app.register_blueprint(r)
if __name__ == "__main__":
    app.run(debug=True)