phone_book = {}

while True:
    print("\n--- Phone Book Menu ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. View all contacts")
    print("5. Exit")

    choice = input("Enter your choice (1–5): ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phone_book[name] = number
        print(f"Added {name} to contacts.")

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in phone_book:
            print(f"{name}'s number is {phone_book[name]}")
        else:
            print(f"{name} not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in phone_book:
            del phone_book[name]
            print(f"{name} deleted from contacts.")
        else:
            print(f"{name} not found.")

    elif choice == "4":
        if phone_book:
            print("\nContacts:")
            for name, number in phone_book.items():
                print(f"{name}: {number}")
        else:
            print("Phone book is empty.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1–5.")
