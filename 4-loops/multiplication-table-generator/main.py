print("=" * 50)
print(" Multiplication Table Generator ".center(50, "="))
print("=" * 50)

# ------------ INPUTS ------------
number = int(input("Number".ljust(17) + ": ").strip())
start_multiplier = int(input("Start Multiplier".ljust(17) + ": ").strip())
end_multiplier = int(input("End Multiplier".ljust(17) + ": ").strip())

# ---------- CONSTANTS ----------
counter = 0
results_sum = 0
largest_result = number * end_multiplier
smallest_result = number * start_multiplier

# ---------- OPERATIONS ----------
print("-" * 50)

if start_multiplier <= end_multiplier:
    for num in range(start_multiplier, end_multiplier + 1):
        print(f"{number} x {num} = {number * num}")

        counter += 1
        results_sum += number * num

        # --- check for negative number ---
        if largest_result <= (number * num):
            largest_result = number * num
        if smallest_result >= (number * num):
            smallest_result = number * num

    # ---------- SUMMARY ----------
    print("-" * 50)
    print("- Table Summary")
    print("Total Multiplications".ljust(22) + f"= {counter}")
    print("Sum of All Results ".ljust(22) + f"= {results_sum}")
    print("Largest Result ".ljust(22) + f"= {largest_result}")
    print("Smallest Result ".ljust(22) + f"= {smallest_result}")
else:
    print('"Start Multiplier" must be equal or less than "End Multiplier"')

print("-" * 50)
