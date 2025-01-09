from datetime import datetime ,timedelta
 
def display_current_datetime():
    current_date = datetime.now().replace(microsecond=0)
    formated_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    current_time = datetime.now()
    future_date = current_time.date() + timedelta(days=number_of_days)
    formated_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {future_date}")

calculate_future_date()

