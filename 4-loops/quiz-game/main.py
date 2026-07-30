print("=" * 50)
print(" Quiz Game ".center(50, "="))
print("=" * 50)


# ---------- CONSTANTS -----------
questions = [
    "what color is the sun? ",
    "1 + 1? ",
    "How many days in a week? ",
    "How many legs does a cat have? ",
]

answers = [
    "yellow",
    "2",
    "7",
    "4",
]
correct_answers = 0
wrong_answers = 0
counter = 0

# ---------- OPERATIONS ----------

for q in questions:
    user_answer = input(q).strip().lower()
    if user_answer == answers[counter]:
        print("Correct!\n")
        correct_answers += 1
    else:
        print(f"Wrong! The Correct is = {answers[counter]}\n")
        wrong_answers += 1
    counter += 1


# ---------- SUMMARY ----------
print(" Summary ".center(50, "-"))
print("Total Questions".ljust(20) + f": {len(questions):d}")
print("Correct Answers".ljust(20) + f": {correct_answers:d}")
print("Wrong Answers".ljust(20) + f": {wrong_answers:d}")
print("Final Score".ljust(20) + f": {correct_answers:d}/{len(questions):d}")
print(
    "Score Percentage".ljust(20) + f": {(correct_answers / len(questions) * 100):.1f}%"
)
