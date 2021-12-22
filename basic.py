import sqlite3
conn = sqlite3.connect("db.sqlite3")
curr = conn.cursor()
#### query ####
curr.execute("CREATE TABLE Keys(Username VARCHAR(50), Key VARCHAR(150), Activated INT, Address VARCHAR(100), Expiry INT)")
conn.commit()