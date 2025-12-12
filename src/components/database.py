import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute(""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREAMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
"")

cursor.execute("INSERT INTO students (name, age,grade) VALUES('ALI', 15, '9th')")
cursor.execute("INSERT INTO students (name, age,grade) VALUES('HASSAN', 15, '10th')")
cursor.execute("INSERT INTO students (name, age,grade) VALUES('SARA', 15, '8th')")

connection.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()