print("=" * 40)
print(" Text Formatter ".center(40, "="))
print("=" * 40)


# ------------ INPUTS ------------
full_name = input("Full Name".ljust(18) + ": ").strip()
email = input("Email Address".ljust(18) + ": ").strip()
city = input("City".ljust(18) + ": ").strip()
fav_quote = input("Favorite Quote".ljust(18) + ": ").strip()

# ------------ FORMATS ------------

# --- FULL NAME ---
print("\n" + " Full Name ".center(40, "-"))
print("Normal".ljust(18) + f": {full_name}")
print("Uppercase".ljust(18) + f": {full_name.upper()}")
print("Lowercase".ljust(18) + f": {full_name.lower()}")
print("Title".ljust(18) + f": {full_name.title()}")
print("First Letter".ljust(18) + f": {full_name[0]}")
print("Last Letter".ljust(18) + f": {full_name[-1]}")
print("Number of Letters".ljust(18) + f": {len(full_name)}")

# --- EMAIL ADDRESS ---
print("\n" + " Email Address ".center(40, "-"))
print("Normal".ljust(18) + f": {email}")
print("Lowercase".ljust(18) + f": {email.lower()}")
print("Capitalized".ljust(18) + f": {email.capitalize()}")

# --- CITY ---
print("\n" + " City ".center(40, "-"))
print("Normal".ljust(18) + f": {city}")
print("Uppercase".ljust(18) + f": {city.upper()}")
print("Capitalized".ljust(18) + f": {city.capitalize()}")

# --- FAVORITE QUOTE ---
print("\n" + " Favorite Quote ".center(40, "-"))
print("Normal".ljust(18) + f": {fav_quote}")
print("Uppercase".ljust(18) + f": {fav_quote.upper()}")
print("Lowercase".ljust(18) + f": {fav_quote.lower()}")
print("Number of Letters".ljust(18) + f": {len(fav_quote)}")