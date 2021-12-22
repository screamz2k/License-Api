from flask import * 
from settings import *
from routes import Routes
from api import Api
from auth import Auth
from key_ops import Key_Ops
app = Flask(__name__, None, "static")
app.secret_key = secret_key
app.register_blueprint(Routes)
app.register_blueprint(Auth)
app.register_blueprint(Key_Ops)
app.register_blueprint(Api, url_prefix='/api')

@app.errorhandler(404)
def error_404(e):
    flash("Page doesnt exist.", "danger")
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)