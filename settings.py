from dotenv import load_dotenv
from cryptography.fernet import Fernet
from os import getenv
load_dotenv()
secret_key = getenv("secret_key")
fernet = Fernet(getenv("dec_key").encode())
user_agent = getenv("user_agent")
if getenv("agent_needed") == "True":
   agent_needed = True
else:
   agent_needed = False
