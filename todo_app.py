# ✅ Python To-Do App

tasks = []


def add_task():
    task = input("Enter a new task: ")

    tasks.append({
        "task": task,
        "completed": False
    })

    print("✅ Task added!")


def view_tasks():
    if not tasks:
        print("📭 No tasks yet.")
        return

    print("\n📋 YOUR TASKS")
    print("-" * 35)

    for number, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else "⏳"
        print(f"{number}. {status} {task['task']}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("🎉 Task completed!")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"🗑️ Deleted: {removed['task']}")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a number.")


def main():
    while True:
        print("\n===== ✅ TO-DO APP =====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option.")


main()
