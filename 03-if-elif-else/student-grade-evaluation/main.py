print("=" * 50)
print(" Student Grade Evaluation ".center(50, "="))
print("=" * 50)

# ------------ INPUTS ------------
full_name = input("Full Name".ljust(22) + ": ").strip().title()
age = int(input("Age".ljust(22) + ": ").strip())
university = input("University".ljust(22) + ": ").strip()
gpa = float(input("GPA (0.0 - 4.0)".ljust(22) + ": ").strip())
att_percentage = int(input("Attendance Percentage(0 - 100)".ljust(22) + ": ").strip())
completed_projects = int(input("Completed Projects".ljust(22) + ": ").strip())

# ------------ CONDITIONS ------------
academic_grade = ""
attendance = ""
projects = ""

# ---- Academic Grade ----
if gpa < 1.5:
    academic_grade = "F"
elif 1.5 <= gpa < 2:
    academic_grade = "D"
elif 2 <= gpa < 3:
    academic_grade = "C"
elif 3 <= gpa < 3.5:
    academic_grade = "B"
elif 3.5 <= gpa <= 4:
    academic_grade = "A"
else:
    academic_grade = "Please write the GPA(0.0 - 4.0) correct!"

# ---- Attendance ----
if att_percentage < 60:
    attendance = "Not Accepted"
elif 60 <= att_percentage <= 100:
    attendance = "Accepted"
else:
    attendance = "Please write the Attendance Percentage correct!"

# ---- Projects ----
if 0 <= completed_projects <= 3:
    projects = "Bad"
elif 3 < completed_projects <= 6:
    projects = "Good"
elif completed_projects > 6:
    projects = "Perfect"
else:
    projects = "Please write the number of Completed Projects correct!"


# ------------ DISPLAY ------------
print("-" * 50)
print("- Student Information")
print("Name".ljust(22) + f": {full_name:s}")
print("Age".ljust(22) + f": {age:d}")
print("University".ljust(22) + f": {university:s}")
print("GPA".ljust(22) + f": {gpa:.1f}")
print("Attendance Percentage".ljust(22) + f": {att_percentage:d}%")
print("Completed Projects".ljust(22) + f": {completed_projects:d}")

print("\n" + "- Status")
print("Academic Status".ljust(22) + f": {academic_grade}")
print("Attendance Status".ljust(22) + f": {attendance}")
print("Project Status".ljust(22) + f": {projects}")
