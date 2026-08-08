print("🧠 PYTHON QUIZ GAME")
print("-------------------")

score = 0

questions = [
    {
        "question": "What language are you learning?",
        "answer": "python"
    },
    {
        "question": "What keyword is used to create a function in Python?",
        "answer": "def"
    },
    {
        "question": "What data type stores True or False?",
        "answer": "boolean"
    },
    {
        "question": "What symbol is used for comments in Python?",
        "answer": "#"
    },
    {
        "question": "What function displays text on the screen?",
        "answer": "print"
    }
]

for item in questions:
    answer = input(item["question"] + " ").lower().strip()

    if answer == item["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect!")
        print("Correct answer:", item["answer"], "\n")

print("-------------------")
print("🎯 Quiz finished!")
print("Your score:", score, "/", len(questions))

if score == len(questions):
    print("🏆 Perfect score!")
elif score >= 3:
    print("🔥 Great job!")
else:
    print("📚 Keep practicing!")
