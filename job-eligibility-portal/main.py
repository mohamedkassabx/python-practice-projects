python = input("Are you proficient in using Python? (Yes/No): ").strip().lower()
experience = int(input("How many years of experience or projects do you have? (Enter a number): ").strip())
bootcamp = input("Do you have a university degree in computer science or have you completed an intensive training bootcamp? (Yes / No): ").strip().lower()

if python == "yes" and (experience >= 2 or bootcamp == "yes"):
    print("Congratulations! You have been accepted to the next stage of interviews.")
else:
    print("Sorry, your current qualifications do not match the job requirements.")