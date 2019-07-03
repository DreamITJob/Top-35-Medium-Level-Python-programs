#Python program TO to Check Armstrong Number of n digits...

from math import pow
def Check_Armstrong(num):
    original_no = num
    n = 0
    result = 0
    #counting how many digits in given number
    while (num!=0):
        num=num//10
        n+=1
        
    #calculating sum of power n of all digits
    num=original_no
    while(num!=0):
        remainder=num%10
        result+=pow(remainder,n)
        num//=10
        
    return result

number = int(input("Enter a number: "))
if(Check_Armstrong(number)==number):
    print("Number is Armstrong number")
else:
    print("Number is not Armstrong number")
