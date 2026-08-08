# 🧾 Python JSON Practice

import json

# Create Python data
student = {
    "name": "Joshua Tobi",
    "age": 24,
    "course": "AI Engineering",
    "skills": [
        "Python",
        "APIs",
        "Artificial Intelligence"
    ]
}

# Convert Python dictionary to JSON
json_data = json.dumps(student, indent=4)

print("📦 JSON DATA")
print(json_data)

# Save JSON to a file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("\n✅ Student information saved to student.json")


# Read JSON from the file
with open("student.json", "r") as file:
    loaded_student = json.load(file)

print("\n📖 INFORMATION FROM JSON FILE")
print("-----------------------------")
print("Name:", loaded_student["name"])
print("Age:", loaded_student["age"])
print("Course:", loaded_student["course"])
print("Skills:", ", ".join(loaded_student["skills"]))
