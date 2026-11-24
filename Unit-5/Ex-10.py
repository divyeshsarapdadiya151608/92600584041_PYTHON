# 10. Retrieve database records using the fetchone, fetchmany, and fetchall methods.
# Retrieve records using fetchone, fetchmany and fetchall
import sqlite3

# Connect to database
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# Insert sample records
cursor.execute("DELETE FROM Student")

students = [
    (1, "Rahul", 85),
    (2, "Amit", 90),
    (3, "Priya", 88),
    (4, "Neha", 92),
    (5, "Raj", 80)
]

cursor.executemany(
    "INSERT INTO Student VALUES (?, ?, ?)",
    students
)

conn.commit()

# Using fetchone()
cursor.execute("SELECT * FROM Student")
print("Using fetchone():")
print(cursor.fetchone())

# Using fetchmany()
cursor.execute("SELECT * FROM Student")
print("\nUsing fetchmany():")
print(cursor.fetchmany(3))

# Using fetchall()
cursor.execute("SELECT * FROM Student")
print("\nUsing fetchall():")
print(cursor.fetchall())

# Close connection
conn.close()
