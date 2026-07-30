class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit!")
        else:
            self.balance += amount
            print("Deposit successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdraw successfully.")

    def show_balance(self):
        return self.balance

    def display_info(self):
        print("=" * 40)
        print("Account Information".center(40))
        print("=" * 40)

        print("Account Holder".ljust(15) + f": {self.account_holder}")
        print("Account Number".ljust(15) + f": {self.account_number}")
        print("Balance".ljust(15) + f": {self.balance:.2f}" + '\n')

# -------- MAIN FUNCTION --------

def main():
    print("=" * 40)
    print("Bank System".center(40))
    print("=" * 40)

    # -------- ACCOUNT INPUTS --------
    account_holder = input("Account Holder".ljust(15) + ": ").strip().title()
    account_number = input("Account Number".ljust(15) + ": ").strip()
    balance = input("Balance".ljust(15) + ": ").strip()
    try:
        account_number = int(account_number)
        balance = float(balance)
    except ValueError:
        print('"Account Number" and "Balance" accept only numbers!')
    else:
        account = BankAccount(account_holder, account_number, balance)
        # -------- ACCOUNT MENU --------

        while True:
            print(" Account Menu ".center(40, "-"))
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Balance")
            print("4. Account Information")
            print("5. Exit")
            user_selector = input("=> ").strip()
            try:
                user_selector = int(user_selector)
            except ValueError:
                print("Only numbers!")
            else:
                # -------- DEPOSIT --------

                if user_selector == 1:
                    print(" Deposit ".center(40, "-"))

                    deposit = input("Deposit amount: ").strip()
                    try:
                        deposit = float(deposit)
                    except ValueError:
                        print("Only numbers!")
                    else:
                        account.deposit(deposit)
                        print(f"Current Balance = {account.show_balance():.2f}")
                # -------- WITHDRAW --------

                elif user_selector == 2:
                    print(" Withdraw ".center(40, "-"))

                    withdraw = input("Withdraw amount: ").strip()
                    try:
                        withdraw = float(withdraw)
                    except ValueError:
                        print("Only numbers!")
                    else:
                        account.withdraw(withdraw)
                        print(f"Current Balance = {account.show_balance():.2f}")
                # -------- SHOW BALANCE --------

                elif user_selector == 3:
                    print(f"Balance = {account.show_balance():.2f}")
                # -------- ACCOUNT INFORMATION --------
                    
                elif user_selector == 4:
                    account.display_info()
                # -------- EXIT --------
                
                elif user_selector == 5:
                    print("Goodbye :)")
                    break
                else:
                    print("Wrong number!")
         


main()
