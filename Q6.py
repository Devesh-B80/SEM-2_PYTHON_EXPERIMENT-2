"""Find whether a given year is a leap year or not."""
year = int(input("Enter a year: "))

# leap year condition:
# divisible by 400 OR divisible by 4 but not by 100
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
