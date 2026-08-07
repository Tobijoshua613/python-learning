print("=== MY TO-DO LIST ===")

tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("✅ Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("📋 Your list is empty.")
        else:
            print("\nYour tasks:")
            for number, task in enumerate(tasks, start=1):
                print(number, "-", task)

    elif choice == "3":
        if len(tasks) == 0:
            print("📋 Nothing to remove.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(number, "-", task)

            number = int(input("Enter task number to remove: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print("🗑️ Removed:", removed)
            else:
                print("❌ Invalid task number.")

    elif choice == "4":
        print("👋 Goodbye! Keep coding!")
        break

    else:
        print("❌ Invalid choice.")
