# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process task based on priority
match priority.lower():  # make it case-insensitive
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an undefined priority"

# Modify reminder if the task is time-bound
if time_bound.lower() == "yes" and priority.lower() in ["high", "medium"]:
    reminder += " that requires immediate attention today!"
elif time_bound.lower() == "no" and priority.lower() == "low":
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print(reminder)
