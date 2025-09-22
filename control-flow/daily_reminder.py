# daily_reminder.py

# Prompt for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority"

# Modify if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."

# Provide a customized reminder
print(reminder)

# print\s*\(\s*f?['\"]Reminder:\s*

