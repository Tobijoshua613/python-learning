# 📊 Grade Calculator

print("=== GRADE CALCULATOR ===")

name = input("Enter student name: ")

score = float(input("Enter student's score (0-100): "))

if score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 45:
    grade = "D"
elif score >= 40:
    grade = "E"
else:
    grade = "F"

print("\nStudent:", name)
print("Score:", score)
print("Grade:", grade)

if grade == "A":
    print("Excellent work! 🎉")
elif grade == "B":
    print("Very good! 👍")
elif grade == "C":
    print("Good effort! 💪")
elif grade == "D" or grade == "E":
    print("Keep practicing! 📚")
else:
    print("Don't give up. Keep learning! 🚀")
