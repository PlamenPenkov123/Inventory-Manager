import inventory

def menu():
    inventory.create_table()
    print("Welcome to the Inventory Management System")
    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Search Item")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            inventory.add_item(name, quantity, price)
            print("Item added successfully.")
        elif choice == '2':
            print("Items in inventory:")
            inventory.view_items()
        elif choice == '3':
            item_id = int(input("Enter item ID to update: "))
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory.update_item(item_id, quantity, price)
            print("Item updated successfully.")
        elif choice == '4':
            item_id = int(input("Enter item ID to delete: "))
            inventory.delete_item(item_id)
            print("Item deleted successfully.")
        elif choice == '5':
            name = input("Enter item name to search: ")
            inventory.search_item(name)
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()