#Python program for Fibonacci Sequence Up to a Certain Number....

first_term = 0
second_term= 1
next_term =1
no_of_term = 2
num = int(input("Enter a positive number: "))
print(first_term,second_term,end=' ')
while(next_term<=num):
    print(next_term,end=' ')
    first_term=second_term
    second_term=next_term
    no_of_term+=1
    next_term=first_term+second_term

print(' ')
print("count of terms is: ",no_of_term)
