# 📦 Inventory Manager

inventory = {
    "Laptop": 5,
    "Phone": 10,
    "Keyboard": 7,
    "Mouse": 12
}

def show_inventory():
    print("\n=== INVENTORY ===")
    for item, quantity in inventory.items():
        print(item, ":", quantity)

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(quantity, item, "added.")

def remove_item(item, quantity):
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity
        print(quantity, item, "removed.")
    else:
        print("Not enough stock available.")

show_inventory()

add_item("Laptop", 2)
remove_item("Phone", 3)

show_inventory()
