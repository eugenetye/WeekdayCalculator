# This function gets birthdate input then call the getWeekday function
# to return the weekday of the birthdate then display it on the terminal
def main():
    print("This program is used to find the weekday of your birthday")
    birthdate = input("Please enter your birthdate: ")
    while "/" not in birthdate:
        birthdate = input("Please enter your birthdate in the form of mm/dd/yyyy: ")
 
    birth_list = birthdate.split("/")
    month = int(birth_list[0])
    days = int(birth_list[1])
    year1 = int(birth_list[2])
    year2 = 1920
    
    while year1 < 1920:
        birthdate = input("Please enter a valid birthdate. It must not be sooner than 1920: ")
        birth_list = birthdate.split("/")
        month = int(birth_list[0])
        days = int(birth_list[1])
        year1 = int(birth_list[2])
    while month < 0 or month > 12:
        birthdate = input("Please enter a birthdate with a valid month from 1 to 12: ")
        birth_list = birthdate.split("/")
        month = int(birth_list[0])
        days = int(birth_list[1])
        year1 = int(birth_list[2])
    while days > 31 or days < 1:
        birthdate = input("Please enter a birthdate with a valid day from 1 to 31: ")
        birth_list = birthdate.split("/")
        month = int(birth_list[0])
        days = int(birth_list[1])
        year1 = int(birth_list[2])

   
    weekday = getWeekday(year1,year2,days,month)
    print()
    print("The weekday of", birthdate, "is a",weekday)


#This function  takes a year as a parameter and return either true (the year is a leap
#year) or false (not a leap year).
def isLeap(year1):
    if year1 % 4 == 0:
        if year1 % 100 == 0:
            if year1 % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


#This function takes month as a parameter and return the number of days
#from January to the month before it.
def daysPerMonth(month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    temp_days = 0
    for i in range(0, month - 1):
            temp_days += days_in_month[i]
    return temp_days


#This function takes two parameters: year1 and year2 as numbers and
#return the total number of days between those years
def daysPerYears(year1,year2):
    days_in_years = (year1 - year2) * 365
    return int(days_in_years)



#This function takes four parameters: year1,year2,days,and month
# then counts the total number of days between both dates and return the weekday.
def getWeekday(year1,year2,days,month):
    week = ['Thursday','Friday','Saturday','Sunday','Monday','Tuesday','Wednesday']
    leap_days = 1
    if year1 == year2:
        if month > 2:
            leap_days = 1
        else:
            leap_days = 0
    else:
        if isLeap(year1):
            if month > 2:
                leap_days += (year1 - year2) // 4
            else:
                leap_days = (year1 - year2) // 4
        else:
            leap_days += int((year1 - year2) // 4)

    total_days = leap_days + daysPerYears(year1,year2) + daysPerMonth(month) + (days-1)
    weekday = total_days % 7
    return week[weekday]


if __name__ == "__main__":
    main()


