import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

conn.commit()
conn.close()

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Вставка данных
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Иван', 25))
conn.commit()

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Петр', 26))
conn.commit()

# Чтение данных
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()