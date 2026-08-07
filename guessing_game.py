import random

print("🎯 === NUMBER GUESSING GAME ===")

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess == secret_number:
        print("🎉 Correct!")
        print("You guessed it in", attempts, "attempt(s).")
        break

    elif guess < secret_number:
        print("📈 Too low! Try again.")

    else:
        print("📉 Too high! Try again.")

print("Thanks for playing! 🚀")
