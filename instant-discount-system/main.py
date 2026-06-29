print("Welcome to instant discount system")
cost =  float(input("Enter the cost: ").strip())

if cost < 100 :
    print(f"Sorry, you cannot get a discount. and the total is {cost:.1f} EGP.")
elif cost > 100 and cost < 500 :
    print(f"Your discount is 10%, and the total is {(cost - (cost * 0.1)):.1f} EGP.")
else:
    print(f"Your discount is 20%, and the total is {(cost - (cost * 0.2)):.1f} EGP.")