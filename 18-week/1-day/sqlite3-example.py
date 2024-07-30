import sqlite3

conn = sqlite3.connect("db.sqlite3")
db = conn.cursor( )

db.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
)

db.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("John", 30))
users = db.execute("SELECT * FROM users")

print(users)
print(users.fetchall())

conn.commit()
conn.close()
