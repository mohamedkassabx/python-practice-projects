# ---------- CONSTANTS -----------
tasks = []

# ---------- MAIN PROGRAM ----------

while True:
    print("\n" + " To-Do List ".center(40, "="))
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    try:
        user_selection = int(input("=> ").strip())
    except ValueError:
        print("Just Numbers!")
    else:
        if user_selection == 1:
            print("\n" + " Add Task ".center(40, "-"))
            task_name = input("Task Name: ").strip()
            if task_name:
                tasks.append(task_name)
                print("Task added successfully.")
            else:
                print("Empty Name!")
        elif user_selection == 2:
            print("\n" + " Tasks ".center(40, "-"))
            if len(tasks) == 0:
                print("There's No Tasks For Now :)")
            else:
                for index, task in enumerate(tasks):
                    print(f"{index + 1}.", task)
        elif user_selection == 3:
            print("\n" + " Remove Task ".center(40, "-"))
            if len(tasks) == 0:
                print("There's No Tasks To Remove :(")
            else:
                try:
                    task_num = int(input("Select the task number: ").strip())
                except ValueError:
                    print("Just Numbers!")
                else:
                    if 0 < task_num <= len(tasks):
                        print(f"{tasks[task_num - 1]} Was Removed.")
                        tasks.pop(task_num - 1)
                    else:
                        print("Select The Correct Number!")
        elif user_selection == 4:
            print("Goodbye:(")
            break
        else:
            print("Select The Correct Number!")
