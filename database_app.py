# 🗄️ Python SQLite Database Practice

import sqlite3

# Connect to the database
connection = sqlite3.connect("students.db")

# Create a cursor
cursor = connection.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

# Add a student
name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter course: ")

cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    (name, age, course)
)

connection.commit()

print("✅ Student saved to database!")

# Display students
cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("\n📚 STUDENTS DATABASE")
print("-" * 40)

for student in students:
    print(
        f"ID: {student[0]} | "
        f"Name: {student[1]} | "
        f"Age: {student[2]} | "
        f"Course: {student[3]}"
    )

# Close database
connection.close()

print("\n🔒 Database connection closed.")
