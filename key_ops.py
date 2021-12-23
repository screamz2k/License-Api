import datetime
from time import sleep
from sqlite3 import connect



def day_change():
    while True:
        conn = connect("db.sqlite3")
        curr = conn.cursor()
        curr.execute("SELECT Key, Expiry, Activated FROM Keys")
        with open("date.txt") as f:
            curr_date = f.read()
            curr_date = datetime.datetime.strptime(curr_date, r"%d/%m/%y")
        days_between = datetime.datetime.today() - curr_date
        if days_between != 0:
            for key, key_days, active in curr.fetchall():
                if key_days > 600 or active == 0:
                    continue
                key_days -= days_between.days
                if key_days < 0:
                    key_days = 0
                curr.execute(f"UPDATE Keys SET Expiry={key_days} WHERE Key='{key}'")
            conn.commit()
            conn.close()
            with open("date.txt", "w") as f:
                f.write(datetime.datetime.today().strftime(r"%d/%m/%y"))
        sleep(10*60*60)
        
