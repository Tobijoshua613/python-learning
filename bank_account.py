# 🏦 Bank Account Practice

balance = 10000

print("=== BANK ACCOUNT ===")
print("Starting Balance: ₦", balance)

# Deposit
deposit = 5000
balance = balance + deposit

print("Deposited: ₦", deposit)
print("Current Balance: ₦", balance)

# Withdraw
withdraw = 2000

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawn: ₦", withdraw)
else:
    print("Insufficient funds!")

print("Final Balance: ₦", balance)
