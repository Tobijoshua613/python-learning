print("=== PYTHON FUNCTIONS ===")


def greet(name):
    print("Hello,", name)
    print("Welcome to your Python learning journey!")


def add_numbers(number1, number2):
    result = number1 + number2
    return result


def calculate_total(price, quantity):
    total = price * quantity
    return total


# Using our functions

greet("Joshua")

answer = add_numbers(10, 20)
print("10 + 20 =", answer)

shopping_total = calculate_total(2500, 3)
print("Shopping total: ₦", shopping_total)

print("🚀 Functions make code reusable!")
