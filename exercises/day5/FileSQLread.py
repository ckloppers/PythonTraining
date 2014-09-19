import sqlite3

db = sqlite3.connect('../db_stuff/plusplus')


cur = db.cursor()
cur.execute("""
    SELECT name, age from person
""")

while True:
    row = cur.fetchone()
    if row is None:
        break

    print row

cur.close()
db.close()
