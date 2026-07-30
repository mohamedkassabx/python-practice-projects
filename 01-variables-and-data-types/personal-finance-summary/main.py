# ------- personal information -------
print("\n" + " Your Information ".center(40, "-"))
full_name = input("Full Name".ljust(24) + ": ").strip().title()
age = int(input("Age ".ljust(24) + ": ").strip())
job = input("Job ".ljust(24) + ": ").strip()
currency = input("Currency ".ljust(24) + ": ").strip()

# ------- income information -------
print("\n" + "Income Information".center(50, "-"))
monthly_income = float(input("Monthly Income ".ljust(24) + ": ").strip())
additional_income = float(input("Additional Income ".ljust(24) + ": ").strip())

# ------- expenses information -------
print("\n" + "Expenses Information".center(50, "-"))
rent = float(input("Rent / Housing Cost ".ljust(24) + ": ").strip())
food = float(input("Food Expenses ".ljust(24) + ": ").strip())
transportation = float(input("Transportation Expenses ".ljust(24) + ": ").strip())
entertainment = float(input("Entertainment Expenses ".ljust(24) + ": ").strip())
other = float(input("Other Expenses ".ljust(24) + ": ").strip())

# ---------- calculations ------------
total_income = monthly_income + additional_income
total_expenses = rent + food + transportation + entertainment + other
remaining = total_income - total_expenses
spent_percentage = (total_expenses / total_income) * 100

# -------- print informations --------

print("\n" + "=" * 50)
print(" Personal Finance Summary ".center(50, "="))
print("=" * 50 + "\n")

print("Name".ljust(24) + f": {full_name}")
print("Age".ljust(24) + f": {age:d}" + "\n")

print("- Income")
print("Monthly Income".ljust(24) + f": {monthly_income:.2f} {currency}")
print("Additional Income".ljust(24) + f": {additional_income:.2f} {currency}")
print("Total Income".ljust(24) + f": {total_income:.2f} {currency}" + "\n")

print("- Expenses")
print("Housing".ljust(24) + f": {rent:.2f} {currency}")
print("Food".ljust(24) + f": {food:.2f} {currency}")
print("Transportation".ljust(24) + f": {transportation:.2f} {currency}")
print("Entertainment".ljust(24) + f": {entertainment:.2f} {currency}")
print("Other".ljust(24) + f": {other:.2f} {currency}")
print("Total Expenses".ljust(24) + f": {total_expenses:.2f} {currency}" + "\n")

print("- Summary")
print("Remaining Balance".ljust(24) + f": {remaining:.2f} {currency}")
print("Spending Percentage".ljust(24) + f": {spent_percentage:.1f}%" + "\n")
