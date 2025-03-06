#touch ~/project/contact_manager.py
def add_contact(contacts, name, phone, email):
    contacts[name] = {"phone": phone, "email": email} # contacts is a variable and [name is the dictionary] The square brackets in contacts[name] aren’t creating a list—they're used to access or assign a value in a dictionary by key. In this case, name is the key in the contacts dictionary, and using square brackets is the standard way to reference that key's value.
    print(f"Contact {name} added successfully.")

def remove_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} removed successfully.")
    else:
        print(f"Contact {name} not found.")

def display_contacts(contacts):
    if contacts:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("Contact list is empty.")

def main():
    contacts = {}
    favorite_contacts = set()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Add to Favorites")
        print("5. Display Favorites")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(contacts, name, phone, email)
        elif choice == "2":
            name = input("Enter name to remove: ")
            remove_contact(contacts, name)
        elif choice == "3":
            display_contacts(contacts)
        elif choice == "4":
            name = input("Enter name to add to favorites: ")
            if name in contacts:
                favorite_contacts.add(name)
                print(f"{name} added to favorites.")
            else:
                print(f"Contact {name} not found.")
        elif choice == "5":
            print("\nFavorite Contacts:")
            for name in favorite_contacts:
                print(name)
        elif choice == "6":
            print("Thank you for using Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


###############
what is happening here 
if __name__ == "__main__":
    main()

is a common Python idiom used to control the execution of code. Let’s break it down:

1. __name__:
Every Python module (or script) has a special built-in variable called __name__.
When you run a Python file directly (as a script), the __name__ variable is automatically set to "__main__".
If the file is imported as a module in another script, __name__ is set to the module's name (which is usually the filename without the .py).
2. if __name__ == "__main__"::
This checks whether the current file is being run directly (as the main program) or is being imported into another module.
If __name__ == "__main__", it means that the file is being run directly (not imported), so the code under this condition will execute.
3. main():
Typically, main() is a function defined elsewhere in the script that contains the main logic of the program.
If the file is being run directly, this function is called to start the program.
Purpose:
This pattern allows you to write code that can be reused as a module, but still allows the script to be executed independently. When run as a script, the program logic (main()) will run. But if the file is imported, main() won’t be called automatically.

Example:
def main():
    print("Hello, this is the main function!")

if __name__ == "__main__":
    main()
If you run this file directly, the output will be:
Hello, this is the main function!

If you import this file as a module in another script, nothing will happen unless you explicitly call main() because __name__ will not be "__main__".
Summary:
The if __name__ == "__main__": check ensures that certain code (like calling main()) only runs when the file is executed directly, not when it is imported as a module.

################

================== CONSOLE OUTPUT
Contact Manager
1. Add Contact
2. Remove Contact
3. Display Contacts
4. Add to Favorites
5. Display Favorites
6. Exit
Enter your choice (1-6): 1
Enter name: Alice
Enter phone number: 123-456-7890
Enter email: alice@example.com
Contact Alice added successfully.

Contact Manager
1. Add Contact
2. Remove Contact
3. Display Contacts
4. Add to Favorites
5. Display Favorites
6. Exit
Enter your choice (1-6): 1
Enter name: Bob
Enter phone number: 987-654-3210
Enter email: bob@example.com
Contact Bob added successfully.

Contact Manager
1. Add Contact
2. Remove Contact
3. Display Contacts
4. Add to Favorites
5. Display Favorites
6. Exit
Enter your choice (1-6): 3

Contact List:
Name: Alice, Phone: 123-456-7890, Email: alice@example.com
Name: Bob, Phone: 987-654-3210, Email: bob@example.com

Contact Manager
1. Add Contact
2. Remove Contact
3. Display Contacts
4. Add to Favorites
5. Display Favorites
6. Exit
Enter your choice (1-6): 4
Enter name to add to favorites: Alice
Alice added to favorites.

Contact Manager
1. Add Contact
2. Remove Contact
3. Display Contacts
4. Add to Favorites
5. Display Favorites
6. Exit
Enter your choice (1-6): 5

Favorite Contacts:
Alice

Contact Manager
1. Add Contact
2. Remove Contact
3. Display Contacts
4. Add to Favorites
5. Display Favorites
6. Exit
Enter your choice (1-6): 6
Thank you for using Contact Manager. Goodbye!



############# important to breaking the code down
def add_contact(contacts, name, phone, email):
    # Add the contact details into the contacts dictionary using 'name' as the key
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully.")

# Create an empty dictionary for contacts
contacts = {}

# Call the function with the correct types: the first argument is a dictionary.
add_contact(contacts, "jj", "2", "33")

# Print the contacts dictionary to see the stored data
print(contacts)

CONSOLE OUTPUT:
labex:project/ $ python test.py
Contact x added successfully.
{'x': {'phone': 'b', 'email': 'c'}}
