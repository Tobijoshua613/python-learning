# 🧠 Python Quiz App

questions = [
    {
        "question": "What language are we learning?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "What does API stand for?",
        "options": [
            "A. Application Programming Interface",
            "B. Advanced Python Instruction",
            "C. Automatic Program Internet",
            "D. Application Process Input"
        ],
        "answer": "A"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. String"],
        "answer": "C"
    },
    {
        "question": "Which keyword creates a function in Python?",
        "options": ["A. function", "B. def", "C. create", "D. func"],
        "answer": "B"
    }
]


def run_quiz():
    score = 0

    print("🧠 PYTHON QUIZ")
    print("=" * 30)

    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {number}:")
        print(question["question"])

        for option in question["options"]:
            print(option)

        answer = input("Your answer: ").upper()

        if answer == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {question['answer']}.")

    print("\n🎯 QUIZ COMPLETE")
    print("-" * 30)
    print(f"Your score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.0f}%")

    if percentage >= 75:
        print("🏆 Excellent work!")
    elif percentage >= 50:
        print("👍 Good effort!")
    else:
        print("📚 Keep practicing!")


run_quiz()
