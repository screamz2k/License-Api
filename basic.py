import sqlite3
conn = sqlite3.connect("db.sqlite3")
curr = conn.cursor()
#### query ####
curr.execute("SELECT * FROM Keys LIMIT 1")
for items in curr.fetchall():
    for item in items:
        print(type(item))
        print(item)