# contact_manager.py
from input_validation import is_valid_phone, is_valid_email

contacts = {}

def add_contact():
    unique_id = input("Enter a unique identifier (Phone or Email): ")
    if unique_id in contacts:
        print("This contact already exists!")
        return
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    if not is_valid_phone(phone):
        print("Invalid phone number format. Use XXX-XXX-XXXX format.")
        return
    if not is_valid_email(email):
        print("Invalid email format.")
        return
    additional_info = input("Enter additional information (optional): ")
    contacts[unique_id] = {"Name": name, "Phone": phone, "Email": email, "Additional Info": additional_info}
    print("Contact added successfully!")

def edit_contact():
    unique_id = input("Enter the unique identifier of the contact to edit: ")
    if unique_id not in contacts:
        print("Contact not found!")
        return
    print(f"Editing contact: {contacts[unique_id]}")
    name = input("Enter new name (leave blank to keep current): ")
    phone = input("Enter new phone number (leave blank to keep current): ")
    email = input("Enter new email (leave blank to keep current): ")
    additional_info = input("Enter new additional info (leave blank to keep current): ")

    if name:
        contacts[unique_id]['Name'] = name
    if phone and is_valid_phone(phone):
        contacts[unique_id]['Phone'] = phone
    if email and is_valid_email(email):
        contacts[unique_id]['Email'] = email
    if additional_info:
        contacts[unique_id]['Additional Info'] = additional_info
    print("Contact updated successfully!")

def delete_contact():
    unique_id = input("Enter the unique identifier of the contact to delete: ")
    if unique_id in contacts:
        del contacts[unique_id]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def search_contact():
    unique_id = input("Enter the unique identifier to search: ")
    if unique_id in contacts:
        print(f"Contact found: {contacts[unique_id]}")
    else:
        print("Contact not found!")

def display_all_contacts():
    if contacts:
        for unique_id, info in contacts.items():
            print(f"ID: {unique_id}, Info: {info}")
    else:
        print("No contacts available!")
