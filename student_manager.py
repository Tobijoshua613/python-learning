# Student Manager
# My Python learning journey

students = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("✅ Student added successfully!")


def show_students():
    if not students:
        print("No students found.")
        return

    print("\n📚 Student List")

    for student in students:
        print("--------------------")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])


def main():
    while True:
        print("\n===== STUDENT MANAGER =====")
        print("1. Add student")
        print("2. Show students")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()

        elif choice == "3":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


main()
