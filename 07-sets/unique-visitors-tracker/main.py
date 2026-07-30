# ---------- CONSTANTS -----------
visitors = set()

# ---------- MAIN PROGRAM ----------

while True:
    print("\n" + "=" * 40)
    print("Unique Visitors Tracker".center(40))
    print("=" * 40)

    # ----------- MENU -----------

    print("1. Add Visitor")
    print("2. View Visitors")
    print("3. Check Visitor")
    print("4. Remove Visitor")
    print("5. Visitors Count")
    print("6. Exit")

    try:
        user_selection = int(input("=> ").strip())
    except ValueError:
        print("Just numbers!")
    else:
        if user_selection == 1:
            print(" Add Visitor ".center(40, "-"))
            add_visitor = input("Visitor Name: ").strip().title()
            if add_visitor in visitors:
                print("This visitor already exists.")
            elif add_visitor:
                visitors.add(add_visitor)
                print(f'"{add_visitor}" added successfully.')
            else:
                print("Empty Name!")
        elif user_selection == 2:
            print(" View Visitors ".center(40, "-"))

            if visitors:
                for index, visitor in enumerate(sorted(visitors)):
                    print(f"{index + 1}. {visitor}")
            else:
                print("No visitors yet.")

        elif user_selection == 3:
            print(" Check Visitor ".center(40, "-"))
            check_visitor = input("Visitor Name: ").strip().title()
            if check_visitor:
                if check_visitor in visitors:
                    print("Visitor found.")
                else:
                    print("Visitor not found.")
            else:
                print("Empty Name!")
        elif user_selection == 4:
            print(" Remove Visitor ".center(40, "-"))
            remove_visitor = input("Visitor Name: ").strip().title()
            if remove_visitor:
                if remove_visitor in visitors:
                    visitors.discard(remove_visitor)
                    print(f'"{remove_visitor}" deleted successfully.')
                else:
                    print("Visitor not found.")
            else:
                print("Empty Name!")
        elif user_selection == 5:
            print(" Visitors Count ".center(40, "-"))
            print(f"Total Visitors: {len(visitors)}")
        elif user_selection == 6:
            print("Goodbye:(")
            break
        else:
            print("Select The Correct Number!")
