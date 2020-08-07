year = 0
option = 0
number = 0
month_number=0

def is_leap_year(year):
    year = int(input("Enter the year (4 digits): \n"))
    if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
        print("%d is a Leap Year" % year)
    else:
        print("%d is Not the Leap Year" % year)

def month_name(number):
    import datetime
    number = int(input("Enter the number of a month:\n"))
    month = datetime.datetime(2020,number,1)
    print(str(number) + " is " + month.strftime("%B"))

def days_in_month(month_number, year):
    import datetime
    month_number = int(input("Enter the number of a month:\n"))
    year = int(input("Enter the year (4 digits): \n"))

    if month_number == 1 or month_number ==  3 or month_number == 5 or month_number == 7 or month_number == 8 or month_number == 10 or month_number == 12:
        x = datetime.datetime(year, month_number, 1)
        print(x.strftime("%B has 31 days"))
    elif month_number == 2:
        if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
            print("February has 29 days.")
        else:
            print("February has 28 days.")
    elif month_number == 4 or month_number == 6 or month_number == 9 or month_number == 11:
        x = datetime.datetime(2018, month_number, 1)
        print(x.strftime("%B has 30 days"))

def first_day_of_year(year):
    import math
    year = eval(input('Enter the year: \n'))
    week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    a = 5 * (math.fmod((year - 1), 4))
    b = 4 * (math.fmod((year - 1), 100))
    c = 6 * (math.fmod((year - 1), 400))
    day = math.fmod((1 + a + b + c), 7)
    day = int(day)
    print("The 1st of January " + str(year) + " falls on a " + str(week[day]) + ".")
def first_day_of_month(month_number, year):
    import datetime

    month_number = int(input("Enter the number of a month:\n"))
    year = int(input("Enter the year (4 digits): \n"))

    x = datetime.datetime(year, month_number, 1)
    print(x.strftime("%w") + " is " + x.strftime("%A"))


while option not in ["0","1","2","3","4","5"]:
    option = int(input('Choose from the following options:\n'
                       '0. quit\n'
                       '1. Test is_leap_year().\n'
                       '2. Test month_name().\n'
                       '3. Test days_in_month().\n'
                       '4. Test first_day_of_year().\n'
                       '5. Test first_day_of_month().\n'))
    if option == 1:
        is_leap_year(year)
    if option == 2:
        month_name(number)
    if option == 3:
        days_in_month(number, year)
    if option == 4:
        first_day_of_year(year)
    if option == 5:
        first_day_of_month(month_number,year)
    if option ==0:
        print("The end")
        break
