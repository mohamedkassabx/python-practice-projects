# ---------- CONSTANTS -----------
students = (
    ("Ali", 20, 95),
    ("Sara", 21, 88),
    ("Omar", 19, 91),
    ("Mohamed", 21, 100),
    )


# ---------- MAIN PROGRAM ----------

while True:
    print("\n" + "=" * 40)
    print("Student Records Viewer".center(40))
    print("=" * 40)

    # ----------- MENU -----------

    print("1. View All Students")
    print("2. Search Student")
    print("3. View Students Count")
    print("4. Exit")

    try:
        user_selection = int(input("=> ").strip())
    except ValueError:
        print("Just numbers!")
    else:
        if user_selection == 1:
            # ---------- VIEW ALL STUDENTS ----------

            print("\n" + " StudentS ".center(40, "-"))
            for index, (name, age, grade) in enumerate(students):
                print(f"{index + 1}.")
                print(name)
                print(f"Age: {age}")
                print(f"Grade: {grade}" + "\n")

        elif user_selection == 2:
            # ---------- SEARCH STUDENT ----------

            print("\n" + " Search Student ".center(40, "-"))
            student_name = input("Student Name: ").strip().title()
            found = False
            for index, (name, age, grade) in enumerate(students):
                if student_name == name:
                    print(f"{name} was founded.")
                    print(f"student number: {index + 1}")
                    print(f"Age: {age}")
                    print(f"Grade: {grade}" + "\n")
                    found = True
                    break
            if not found:
                print(f"{student_name} not founded.")

        elif user_selection == 3:
            # ---------- STUDENTS COUNT ----------

            print("\n" + " View Students Count ".center(40, "-"))
            print(f"Total Students: {len(students)}")

        elif user_selection == 4:
            # ---------- EXIT ----------

            print("Goodbye :)")
            break
        else:
            print("Select The Correct Number!")
