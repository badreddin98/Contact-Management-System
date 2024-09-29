from contact_manager import add_contact, edit_contact, delete_contact, search_contact, display_all_contacts
from file_operations import export_contacts, import_contacts

def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        match choice:
            case '1':
                add_contact()
            case '2':
                edit_contact()
            case '3':
                delete_contact()
            case '4':
                search_contact()
            case '5':
                display_all_contacts()
            case '6':
                export_contacts()
            case '7':
                import_contacts()
            case '8':
                print("Exiting Contact Management System. Goodbye!")
                break
            case _:
                print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
