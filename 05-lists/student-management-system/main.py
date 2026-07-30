# ---------- CONSTANTS -----------
names = []
ages = []
grades = []


# ---------- MAIN PROGRAM ----------

while True:
    print("\n" + "=" * 40)
    print("Student Management System".center(40))
    print("=" * 40)

    # ----------- MENU -----------

    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Search Student")
    print("5. Exit")

    try:
        user_selection = int(input("=> ").strip())
    except ValueError:
        print("Just numbers!")
    else:
        if user_selection == 1:
            # ---------- ADD STUDENT ----------

            print("\n" + " Add Student ".center(40, "-"))
            student_name = input("Student Name: ").strip().title()

            try:
                student_age = int(input("Student Age: ").strip())
                student_grade = int(input("Student Grade: ").strip())
            except ValueError:
                print('"Student Age & Student Grade" must be a number!')
            else:
                if student_name and student_age >= 0  and student_grade >= 0:
                    names.append(student_name)
                    ages.append(student_age)
                    grades.append(student_grade)
                    print(f"{student_name} added successfully.")
                else:
                    print("There's field empty!")
        elif user_selection == 2:
            # ---------- VIEW STUDENTS ----------

            print("\n" + " Students ".center(40, "-"))
            if names:
                for index, student in enumerate(names):
                    print(f"{index + 1}. {student}")
                    print(f"Age: {ages[index]}")
                    print(f"Grade: {grades[index]}" + "\n")
            else:
                print("There's no students for now.")
        elif user_selection == 3:
            # ---------- REMOVE STUDENT ----------

            print("\n" + " Remove Student ".center(40, "-"))
            if names:
                try:
                    student_number = int(input("Select the student number: ").strip())
                except ValueError:
                    print("Just numbers!")
                else:
                    if 0 < student_number <= len(names):
                        print(f'"{names[student_number - 1]}" was removed.')
                        names.pop(student_number - 1)
                        ages.pop(student_number - 1)
                        grades.pop(student_number - 1)
                    else:
                        print("Select a correct number!")
            else:
                print("There's no students for now.")

        elif user_selection == 4:
            # ---------- SEARCH STUDENT ----------

            print("\n" + " Search Student ".center(40, "-"))
            search_student = input("Student Name: ").strip().title()
            if search_student in names:
                student_id = names.index(search_student)
                print(f"{search_student} was founded.")
                print(f"student number: {student_id + 1}")
                print(f"Age: {ages[student_id]}")
                print(f"Grade: {grades[student_id]}" + "\n")
            else:
                print(f"{search_student} not founded.")

        elif user_selection == 5:
            # ---------- EXIT ----------

            print("Goodbye :)")
            break
        else:
            print("Select The Correct Number!")
