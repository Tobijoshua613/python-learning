# 📁 Python File Manager Practice

filename = "notes.txt"

# Write to a file
with open(filename, "w") as file:
    file.write("Welcome to my Python learning journey!\n")
    file.write("I am learning Python and AI Engineering.\n")

print("✅ File created successfully!")


# Read the file
with open(filename, "r") as file:
    content = file.read()

print("\n📖 FILE CONTENT")
print("----------------")
print(content)


# Add more information
with open(filename, "a") as file:
    file.write("My goal is to build useful AI applications. 🚀\n")

print("✅ New information added!")
