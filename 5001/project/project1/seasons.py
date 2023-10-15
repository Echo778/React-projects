'''
    QI NIU
    16 Sep 2023
    Lab 2 code file
    Ask the user for a date and print out the season that date happens in.
'''

# Input the date and convert it into int form for the following determination
day = int(input("Please enter the day of the date: "))
month = int(input("Please enter the month of the date: "))
year = int(input("Please enter the year of the date: "))

# 1. Determining the invlid dates, if it occurs then exit the program
if (month >= 13 or month <= 0) or (day <= 0 or day >= 32) or \
    (year <= 0) or (month == 2 and day >= 29) or \
    ((month == 4 or month == 6 or month == 9 or month == 11) and day >= 31):
    exit("it is an invalid date")

# 2. Determining the season based on the date and output the result
if (month == 12 and day >= 21) or (month <= 2) or (month == 3 and day < 19):
    print(f"{month}/{day}/{year} is in Winter")
elif (month == 3 and day >= 19) or (month >= 4 and month <= 6) or (month == 6 and day < 21):
    print(f"{month}/{day}/{year} is in Spring")
elif (month == 6 and day >= 21) or (month >= 7 and month <= 9) or (month == 9 and day < 23):
    print(f"{month}/{day}/{year} is in Summer")
elif (month == 9 and day >= 23) or (month >= 10 and month <= 12) or (month == 12 and day < 21):
    print(f"{month}/{day}/{year} is in Fall")
else:
    print("it is an invalid date")
