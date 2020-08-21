import sqlite3

db_file = 'pets.db'

with open("something.csv", "w") as f:
    pass

connection = sqlite3.connect(db_file)
cur = connection.cursor()

print(cur.execute("CREATE TABLE IF NOT EXISTS pets (type CHAR(20), age INT, name CHAR(50))"))

cur.execute("INSERT INTO pets (type, age, name) VALUES ('lizard', 4, 'Lizzy')")
connection.commit()

cur.execute("SELECT * FROM pets")
print(cur.fetchall())
connection.close()
