#Python Program for checking all bits are set to 1 or not....

def Checking_Bits(number):
    if ((number & number+1)==0):
        print("All bits are set")
    else:
        print("All bits are not set")
        
        
number = int(input("Enter the number "))
Checking_Bits(number)
