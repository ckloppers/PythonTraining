import sqlite3

db = sqlite3.connect('../db_stuff/plusplus')

cur = db.cursor()

cur.execute("""
  insert into person
    (name, age)
  values (?,?)
""", ('CORNE',99) )


db.commit()

db.close()