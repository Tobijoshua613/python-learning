print("=== Password Strength Checker ===")

password = input("Create a password: ")

if len(password) < 6:
    print("❌ Weak password")
    print("Your password should have at least 6 characters.")

elif len(password) < 10:
    print("⚠️ Medium password")
    print("Try making it longer.")

else:
    print("✅ Strong password!")
    print("Great job! Your password is long enough.")

print("🔐 Keep your passwords private!")
