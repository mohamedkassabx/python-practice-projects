print("=" * 40)
print(" Username Generator ".center(40, "="))
print("=" * 40)

# ------------ INPUTS ------------
first_name = input("First Name".ljust(18) + ": ").strip()
last_name = input("Last Name".ljust(18) + ": ").strip()
birth_year = int(input("Birth Year".ljust(18) + ": ").strip())
fav_number = int(input("Favorite Number".ljust(18) + ": ").strip())

# ------------ GENERATOR ------------
print("\n" + " Suggested Usernames ".center(40, "-"))
print(f"1 - {first_name + last_name}")
print(f"2 - {first_name[0:3] + last_name[0] + str(birth_year)}")
print(f"3 - {first_name.capitalize() + str(birth_year)}")
print(f"4 - {last_name + str(fav_number)}")
print(f"5 - {first_name + str(fav_number) + last_name.upper()}")
print(f"6 - {first_name[0] + '_' + last_name}")

# ------------ NAME SUMMARY ------------
full_name = first_name + " " + last_name

print("\n" + " Full Nmae ".center(40, "-"))
print("Full Name".ljust(18) + f": {full_name}")
print("Name In Uppercase".ljust(18) + f": {full_name.upper()}")
print("Name In Lowercase".ljust(18) + f": {full_name.lower()}")
print("Name Length".ljust(18) + f": {len(full_name)}")
print("First Character".ljust(18) + f": {full_name[0]}")
print("Last Character".ljust(18) + f": {full_name[-1]}")
