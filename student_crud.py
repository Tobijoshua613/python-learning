# 🗄️ Student CRUD Application
# Create, Read, Update, Delete

import sqlite3

DATABASE = "students.db"


def connect_database():
    return sqlite3.connect(DATABASE)


def create_table():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
    )
    """)

    connection.commit()
    connection.close()


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course: ")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    connection.commit()
    connection.close()

    print("✅ Student added successfully!")


def view_students():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    connection.close()

    if not students:
        print("📭 No students found.")
        return

    print("\n📚 STUDENTS")
    print("-" * 50)

    for student in students:
        print(
            f"ID: {student[0]} | "
            f"Name: {student[1]} | "
            f"Age: {student[2]} | "
            f"Course: {student[3]}"
        )


def update_student():
    view_students()

    student_id = int(input("\nEnter student ID to update: "))
    new_course = input("Enter new course: ")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE students SET course = ? WHERE id = ?",
        (new_course, student_id)
    )

    connection.commit()
    connection.close()

    print("✅ Student updated successfully!")


def delete_student():
    view_students()

    student_id = int(input("\nEnter student ID to delete: "))

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    connection.commit()
    connection.close()

    print("🗑️ Student deleted successfully!")


def main():
    create_table()

    while True:
        print("\n===== 🎓 STUDENT DATABASE =====")
        print("1. Add student")
        print("2. View students")
        print("3. Update student")
        print("4. Delete student")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option.")


main()
