def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month > 12 or month < 1:
        return f"Invalid Input"
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]

year = int(input("Please Enter a year: "))
month = int(input("Please Enter a month in integer: "))
days = days_in_month(year, month)
print(f"There are {days} days.")
if days == 29:
    print("It is a leap year.")