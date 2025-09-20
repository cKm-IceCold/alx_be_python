# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Normalize inputs
priority = priority.lower()
time_bound = time_bound.lower()

# Generate reminder
match priority:
    case "high" | "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task.")
    case "low":
        if time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"'{task}' has an undefined priority.")
