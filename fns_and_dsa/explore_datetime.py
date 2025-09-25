import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()   # Step 2
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Step 3
    print("Current date and time:", formatted_date)
    return current_date   # return so we can reuse if needed

def calculate_future_date():
    number_of_days = int(input("Enter number of days: "))
    current_date = datetime.date.today()  # today's date only (YYYY-MM-DD)
    future_date = current_date + datetime.timedelta(days=number_of_days)  # Step 5
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Call functions
display_current_datetime()
calculate_future_date()
