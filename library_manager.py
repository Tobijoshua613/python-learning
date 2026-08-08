# 📚 Library Management System
# My first Python OOP project

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"✅ You borrowed: {self.title}")
        else:
            print(f"❌ Sorry, {self.title} is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"✅ You returned: {self.title}")
        else:
            print(f"ℹ️ {self.title} is already in the library.")

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"📖 {self.title} by {self.author} - {status}")


# Create books
book1 = Book("Python for Beginners", "Joshua Tobi")
book2 = Book("Artificial Intelligence Basics", "OpenAI")

# Display books
print("📚 MY LIBRARY")
print("-" * 30)

book1.display_info()
book2.display_info()

# Borrow a book
print("\n📥 BORROWING BOOK")
book1.borrow()

# Display updated information
print("\n📚 UPDATED LIBRARY")
book1.display_info()

# Return the book
print("\n📤 RETURNING BOOK")
book1.return_book()

# Final information
print("\n📚 FINAL LIBRARY")
book1.display_info()
