from flask import * 
from settings import *
from threading import Thread
from key_ops import day_change
from routes import Routes
from api import Api
from auth import Auth
import requests as r
import os
import shutil
from zipfile import ZipFile
if auto_update:
    res = r.get("https://github.com/screamz2k/License-API/releases/latest", allow_redirects=True)
    current_ver = 0
    update_ver = res.url.split('/')[7]
    if not int(update_ver.split(".")[1]) > current_ver:
        exit()
    else:
        file = r.get(f"https://github.com/screamz2k/License-API/archive/refs/tags/{update_ver}.zip")
        with open("update.zip", "wb") as f:
            f.write(file.content)
        zip = ZipFile("update.zip")
        zip.extractall()
        for fil in os.listdir(zip.infolist()[0].filename):
            if os.path.isdir(zip.infolist()[0].filename + fil):
                shutil.rmtree(os.getcwd() + "\\" + fil)
                shutil.move(zip.infolist()[0].filename + fil, os.getcwd())
                continue
            try:
                shutil.move(zip.infolist()[0].filename + fil, os.getcwd())
            except:
                os.remove(os.getcwd() + "\\" + fil)
                shutil.move(zip.infolist()[0].filename + fil, os.getcwd())
        os.rmdir(zip.infolist()[0].filename)
        zip.close()
        os.remove(os.getcwd() + "\\" + "update.zip")
app = Flask(__name__, None, "static")
app.secret_key = secret_key
app.register_blueprint(Routes)
app.register_blueprint(Auth)
app.register_blueprint(Api, url_prefix='/api')

@app.errorhandler(404)
def error_404(e):
    flash("Page doesnt exist.", "danger")
    return redirect("/")
if __name__ == "__main__":
    Thread(target=app.run, kwargs={"threaded":True}).start()
    Thread(target=day_change).start()