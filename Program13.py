#Python program for swapping of variables...

def swap1(x,y):
    print("1st swap function: ")
    x,y=y,x
    print("first number: ",x)
    print("second number: ",y)

def swap2(x,y):
    print("2nd swap function: ")
    x=x+y
    y=x-y
    x=x-y
    print("first number: ",x)
    print("second number: ",y)

def swap3(x,y):
    print("3rd swap function: ")
    x=x^y
    y=x^y
    x=x^y
    print("first number: ",x)
    print("second number: ",y)
    
def swap4(x,y):
    print("4th swap function: ")
    x=x*y
    y=x//y
    x=x//y
    print("first number: ",x)
    print("second number: ",y)

x=int(input("Enter first number: "))
y= int(input("Enter second number : "))
swap1(x,y)
swap2(x,y)
swap3(x,y)
swap4(x,y)
