#Python program for calculating prime upto 1000.....
#Please undersatnd this program: https://github.com/DreamITJob/Basic-C-Programs/blob/master/Program4.c
'''After doing this program please see below links:
https://stackoverflow.com/questions/2468412/finding-a-prime-number-after-a-given-number
https://www.geeksforgeeks.org/prime-numbers-after-prime-p-with-sum-s/ '''

def Check_Prime(number): #function for checking given number is prime or not?
    count=0
    for i in range(2,(number//2)+1):
        if(number%i==0):
            count+=1
    
    if count==0:
        return True
    else:
        return False
            
def Prime_upto_p(number):
    first_prime = 2
    count=0
    print(first_prime,end=' ')
    for i in range(3,number+1):
        if Check_Prime(i):
            print(i,end=' ')
            count+=1
    return count

number = int(input("Enter value up to which u want prime number: "))
print("Total number of prime are : {}".format(Prime_upto_p(number)))
