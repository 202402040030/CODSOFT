import re

contacts = []

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("❗This field cannot be empty.")

def add_contact():
    store_name = input_non_empty("Enter store name: ")

    while True:
        phone = input("Enter phone number (10 digits): ").strip()
        if validate_phone(phone):
            break
        print("❗Invalid phone number. Must be 10 digits.")

    while True:
        email = input("Enter email address: ").strip()
        if validate_email(email):
            break
        print("❗Invalid email format.")

    address = input_non_empty("Enter address: ")

    # Check if phone already exists
    for contact in contacts:
        if contact['phone'] == phone:
            print("❌ Contact with this phone number already exists.\n")
            return

    contact = {
        "store_name": store_name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("✅ Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("📭 No contacts to display.\n")
        return
    print("\n📇 Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['store_name']} | {contact['phone']}")
    print()

def search_contact():
    query = input("🔍 Enter name or phone to search: ").lower()
    found_contacts = []

    for contact in contacts:
        if query in contact['store_name'].lower() or query in contact['phone']:
            found_contacts.append(contact)

    if found_contacts:
        print(f"\n🔎 Found {len(found_contacts)} contact(s):")
        for contact in found_contacts:
            print("-" * 40)
            print(f"Store Name: {contact['store_name']}")
            print(f"Phone     : {contact['phone']}")
            print(f"Email     : {contact['email']}")
            print(f"Address   : {contact['address']}")
        print("-" * 40 + "\n")
    else:
        print("❌ No matching contact found.\n")

def update_contact():
    identifier = input("✏️ Enter phone number or store name to update: ").strip().lower()

    matches = []

    for contact in contacts:
        if identifier == contact['phone'] or identifier in contact['store_name'].lower():
            matches.append(contact)

    if not matches:
        print("❌ No matching contact found.\n")
        return

    if len(matches) > 1:
        print(f"🔍 Found {len(matches)} contacts:")
        for idx, contact in enumerate(matches, start=1):
            print(f"{idx}. {contact['store_name']} | {contact['phone']} | {contact['email']}")
        try:
            choice = int(input("Select the contact number to update: "))
            if 1 <= choice <= len(matches):
                contact = matches[choice - 1]
            else:
                print("❗Invalid choice.\n")
                return
        except ValueError:
            print("❗Invalid input.\n")
            return
    else:
        contact = matches[0]

    print("✏️ Leave blank to keep current value.")
    new_name = input(f"New store name ({contact['store_name']}): ").strip()
    new_phone = input(f"New phone ({contact['phone']}): ").strip()
    new_email = input(f"New email ({contact['email']}): ").strip()
    new_address = input(f"New address ({contact['address']}): ").strip()

    if new_name:
        contact['store_name'] = new_name
    if new_phone:
        if validate_phone(new_phone):
            # Check if phone is already used by another contact
            for c in contacts:
                if c['phone'] == new_phone and c != contact:
                    print("❌ Phone number already in use by another contact. Not updated.")
                    break
            else:
                contact['phone'] = new_phone
        else:
            print("❗Invalid phone number. Keeping old value.")
    if new_email:
        if validate_email(new_email):
            contact['email'] = new_email
        else:
            print("❗Invalid email. Keeping old value.")
    if new_address:
        contact['address'] = new_address

    print("✅ Contact updated successfully!\n")


def delete_contact():
    identifier = input("🗑️ Enter phone number or store name to delete: ").strip().lower()

    matches = []

    for contact in contacts:
        if identifier == contact['phone'] or identifier in contact['store_name'].lower():
            matches.append(contact)

    if not matches:
        print("❌ No matching contact found.\n")
        return

    if len(matches) > 1:
        print(f"🔍 Found {len(matches)} contacts:")
        for idx, contact in enumerate(matches, start=1):
            print(f"{idx}. {contact['store_name']} | {contact['phone']} | {contact['email']}")
        try:
            choice = int(input("Select the contact number to delete: "))
            if 1 <= choice <= len(matches):
                contact = matches[choice - 1]
            else:
                print("❗Invalid choice.\n")
                return
        except ValueError:
            print("❗Invalid input.\n")
            return
    else:
        contact = matches[0]

    confirm = input(f"Are you sure you want to delete '{contact['store_name']}'? (y/n): ").strip().lower()
    if confirm == 'y':
        contacts.remove(contact)
        print("✅ Contact deleted successfully!\n")
    else:
        print("❌ Deletion cancelled.\n")

def main():
    while True:
        print("📱 Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()
        print()

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
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
