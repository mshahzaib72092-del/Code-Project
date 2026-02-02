# /////////CONTACT Management SYSTEM//////////

contacts = {}

def add_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("❌ Contact already exists")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    print("✅ Contact added successfully")

def view_contacts():
    if not contacts:
        print("📭 No contacts found")
        return
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"✅ Found → Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("❌ Contact not found")

def update_contact():
    name = input("Enter name to update: ")
    if name not in contacts:
        print("❌ Contact not found")
        return
    phone = input("Enter new phone number: ")
    email = input("Enter new email: ")
    contacts[name] = {"phone": phone, "email": email}
    print("✅ Contact updated successfully")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("✅ Contact deleted")
    else:
        print("❌ Contact not found")

def menu():
    while True:
        print("""
📇 Contact Management System
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
""")
        choice = input("Choose option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Program Exit")
            break
        else:
            print("❌ Invalid choice")

menu()

# //////////RUN PROGRAM//////////

 python contact_management.py








