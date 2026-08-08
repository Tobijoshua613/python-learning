# 🛒 Shopping Cart
# Python Practice Project

cart = []


def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: ₦"))
    quantity = int(input("Enter quantity: "))

    item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    cart.append(item)
    print("✅ Item added to cart!")


def show_cart():
    if not cart:
        print("🛒 Your cart is empty.")
        return

    print("\n🛒 YOUR SHOPPING CART")
    print("-" * 40)

    total = 0

    for item in cart:
        item_total = item["price"] * item["quantity"]
        total += item_total

        print(
            f"{item['name']} | "
            f"₦{item['price']:.2f} × "
            f"{item['quantity']} = "
            f"₦{item_total:.2f}"
        )

    print("-" * 40)
    print(f"💰 TOTAL: ₦{total:.2f}")


def main():
    while True:
        print("\n===== 🛒 SHOPPING CART =====")
        print("1. Add item")
        print("2. View cart")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_item()

        elif choice == "2":
            show_cart()

        elif choice == "3":
            print("👋 Thank you for shopping!")
            break

        else:
            print("❌ Invalid choice. Try again.")


main()
