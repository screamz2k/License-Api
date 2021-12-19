import sqlite3
conn = sqlite3.connect("db.sqlite3")
curr = conn.cursor()
#### query ####
"""curr.execute("CREATE TABLE Users(ID int NOT NULL, Email VARCHAR(50), Username VARCHAR(20), Password VARCHAR(100), PRIMARY KEY (ID))")
conn.commit()
"""
curr.execute("SELECT * FROM users WHERE username='lo'")
print(curr.fetchall())