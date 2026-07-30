# --------- STUDENT DATA ---------

def get_student_data():
    first_name = input("First name: ").strip().title()
    last_name = input("Last name: ").strip().title()
    math = input("Math(0-100): ").strip()
    python = input("Python(0-100): ").strip()
    ai = input("AI(0-100): ").strip()
    if first_name and last_name and math and python and ai:
        try:
            math = int(math)
            python = int(python)
            ai = int(ai)
        except ValueError:
            print("Grades take only numbers!")
        else:
            if 0 <= math <= 100 and 0 <= python <= 100 and 0 <= ai <= 100:
                return f"{first_name} {last_name}", math, python, ai
            else:
                print("Grades must be between 0 and 100")
    else:
        print("Empty field!")


# --------- GRADES ---------


def averages(math, python, ai):
    average = (math + python + ai) / 3
    return average


# --------- ASSESSMENTS ---------


def grade(math, python, ai):
    average = averages(math, python, ai)
    if 0 <= average < 60:
        return "F"
    elif average < 70:
        return "D"
    elif average < 80:
        return "C"
    elif average < 90:
        return "B"
    elif average <= 100:
        return "A"


# --------- MAIN FUNCTION ---------


def main():
    student_data = get_student_data()

    if student_data is None:
        return

    full_name, math, python, ai = student_data

    print("=" * 40)
    print("Student Report".center(40))
    print("=" * 40 + "\n")
    print("Name".ljust(10) + f": {full_name}")
    print("Math".ljust(10) + f": {math}")
    print("Python".ljust(10) + f": {python}")
    print("AI".ljust(10) + f": {ai}" + "\n")
    print("Average".ljust(10) + f": {averages(math, python, ai):.2f}")
    print("Grade".ljust(10) + f": {grade(math, python, ai)}")


main()
