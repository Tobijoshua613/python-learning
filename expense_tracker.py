print("=== EXPENSE TRACKER ===")

expenses = []

while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("What did you spend money on? ")
        amount = float(input("How much did you spend? ₦"))

        expenses.append([name, amount])
        print("✅ Expense added!")

    elif choice == "2":
        if len(expenses) == 0:
            print("📋 No expenses recorded yet.")
        else:
            print("\n=== YOUR EXPENSES ===")

            for number, expense in enumerate(expenses, start=1):
                print(number, "-", expense[0], "₦", expense[1])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense[1]

        print("💰 Total spending: ₦", total)

    elif choice == "4":
        print("👋 Goodbye! Keep tracking your money!")
        break

    else:
        print("❌ Invalid option. Please choose 1–4.")
