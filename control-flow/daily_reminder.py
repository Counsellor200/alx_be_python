# daily_reminder.py
# Ask the user for task details
priority = input("Enter the task's priority (high, medium, low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()
# Generate reminder message based on priority
match priority:
    case "high":
        reminder = (f"Task: {task} | Priority: HIGH - Act immediately!")
    case "medium":
        reminder = (f"Task: {task} | Priority: MEDIUM - plan to complete soon.")
    case "low":
        reminder = (f"Task: {task} | Priority: LOW - Handle when possible.")
    case _:
        reminder = (f"Task: {task} | Priority: UNKNOWN Please provide a valid priority (high, medium,low).")
# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder+= "That requires immediate attention today!"
# Print the final reminder message
print(reminder)
