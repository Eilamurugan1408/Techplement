import json
import os

class ContactManagerCLI:
    def __init__(self):
        self.contacts_file = "contacts.json"
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        """Load contacts from file"""
        try:
            if os.path.exists(self.contacts_file):
                with open(self.contacts_file, 'r') as file:
                    return json.load(file)
            return {}
        except Exception as e:
            print(f"Error loading contacts: {e}")
            return {}
    
    def save_contacts(self):
        """Save contacts to file"""
        try:
            with open(self.contacts_file, 'w') as file:
                json.dump(self.contacts, file, indent=2)
            print("Contacts saved successfully!")
        except Exception as e:
            print(f"Error saving contacts: {e}")
    
    def add_contact(self):
        """Add a new contact"""
        print("\n=== ADD NEW CONTACT ===")
        name = input("Enter name: ").strip()
        
        if not name:
            print("Error: Name cannot be empty!")
            return
        
        if name.lower() in [contact.lower() for contact in self.contacts.keys()]:
            print("Error: Contact with this name already exists!")
            return
        
        phone = input("Enter phone: ").strip()
        if not phone:
            print("Error: Phone cannot be empty!")
            return
        
        email = input("Enter email: ").strip()
        if not email or "@" not in email:
            print("Error: Please enter a valid email!")
            return
        
        self.contacts[name] = {
            "phone": phone,
            "email": email
        }
        
        self.save_contacts()
        print(f"Contact '{name}' added successfully!")
    
    def search_contact(self):
        """Search for contacts by name"""
        print("\n=== SEARCH CONTACTS ===")
        search_term = input("Enter name to search: ").strip().lower()
        
        if not search_term:
            print("Error: Please enter a search term!")
            return
        
        found_contacts = []
        for name, info in self.contacts.items():
            if search_term in name.lower():
                found_contacts.append((name, info))
        
        if found_contacts:
            print(f"\nFound {len(found_contacts)} contact(s):")
            print("-" * 50)
            for name, info in found_contacts:
                print(f"Name: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print("-" * 50)
        else:
            print("No contacts found!")
    
    def update_contact(self):
        """Update existing contact"""
        print("\n=== UPDATE CONTACT ===")
        name = input("Enter name of contact to update: ").strip()
        
        if not name:
            print("Error: Name cannot be empty!")
            return
        
        if name not in self.contacts:
            print("Error: Contact not found!")
            return
        
        print(f"\nCurrent details for '{name}':")
        print(f"Phone: {self.contacts[name]['phone']}")
        print(f"Email: {self.contacts[name]['email']}")
        
        new_phone = input(f"Enter new phone (current: {self.contacts[name]['phone']}): ").strip()
        new_email = input(f"Enter new email (current: {self.contacts[name]['email']}): ").strip()
        
        if new_phone:
            self.contacts[name]["phone"] = new_phone
        if new_email and "@" in new_email:
            self.contacts[name]["email"] = new_email
        elif new_email:
            print("Warning: Invalid email format, keeping old email")
        
        self.save_contacts()
        print(f"Contact '{name}' updated successfully!")
    
    def delete_contact(self):
        """Delete a contact"""
        print("\n=== DELETE CONTACT ===")
        name = input("Enter name of contact to delete: ").strip()
        
        if not name:
            print("Error: Name cannot be empty!")
            return
        
        if name not in self.contacts:
            print("Error: Contact not found!")
            return
        
        # Show contact details before deletion
        print(f"\nContact to delete:")
        print(f"Name: {name}")
        print(f"Phone: {self.contacts[name]['phone']}")
        print(f"Email: {self.contacts[name]['email']}")
        
        confirm = input("\nAre you sure you want to delete this contact? (yes/no): ").strip().lower()
        
        if confirm in ['yes', 'y']:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact '{name}' deleted successfully!")
        else:
            print("Deletion cancelled.")
    
    def list_all_contacts(self):
        """Display all contacts"""
        print("\n=== ALL CONTACTS ===")
        
        if not self.contacts:
            print("No contacts found!")
            return
        
        print(f"Total contacts: {len(self.contacts)}")
        print("-" * 50)
        
        for name in sorted(self.contacts.keys()):
            info = self.contacts[name]
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("-" * 50)
    
    def show_menu(self):
        """Display main menu"""
        print("\n" + "="*40)
        print("    CONTACT MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List All Contacts")
        print("6. Exit")
        print("-"*40)
    
    def run(self):
        """Main program loop"""
        print("Welcome to Contact Management System!")
        
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.search_contact()
            elif choice == '3':
                self.update_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                self.list_all_contacts()
            elif choice == '6':
                print("\nThank you for using Contact Management System!")
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1-6.")
            
            # Wait for user to press Enter before showing menu again
            input("\nPress Enter to continue...")

def main():
    contact_manager = ContactManagerCLI()
    contact_manager.run()

if __name__ == "__main__":
    main()