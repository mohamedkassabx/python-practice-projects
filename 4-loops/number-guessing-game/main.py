print("=" * 50)
print(" Number Guessing Game ".center(50, "="))
print("=" * 50)


# ---------- CONSTANTS -----------
secret_number = 7
counter = 0

# ------------ INPUTS ------------
while 1:
    if counter == 0:
        number = int(input("Guess the number from 0 to 10 : ").strip())
        counter += 1
        if number == secret_number:
            print(f"{number} Is Correct!")
            print("Congrats you made it from First Time!")
            break
    else:
        number = int(input(f"{number} is Wrong, try again : ").strip())
        counter += 1
        if number == secret_number:
            print(f"{number} Is Correct!")
            print(f"Number of tries : {counter}")
            break