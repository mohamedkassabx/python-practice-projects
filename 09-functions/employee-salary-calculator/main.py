# ---------- INPUTS FUNCTION ----------


def get_employee_data():
    employee_name = input("Employee Name: ").strip().title()
    try:
        basic_salary = float(input("Basic Salary: ").strip())
        bonus = float(input("Bonus: ").strip())
        tax_percentage = float(input("Tax Percentage(0-100): ").strip())
    except ValueError:
        print("Only numbers.")
    else:
        if basic_salary >= 0 and bonus >= 0 and 0 <= tax_percentage <= 100:
            return employee_name, basic_salary, bonus, tax_percentage
        else:
            print("Wrong Value, Check again.")


# ---------- CONVERTING FUNCTIONS ----------


def calculate_tax(salary, tax_percentage):
    tax = salary * tax_percentage / 100
    return tax


def calculate_net_salary(salary, bonus, tax):
    net_salary = salary + bonus - tax
    return net_salary


# ---------- DISPLAY FUNCTION ----------


def display_report(name, basic_salary, bonus, tax, net_salary):
    print("=" * 40)
    print("Employee Report".center(40))
    print("=" * 40)

    print("Name".ljust(15) + f": {name}")
    print("Basic Salary".ljust(15) + f": {basic_salary:.2f}")
    print("Bonus".ljust(15) + f": {bonus:.2f}")
    print("Tax".ljust(15) + f": {tax:.2f}" + "\n")
    print("Net Salary".ljust(15) + f": {net_salary:.2f}")


# ---------- MAIN FUNCTION ----------


def main():
    employee_data = get_employee_data()
    if employee_data is None:
        return
    employee_name, basic_salary, bonus, tax_percentage = employee_data
    tax = calculate_tax(basic_salary, tax_percentage)
    net_salary = calculate_net_salary(basic_salary, bonus, tax)
    display_report(employee_name, basic_salary, bonus, tax, net_salary)


main()
