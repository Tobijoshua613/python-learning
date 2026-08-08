# Contact Book

contacts = {}


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone
    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contacts ---")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")


def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")


while True:
    print("\n=== CONTACT BOOK ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
