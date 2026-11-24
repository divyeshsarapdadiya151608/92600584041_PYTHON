# 9. Connect Python with a database and execute SQL queries.
# Connect Python with SQLite database
import sqlite3

# Establish database connection
conn = sqlite3.connect("college.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# Insert records
cursor.execute(
    "INSERT INTO Student (name, marks) VALUES (?, ?)",
    ("Rahul", 85)
)

cursor.execute(
    "INSERT INTO Student (name, marks) VALUES (?, ?)",
    ("Amit", 90)
)

# Execute SELECT query
cursor.execute("SELECT * FROM Student")

# Display records
records = cursor.fetchall()

for row in records:
    print(row)

# Commit changes and close connection
conn.commit()
conn.close()
