while True:
    print("\n" + "=" * 40)
    print("Student Records".center(40))
    print("=" * 40)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Students Count")
    print("5. Exit")

    user_selector = input("=> ").strip()
    try:
        user_selector = int(user_selector)
    except ValueError:
        print("Only numbers!")
    else:
        # -------- Add Student --------
        if user_selector == 1:
            print(" Add Student ".center(40, "-"))
            name = input("Name: ").strip().title()
            age = input("Age: ").strip()
            grade = input("Grade(0-100): ").strip()
            try:
                age = int(age)
                grade = float(grade)
            except ValueError:
                print("Only numbers!")
            else:
                if name and 0 < age and 0 <= grade <= 100:
                    with open("students.txt", "a") as students:
                        students.write(f"{name},{age},{grade}\n")
                        print(f'"{name}" added successfully.')
                else:
                    print("Check the fields again!")
        # -------- View Students --------

        elif user_selector == 2:
            print(" View Students ".center(40, "-"))
            try:
                with open("students.txt", "r") as students:
                    for index, student in enumerate(students):
                        name, age, grade = student.strip().split(",")
                        print(f"{index + 1}.")
                        print("Name".ljust(5) + f": {name}")
                        print("Age".ljust(5) + f": {age}")
                        print("Grade".ljust(5) + f": {grade}")
            except FileNotFoundError:
                print("No students for now.")
        # -------- Search Student --------

        elif user_selector == 3:
            print(" Search Student ".center(40, "-"))
            try:
                with open("students.txt", "r") as students:
                    search_name = input("Studend name: ").strip().title()
                    if search_name:
                        found = False
                        
                        for student in students:
                            name, age, grade = student.strip().split(",")

                            if search_name == name:
                                print("\n" + "Name".ljust(5) + f": {name}")
                                print("Age".ljust(5) + f": {age}")
                                print("Grade".ljust(5) + f": {grade}")
                                found = True
                        if not found:
                            print(f'"{search_name}" not found.')
                    else:
                        print("Empty field!")
            except FileNotFoundError:
                print("No students for now.")
        # -------- Students Count --------

        elif user_selector == 4:
            print(" Students Count ".center(40, "-"))
            try:
                with open("students.txt", "r") as students:
                    print(f"Total students = {len(students.readlines())}")
            except FileNotFoundError:
                print("No students for now.")
        # -------- EXIT --------

        elif user_selector == 5:
            print("Goodbye :)")
            break
        else:
            print("Wrong number!")
