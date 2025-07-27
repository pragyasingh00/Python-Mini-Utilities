import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("✅ Contact added.")

# Search contact by name or phone
def search_contact(contacts):
    query = input("Search by name or phone: ").lower()
    results = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]
    if results:
        for c in results:
            print(f"- {c['name']} | {c['phone']} | {c['email']}")
    else:
        print("⚠️ No contact found.")

# Update a contact
def update_contact(contacts):
    query = input("Enter name or phone to update: ").lower()
    for c in contacts:
        if query in c["name"].lower() or query in c["phone"]:
            print(f"Updating: {c}")
            c["name"] = input("New name (leave blank to keep current): ") or c["name"]
            c["phone"] = input("New phone (leave blank to keep current): ") or c["phone"]
            c["email"] = input("New email (leave blank to keep current): ") or c["email"]
            save_contacts(contacts)
            print("✅ Contact updated.")
            return
    print("⚠️ Contact not found.")

# Delete a contact
def delete_contact(contacts):
    query = input("Enter name or phone to delete: ").lower()
    for i, c in enumerate(contacts):
        if query in c["name"].lower() or query in c["phone"]:
            print(f"Deleting: {c}")
            del contacts[i]
            save_contacts(contacts)
            print("🗑️ Contact deleted.")
            return
    print("⚠️ Contact not found.")

# CLI Menu
def main():
    contacts = load_contacts()
    while True:
        print("\n📒 Contact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("👋 Exiting Contact Book. Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
