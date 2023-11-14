#!/usr/bin/python3
import math
import argparse

def checkLeapYear(year):
    """Checks if given year is a leap year
    Three rules to determine if year is a leap year
    1. If the Year is evenly divisible by 4
    2. If the Year is not evenly divisible by 100
    3. Unless the year is also evenly divisible by 400
    E.g. 1900 is not a leap year (evenly divisible by 4, evenly divisible by 100, but not evenly divisible by 400)
    but 2000 is a leap year (evenly divislbe by 4, evenly divisible by 100, but IS evenly divislbe by 400)
    Returns True if given year is a leap year, false otherwise
    """
    if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
        return True
    else:
        return False

def checkFirstDayOfMonth(month, year):
    """Returns what day of the week the first day of the month falls on
    Each month is given a value, Jan and Feb are given 11 and 12 respectivly due to special leap year rules
    Century is determined by the first 2 digits of the year and yr is determined by the last 2 digits of the year
    (Note: If the year given is less than 4 digits, leading zeros are added to complete the calculation)
    If the month given is either January or Feburary, 1 year is subtracted from the given year due to leap year rules
    The forumula for calculating the day of the week for any given date is taken from https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
    k = 1 because we only want to find which day the first day of the month falls on
    Returns an integer value that corresponds to the day in the week (0=Sun,1=Mon,2=Tues,...,6=Sat)
    """

    # Each month gets a corresponding integer value, starting at March=1. Jan and Feb are given 11 and 12 respectivly due to leap year rules.
    months = {'MARCH': 1, 'APRIL': 2, 'MAY': 3, 'JUNE': 4, 'JULY': 5, 'AUGUST': 6, 'SEPTEMBER': 7, 'OCTOBER': 8, 'NOVEMBER': 9, 'DECEMBER': 10, 'JANUARY': 11, 'FEBUARY': 12}
    month_num = months.get(month)

    # Checks that the given month is a real month, if it does not find the month in the list, the program exits with an error message
    if month_num == None:
        print("Month must be valid English month (e.g. January, Febuary, March, ect)")
        exit()

    # Adds leading zeros if year is less than 4 digits
    if len(str(year)) < 4:
        difference = 4 - len(str(year))
        zeros = '0'*difference
        year = zeros + str(year)

    # Assigns century (first 2 digits) and yr (last 2 digits) for calculation
    century = str(year)[0] + str(year)[1]
    yr = str(year)[2] + str(year)[3]
    
    # Subtracts a year from 'yr' if the month is Jan or Feb due to leap year rules
    if month == 'JANUARY' or month == 'FEBUARY':
        yr = int(yr) - 1
    
    calc_day = (1 + math.floor((2.6 * int(month_num)) - 0.2) - (2 * int(century)) + int(yr) + math.floor(int(yr)/4) + math.floor(int(century)/4)) % 7

    return calc_day

def daysInMonth(month, year):
    """Based on given month, returns how many days are in each month
    7 Months have 31 days, 4 Months have 30 days (specified), and Feburary has 29 days if the year is a leap year, and 28 if it is not
    Returns the amount of days that exist in the given month for the given year"""
    if month == 'APRIL' or month == 'JUNE' or month == 'SEPTEMBER' or month == 'NOVEMBER':
        return 30
    elif month == 'FEBUARY':
        if checkLeapYear(year) == True:
            return 29
        else:
            return 28
    else:
        return 31

def printCalander(month, year):
    """Main driver that prints out the calander month for any given month/year
    Uses first day value to determine where to start on the calander (how many spaces to include)
    Also uses first day value as a counter to determine when it should move to the next line (new week)
    Gap between dates gets smaller when dates reach 2 digits
    Returns the calander string"""

    # Validates data types, error message and exit if year is not given as an integer
    try:
        year = int(year)
    except(ValueError):
        print("Not valid year! (e.g. June 1456, March 2000, August 2023, September 3050)")
        exit()
    
    # Checks that year given is a positive integer (i.e. value 0 or higher)
    if int(year) < 0:
        print("Year must be positive integer!")
        exit()
    
    # Converts every letter in month to uppercase to account for different variations (i.e. One person may write 'march' and another may write 'March')
    month = month.upper()
    # Standardizes the spacing between dates
    spaces = '   '
    # Gets the first day of the month for the given month/year
    first_day = checkFirstDayOfMonth(month, year)
    # Gets how many days are in the given month/year
    days = daysInMonth(month, year)

    # Begin building calander string
    calander = str('\n')

    # Formatting the Month so the first letter is capitalized and every other letter is lowercase
    for letter in range(0, len(str(month))):
        if letter == 0:
            calander += str(month[letter])
        else:
            calander += str(month[letter].lower())

    # Our header (i.e. $Month $Year)
    calander += str(f' {year}')
    calander += str(f'\n\nS  M  T  W  T  F  S\n')
    calander += str(spaces*first_day)

    # Go through each day in the given month
    for day in range(1, days + 1):

        # Our counter for a new week
        if first_day > 6:
            first_day = 0
            calander += str('\n')
        
        # Our check if the digits go to 2 (i.e. 10 or above) since we'll need to change the spacing
        if day < 10:
            calander += str(f'{day}  ')
        else:
            calander += str(f'{day} ')
        first_day+=1

    return calander

def printYear(year):

    months = ['JANUARY', 'FEBUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'NOVEMBER', 'DECEMBER']

    for month in months:
        print(printCalander(month, year), end='\n\n----------------------\n')

def main(month, year):
    calander = printCalander(month, year)

    print(f'{calander}', end='\n\n')

def unitTests():

    printCalander()  
    printCalander('june', 2023)
    printCalander('jUnE', 2023)
    printCalander('JUNE', 2023)
    printCalander('blah', 2023)
    printCalander('June', 203)
    printCalander('June', 20)
    printCalander('June', 1)
    printCalander('March', 10000)
    printCalander('June', 'blah')
    printCalander(2000, 'June')
    printCalander(2023, 2024)
    printCalander('August', 3075)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Print Out Full Calander For Any Given Month of Any Given Year!")
    parser.add_argument("month", help="English Month In Gregorian Calander")
    parser.add_argument("year", help="A Standard Year (After Common Era)")

    args = parser.parse_args()

    main(args.month, args.year)