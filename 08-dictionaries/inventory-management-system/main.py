# ---------- CONSTANTS -----------
products = {}

# ---------- MAIN PROGRAM ----------

while True:
    # ---------- MENU ----------
    print("=" * 40)
    print("Inventory Management System".center(40))
    print("=" * 40)

    print("1. Add Product")
    print("2. View Inventory")
    print("3. Update Quantity")
    print("4. Search Product")
    print("5. Remove Product")
    print("6. Inventory Count")
    print("7. Exit")

    try:
        user_selector = int(input("=> ").strip())
    except ValueError:
        print("Just numbers!")
    else:
        # ---------- ADD PRODUCT ----------
        if user_selector == 1:
            print(" Add Product ".center(40, "-"))

            product_name = input("Product Name: ").strip().title()
            product_quantity = input("Product Quantity: ").strip()

            if product_name and product_quantity:
                try:
                    product_quantity = int(product_quantity)
                except ValueError:
                    print('"Product Quantity" accept only numbers.')
                else:
                    if product_name in products:
                        print(f'"{product_name}" already exists.')
                    elif product_quantity < 1:
                        print('"Product Quantity" must be 1 or more.')
                    else:
                        products[product_name] = product_quantity
                        print(f'"{product_name}" added successfully.')
            else:
                print("Empty field!")
        # ---------- VIEW PRODUCTS ----------

        elif user_selector == 2:
            print(" View Products ".center(40, "-"))
            if products:
                for index, (product, Quantity) in enumerate(products.items()):
                    print(f"{index + 1}.")
                    print(f"Product : {product}")
                    print(f"Quantity: {Quantity}", "\n")
            else:
                print("Inventory is empty.")
        # ---------- UPDATE QUANTITY ----------
        elif user_selector == 3:
            print(" Update Quantity ".center(40, "-"))
            update_name = input("Product Name: ").strip().title()
            if update_name in products:
                new_quantity = input("New Quantity: ").strip()
                try:
                    new_quantity = int(new_quantity)
                except ValueError:
                    print('"New Quantity" accept only numbers!')
                else:
                    if new_quantity < 1:
                        print("Quantity must be 1 or more.")
                    else:
                        products[update_name] = new_quantity
                        print(f'"{update_name}" updated.')
            else:
                print(f'"{update_name}" not found.')

        # ---------- SEARCH PRODUCT ----------

        elif user_selector == 4:
            print(" Search Product ".center(40, "-"))
            search_name = input("Product Name: ").strip().title()
            if search_name in products:
                print(f"Product : {search_name}")
                print(f"Quantity: {products[search_name]}")
            else:
                print(f'"{search_name}" not found.')
        # ---------- REMOVE PRODUCT ----------

        elif user_selector == 5:
            print(" Remove Product ".center(40, "-"))
            remove_name = input("Product Name: ").strip().title()
            if remove_name in products:
                products.pop(remove_name)
                print(f"{remove_name} deleted successfully.")
            else:
                print(f'"{remove_name}" not found.')
        # ---------- INVENTORY COUNT ----------

        elif user_selector == 6:
            print(" Inventory Count ".center(40, "-"))
            print(f"Total Products: {len(products)}")
        # ---------- EXIT ----------

        elif user_selector == 7:
            print("Goodbye:(")
            break
        else:
            print("Select The Correct Number!")
