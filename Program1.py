#Program to find maximum number among 3 numbers using ternary operator in Python....
a = int(input("Enter first Number "))
b = int(input("Enter second Number "))
c = int(input("Enter third Number "))
max = a if ((a>b) and (a>c)) else (b if b>c else c)
print (max)
