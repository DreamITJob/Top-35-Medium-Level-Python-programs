#Python program to check whether a character is Uppercase or Lowercase.....

ch = input("Enter a character ")
if(ch >='A') and (ch<= 'Z'):
    print(ch + " is a uppercase character",ch)
elif(ch >='a') and (ch<= 'z'):
    print(ch + " is a lowercase character",ch)
else :
    print("You have Entered invalid character!")
