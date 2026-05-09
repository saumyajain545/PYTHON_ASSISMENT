# Contact Management System using Dictionary

# Empty dictionary to store contacts
contacts = {}

while True:
    # Display menu
    print("\n1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    # Take user choice
    choice = int(input("Enter your choice: "))

    # Add contact
    if choice == 1:
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")

        contacts[name] = number
        print("Contact Added Successfully")

    # Update contact
    elif choice == 2:
        name = input("Enter contact name to update: ")

        if name in contacts:
            number = input("Enter new phone number: ")
            contacts[name] = number
            print("Contact Updated Successfully")
        else:
            print("Contact Not Found")

    # Search contact
    elif choice == 3:
        name = input("Enter contact name to search: ")

        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact Not Found")

    # Delete contact
    elif choice == 4:
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully")
        else:
            print("Contact Not Found")

    # Exit program
    elif choice == 5:
        print("Exiting Program...")
        break

    # Invalid choice
    else:
        print("Invalid Choice")

'''
output
1. Add Contact
2. Update Contact
3. Search Contact
4. Delete Contact
5. Exit

Enter your choice: 1
Enter contact name: Aman
Enter phone number: 9876543210

Contact Added Successfully

Enter your choice: 3
Enter contact name to search: Aman

Phone Number: 9876543210
'''
