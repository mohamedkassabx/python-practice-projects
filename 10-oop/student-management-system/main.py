class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("Name".ljust(5) + f": {self.name}")
        print("Age".ljust(5) + f": {self.age}")
        print("Grade".ljust(5) + f": {self.grade:.2f}" + "\n")

    def update_grade(self, new_grade):
        self.grade = new_grade


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        if self.students:
            for index, student in enumerate(self.students):
                print(f"{index + 1}.")
                student.display_info()
        else:
            print("No students for now.")

    def search_student(self, name):
        found = False
        for index, student in enumerate(self.students):
            if name == student.name:
                print(f"{index + 1}.")
                Student.display_info(student)
                found = True     
        if not found:
            print(f'"{name}" not found.')

    def remove_student(self, index):
        if 0 < index <= len(self.students):
            print(f'"{self.students[index - 1].name}" removed successfully.')
            self.students.pop(index - 1)
        else:
            print("Invalid student number!")

    def update_student_grade(self, index, new_grade):
        if 0 < index <= len(self.students):
            self.students[index - 1].update_grade(new_grade)
            print(f'"{self.students[index - 1].name}" grade updated')
        else:
            print("Invalid student number!")

    def students_count(self):
        return len(self.students)


# -------- MAIN FUNCTION --------


def main():

    studentmanager = StudentManager()
    while True:
        print("\n" + "=" * 40)
        print("Student Manager".center(40))
        print("=" * 40)

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Grade")
        print("5. Remove Student")
        print("6. Students Count")
        print("7. Exit")

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
                    if 0 < age and 0 <= grade <= 100:
                        student = Student(name, age, grade)
                        studentmanager.add_student(student)
                        print(f'"{name}" added successfully.')
                    else:
                        print("Check the age and grade again!")
            # -------- View Students --------

            elif user_selector == 2:
                print(" View Students ".center(40, "-"))
                studentmanager.view_students()
            # -------- Search Student --------

            elif user_selector == 3:
                print(" Search Student ".center(40, "-"))
                search_name = input("Studend name: ").strip().title()
                studentmanager.search_student(search_name)
            # -------- Update Grade --------

            elif user_selector == 4:
                print(" Update Grade ".center(40, "-"))
                student_number = input("Student number: ").strip()
                new_grade = input("New grade(0-100): ").strip()
                try:
                    student_number = int(student_number)
                    new_grade = float(new_grade)
                except ValueError:
                    print("Only numbers!")
                else:
                    if 0 <= new_grade <= 100:
                        studentmanager.update_student_grade(student_number, new_grade)
                    else:
                        print("Grade must be between 0 and 100!")
            # -------- Remove Student --------

            elif user_selector == 5:
                print(" Remove Student ".center(40, "-"))
                student_number = input("Student number: ").strip()
                try:
                    student_number = int(student_number)
                except ValueError:
                    print("Only numbers!")
                else:
                    studentmanager.remove_student(student_number)
            # -------- Students Count --------

            elif user_selector == 6:
                print(" Students Count ".center(40, "-"))
                print(f"Total students = {studentmanager.students_count()}")

            # -------- EXIT --------

            elif user_selector == 7:
                print("Goodbye :)")
                break
            else:
                print("Wrong number!")


main()
