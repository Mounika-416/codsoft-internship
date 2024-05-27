import json

# Define the contact list file name

CONTACT_FILE = 'contacts.json'

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    store_name = input("Enter store name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts.append({
        'store_name': store_name,
        'phone_number': phone_number,
        'email': email,
        'address': address
    })
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['store_name']} - {contact['phone_number']}")

# Search for a contact by name or phone number
def search_contact():
    query = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if query in contact['store_name'] or query in contact['phone_number']]
    if results:
        for contact in results:
            print(f"{contact['store_name']} - {contact['phone_number']} - {contact['email']} - {contact['address']}")
    else:
        print("No contacts found.")

# Update an existing contact
def update_contact():
    search_query = input("Enter the name or phone number of the contact to update: ")
    for contact in contacts:
        if search_query in contact['store_name'] or search_query in contact['phone_number']:
            print(f"Current details: {contact}")
            contact['store_name'] = input(f"Enter new store name (current: {contact['store_name']}): ") or contact['store_name']
            contact['phone_number'] = input(f"Enter new phone number (current: {contact['phone_number']}): ") or contact['phone_number']
            contact['email'] = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address (current: {contact['address']}): ") or contact['address']
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Delete a contact
def delete_contact():
    search_query = input("Enter the name or phone number of the contact to delete: ")
    for contact in contacts:
        if search_query in contact['store_name'] or search_query in contact['phone_number']:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

# Main menu
def main():
    global contacts
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

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
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

