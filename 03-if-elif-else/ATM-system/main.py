print("=" * 50)
print(" ATM System ".center(50, "="))
print("=" * 50)


# ----- ACCOUNT INFORMATION ------
current_card_number = 111
current_pin = 1234
account_balance = 5000.00

# ------------ INPUTS ------------
card_number = int(input("Card Number".ljust(20) + ": "))
pin_code = int(input("PIN Code".ljust(20) + ": "))
holder_name = input("Account Holder Name".ljust(20) + ": ")

# ------------ CONDITIONS ------------
if pin_code != current_pin and card_number  != current_card_number :
    print("Incorrect Card Number and PIN, Login declined (hint: 111 & 1234)")
elif pin_code != current_pin:
    print("Incorrect PIN, Login declined (hint: 1234)")
elif card_number  != current_card_number:
    print("Incorrect Card Number, Login declined (hint: 111)")
else:
    print("-" * 50)
    print(f"Welcome {holder_name}.")
    print("1) Withdraw")
    print("2) Check balance.")

    operation = int(input("Please select the operation number: ").strip())

    if operation == 1 :

        amount = int(input("Enter the amount: ").strip())

        if amount > account_balance:
            print("Sorry, your balance is insufficient.")

        else:
            account_balance -= amount
            print(f"Withdraw successful. Your remaining balance is: {account_balance:.2f}")
    elif operation == 2 :
        print(f"The current balance = {account_balance:.2f}") 
    else:
        print("Invalid operation.")