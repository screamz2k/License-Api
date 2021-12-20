import sqlite3
conn = sqlite3.connect("db.sqlite3")
curr = conn.cursor()
#### query ####
curr.execute("SELECT * FROM Users")
print(curr.fetchall())