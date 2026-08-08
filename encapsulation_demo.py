# 🔐 Python Encapsulation Practice


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₦{amount} deposited successfully.")
        else:
            print("❌ Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("❌ Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"₦{amount} withdrawn successfully.")

    def get_balance(self):
        return self.__balance


# Create an account
account = BankAccount("Joshua", 10000)

print("🏦 BANK ACCOUNT")
print("----------------")

print("Owner:", account.owner)
print("Balance: ₦", account.get_balance())

account.deposit(5000)
print("Balance: ₦", account.get_balance())

account.withdraw(3000)
print("Balance: ₦", account.get_balance())
