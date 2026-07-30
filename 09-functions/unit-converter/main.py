# ---------- CONVERTING FUNCTIONS ----------


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles


def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    return kilometers


# ---------- MAIN FUNCTION ----------


def main():
    while True:
        print("=" * 40)
        print("Unit Converter".center(40))
        print("=" * 40)

        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Kilometers to Miles")
        print("4. Miles to Kilometers")
        print("5. Exit")

        try:
            user_selection = int(input("=> ").strip())
        except ValueError:
            print("Only numbers!")
        else:
            # ---------- C TO F ----------

            if user_selection == 1:
                try:
                    unit = float(input("Celsius: ").strip())
                except ValueError:
                    print("Only numbers!")
                else:
                    print(f"Fahrenheit: {celsius_to_fahrenheit(unit):.2f}" + "\n")
            # ---------- F TO C ----------
            
            elif user_selection == 2:
                try:
                    unit = float(input("Fahrenheit: ").strip())
                except ValueError:
                    print("Only numbers!")
                else:
                    print(f"Celsius: {fahrenheit_to_celsius(unit):.2f}" + "\n")
            # ---------- KM TO M ----------

            elif user_selection == 3:
                try:
                    unit = float(input("Kilometers: ").strip())
                except ValueError:
                    print("Only numbers!")
                else:
                    print(f"Miles: {kilometers_to_miles(unit):.2f}" + "\n")
            # ---------- M TO KM ----------

            elif user_selection == 4:
                try:
                    unit = float(input("Miles: ").strip())
                except ValueError:
                    print("Only numbers!")
                else:
                    print(f"Kilometers: {miles_to_kilometers(unit):.2f}" + "\n")
            elif user_selection == 5:
                print("Goodbye:(")
                break
            else:
                print("Wrong choice!")
                

main()
