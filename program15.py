#Python program to add two numbers without using arithmetic operator

def Add(num1,num2):
    while(num2!=0):
        carry = num1&num2
        num1=num1^num2
        num2= carry<<1
    return num1
    
number1 = int(input("First number: "))
number2 = int(input("Second number: "))
print("The sum of {0} and {1} is {2}" .format(number1, number2,Add(number1, number2)))
