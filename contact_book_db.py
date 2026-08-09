# 📞 Contact Book with SQLite
# Database-powered Python project

import sqlite3

DATABASE = "contacts.db"


def connect_database():
    return sqlite3.connect(DATABASE)


def create_table():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT
    )
    """)

    connection.commit()
    connection.close()


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO contacts (name, phone, email)
        VALUES (?, ?, ?)
        """,
        (name, phone, email)
    )

    connection.commit()
    connection.close()

    print("✅ Contact saved!")


def view_contacts():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()

    connection.close()

    if not contacts:
        print("📭 No contacts found.")
        return

    print("\n📞 CONTACTS")
    print("-" * 50)

    for contact in contacts:
        print(
            f"ID: {contact[0]} | "
            f"Name: {contact[1]} | "
            f"Phone: {contact[2]} | "
            f"Email: {contact[3]}"
        )


def search_contact():
    name = input("Enter name to search: ")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM contacts WHERE name LIKE ?",
        (f"%{name}%",)
    )

    contacts = cursor.fetchall()
    connection.close()

    if not contacts:
        print("❌ No matching contact found.")
        return

    print("\n🔎 SEARCH RESULTS")
    print("-" * 50)

    for contact in contacts:
        print(
            f"ID: {contact[0]} | "
            f"Name: {contact[1]} | "
            f"Phone: {contact[2]} | "
            f"Email: {contact[3]}"
        )


def delete_contact():
    view_contacts()

    try:
        contact_id = int(input("\nEnter contact ID to delete: "))
    except ValueError:
        print("❌ Please enter a valid ID.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM contacts WHERE id = ?",
        (contact_id,)
    )

    connection.commit()
    connection.close()

    print("🗑️ Contact deleted!")


def main():
    create_table()

    while True:
        print("\n===== 📞 CONTACT BOOK =====")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option.")


main()
