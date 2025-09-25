# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View items")
    print("4. Exit")

def main():
    shopping_list = []  # start with an empty list

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':  # Add item
            item = input("Enter the item to add: ")
            shopping_list.append(item)  # add item to the list
            print(f"{item} has been added to your shopping list.")

        elif choice == '2':  # Remove item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from your shopping list.")
            else:
                print(f"{item} is not in your shopping list.")

        elif choice == '3':  # View items
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nYour shopping list:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")

        elif choice == '4':  # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
