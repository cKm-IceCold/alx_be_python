# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Base reminder using match case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level"

# Modify reminder if time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no" and priority == "low":
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print(reminder)

