contacts = []

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    print("\nAdd New Contact")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")

def view_contacts():
    print("\nContact List")
    if not contacts:
        print("No contacts available.")
        return
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact():
    print("\nSearch Contact")
    search = input("Enter Name or Phone Number to search: ")
    found = [c for c in contacts if search in c['name'] or search in c['phone']]
    if found:
        for contact in found:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")

def update_contact():
    print("\nUpdate Contact")
    search = input("Enter Name or Phone Number to update: ")
    for contact in contacts:
        if search in contact['name'] or search in contact['phone']:
            print("Enter new details (leave blank to keep existing values):")
            name = input(f"New Name ({contact['name']}): ") or contact['name']
            phone = input(f"New Phone ({contact['phone']}): ") or contact['phone']
            email = input(f"New Email ({contact['email']}): ") or contact['email']
            address = input(f"New Address ({contact['address']}): ") or contact['address']
            contact.update({"name": name, "phone": phone, "email": email, "address": address})
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    print("\nDelete Contact")
    search = input("Enter Name or Phone Number to delete: ")
    for i, contact in enumerate(contacts):
        if search in contact['name'] or search in contact['phone']:
            contacts.pop(i)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
