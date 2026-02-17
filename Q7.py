"""Write a program which takes any date as input and display next date of the calendar e.g. I/P: day=20 month=9 year=2005 O/P: day=21 month=9 year 2005 """
# take input date
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

# function to check leap year
def is_leap(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

# number of days in each month
days_in_month = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]

# adjust February for leap year
if is_leap(year):
    days_in_month[1] = 29

# move to next date
day += 1

# if day exceeds days in current month
if day > days_in_month[month - 1]:
    day = 1
    month += 1

    # if month exceeds December
    if month > 12:
        month = 1
        year += 1

# display next date
print("Next date is:")
print("day =", day, "month =", month, "year =", year)
