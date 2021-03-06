from os import system
import string as s
from random import choices
from datetime import datetime
system("pip3 install -r requirements.txt")
from sqlite3 import connect
from cryptography.fernet import Fernet
connection = connect("db.sqlite3")
cursor = connection.cursor()
cursor.execute("CREATE TABLE Keys(Username VARCHAR(50), Key VARCHAR(150), Activated INT, Address VARCHAR(100), Expiry INT)")
cursor.execute("CREATE TABLE Users(Email VARCHAR(50), Username VARCHAR(50), Password VARCHAR(800))")
connection.commit()
connection.close()
secret_key =  "".join(choices(s.ascii_uppercase + s.ascii_lowercase +s.digits, k=25))
dec_key = Fernet.generate_key().decode()
env_string = f'''secret_key = "{secret_key}"
dec_key = "{dec_key}"
user_agent = ""
agent_needed = "False"
auto_update = "True"
'''
with open(".env", "w") as f:
    f.write(env_string)
with open("date.txt", "w") as f:
    f.write(datetime.today().strftime(r"%d/%m/%y"))
input("Finished Setup. Press Enter to exit.")