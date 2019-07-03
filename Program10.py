#Python program TO find GCD of 2 positive integers....

def GCD(x,y):
    if (x==0):
        return y
    while y!=0 :
        if (x>y):
            x=x-y
        else :
            y =y-x
    return x

first_no = int(input("Enter first number: "))
second_no = int(input("Enter Second number: "))
print("GCD of numbers is: ",GCD(first_no,second_no))
