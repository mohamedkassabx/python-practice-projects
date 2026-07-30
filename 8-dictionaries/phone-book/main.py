# ---------- CONSTANTS -----------
contacts = {}

# ---------- MAIN PROGRAM ----------

while True:
    # ---------- MENU ----------
    print("=" * 40)
    print("Phone Book".center(40))
    print("=" * 40)

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Contacts Count")
    print("6. Exit")

    try:
        user_selector = int(input("=> ").strip())
    except ValueError:
        print("Just numbers!")
    else:
        # ---------- ADD CONTACT ----------
        
        if user_selector == 1:
            print(" Add Contact ".center(40, "-"))

            contact_name = input("Contact Name: ").strip().title()
            contact_number = input("Contact Number: ").strip()

            if contact_number and contact_name:
                try:
                    contact_number = int(contact_number)
                except ValueError:
                    print("Contact Number accept only numbers.")
                else:
                    if contact_name in contacts:
                        print(f'Contact name"{contact_name}" already exists.')
                    elif contact_number in contacts.values():
                        print(f'Contact number "{contact_number}" already exists.')
                    else:
                        contacts[contact_name] = contact_number
                        print(f'"{contact_name}" added successfully.')
            else:
                print("Empty field!")
        # ---------- VIEW CONTACT ----------

        elif user_selector == 2:
            print(" View Contacts ".center(40, "-"))
            if contacts:
                for index, contact in enumerate(contacts):
                    print(f"{index + 1}.")
                    print(f"Name: {contact}")
                    print(f"Phone: {contacts[contact]}", "\n")
            else:
                print("No contacts.")
        # ---------- SEARCH CONTACT ----------

        elif user_selector == 3:
            print(" Search Contact ".center(40, "-"))
            search_name = input("Contact Name: ").strip().title()
            if search_name in contacts:
                print(f"{search_name} : {contacts[search_name]}")
            else:
                print(f'"{search_name}" not found.')
        # ---------- REMOVE CONTACT ----------

        elif user_selector == 4:
            print(" Remove Contact ".center(40, "-"))
            remove_name = input("Contact Name: ").strip().title()
            if remove_name in contacts:
                contacts.pop(remove_name)
                print(f"{remove_name} deleted successfully.")
            else:
                print(f'"{remove_name}" not found.')
        # ---------- CONTACTS COUNT ----------

        elif user_selector == 5:
            print(" Contacts Count ".center(40, "-"))
            print(f"Total Contacts: {len(contacts)}")
        # ---------- EXIT ----------
        
        elif user_selector == 6:
            print("Goodbye:(")
            break
        else:
            print("Select The Correct Number!")

            
