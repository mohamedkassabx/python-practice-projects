current_PIN = 1234
current_balance = 5000.0

PIN = int(input("Please enter the PIN: ").strip())

if PIN != current_PIN:
    print("Incorrect PIN, transaction declined")
else:
    print("1) Withdraw")
    print("2) Check balance.")

    operation = int(input("Please select the operation number: ").strip())

    if operation == 1 :

        amount = int(input("Enter the amount: ").strip())

        if amount > 5000:
            print("Sorry, your balance is insufficient.")

        else:
            current_balance -= amount
            print(f"Withdraw successful. Your remaining balance is: {current_balance:.1f}")

    elif operation == 2 :
        print(f"The current balance = {current_balance:.1f}")
        
    else:
        print("Please try again.")
