from datetime import datetime, timedelta, date

def display_current_datetime():
    """Displays the current date and time in YYYY-MM-DD HH:MM:SS format"""
    current_date = datetime.now()   # current date & time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return formatted_date   # return so it can be reused

def calculate_future_date():
    """Calculates a future date based on user input (in days)"""
    number_of_days = int(input("Enter number of days to add to the current date: "))
    current_date = date.today()  # today's date
    future_date = current_date + timedelta(days=number_of_days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Run functions
display_current_datetime()
calculate_future_date()
