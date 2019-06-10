//Python program to check Leap year.....
//Please carefully check conditions of a leap year

def CheckLeapYear(year):
    if year%4==0 :
        if year%100 == 0 :
            if year % 400 == 0:
                print (str(year) + " is a leap year")
            else :
                print (str(year) + " is not a leap year")
        else :
                print (str(year) + " is a leap year")
    else :
                print (str(year) + " is not a leap year")

year = int(input("Enter the year "))
CheckLeapYear(year)
