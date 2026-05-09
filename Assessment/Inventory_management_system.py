# Inventory management system

inventory = {}

while True:
    print("\n1. Add Product")
    print("2. Update Quantity")
    print("3. Search Product")
    print("4. Low Stock Items")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        inventory[name] = qty

    elif choice == 2:
        name = input("Enter product name: ")
        qty = int(input("Enter new quantity: "))
        inventory[name] = qty

    elif choice == 3:
        name = input("Enter product name: ")
        print("Quantity:", inventory.get(name, "Product Not Found"))

    elif choice == 4:
        print("Low Stock Items:")
        for item, qty in inventory.items():
            if qty < 5:
                print(item, qty)

    elif choice == 5:
        break


#output
#Low Stock Items:
#Pen 2
#Notebook 3
