# ---------- CONSTANTS -----------
cart = []


# ---------- MAIN PROGRAM ----------

while True:
    print("\n" + "=" * 40)
    print("Shopping Cart".center(40))
    print("=" * 40)

    # ----------- MENU -----------
    
    print("1. Add Product")
    print("2. View Cart")
    print("3. Remove Product")
    print("4. Calculate Total Items")
    print("5. Exit")

    try:
        user_selection = int(input("=> ").strip())
    except ValueError:
        print("Just numbers!")
    else:
        if user_selection == 1:
            # ---------- ADD PRODUCT ----------

            print("\n" + " Add Product ".center(40, "-"))
            product_name = input("Write the product name: ").strip()
            if product_name:
                cart.append(product_name)
                print(f'"{product_name}" added successfully.')
            else:
                print("Name is empty!")
        elif user_selection == 2:
            # ---------- VIEW CART ----------

            print("\n" + " Cart ".center(40, "-"))
            if cart:
                for index, product in enumerate(cart):
                    print(f"{index + 1}. {product}")
            else:
                print("Your cart is empty.")
        elif user_selection == 3:
            # ---------- REMOVE PRODUCT ----------

            print("\n" + " Remove Product ".center(40, "-"))
            if cart:
                try:
                    product_number = int(input("Select the product number: ").strip())
                except ValueError:
                    print("Just numbers!")
                else:
                    if 0 < product_number <= len(cart):
                        print(f'"{cart[product_number - 1]}" was removed.')
                        cart.pop(product_number - 1)
                    else:
                        print("Select a correct number!")
            else:
                print("Your cart is empty.")

        elif user_selection == 4:
            # ---------- TOTAL ITEMS ----------

            print("\n" + " Calculate Total Items ".center(40, "-"))
            print(f"Total Items: {len(cart)}")
        elif user_selection == 5:
            # ---------- EXIT ----------

            print("Goodbye :)")
            break
        else:
            print("Select The Correct Number!")
