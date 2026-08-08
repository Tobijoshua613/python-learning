# 💰 Expense Tracker Pro
# A simple expense tracker using Python

expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: ₦"))
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("✅ Expense added successfully!")


def show_expenses():
    if not expenses:
        print("📭 No expenses recorded yet.")
        return

    print("\n📋 Your Expenses")
    print("-" * 40)

    for expense in expenses:
        print(
            f"{expense['name']} | "
            f"₦{expense['amount']:.2f} | "
            f"{expense['category']}"
        )


def show_total():
    total = sum(expense["amount"] for expense in expenses)

    print("-" * 40)
    print(f"💰 Total Expenses: ₦{total:.2f}")


def main():
    while True:
        print("\n===== 💰 EXPENSE TRACKER PRO =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_expenses()

        elif choice == "3":
            show_total()

        elif choice == "4":
            print("👋 Goodbye! Keep tracking your money.")
            break

        else:
            print("❌ Invalid choice. Please try again.")


main()
