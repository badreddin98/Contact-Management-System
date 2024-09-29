from contact_manager import contacts

def export_contacts():
    with open("contacts.txt", "w") as f:
        for unique_id, info in contacts.items():
            f.write(f"{unique_id}, {info}\n")
    print("Contacts exported successfully!")

def import_contacts():
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                unique_id, info = line.strip().split(", ", 1)
                contacts[unique_id] = eval(info)
        print("Contacts imported successfully!")
    except FileNotFoundError:
        print("No import file found!")
