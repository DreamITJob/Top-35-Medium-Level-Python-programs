#Python program to check a string is pallindrome....

def CheckPallindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

string = "shaynanyahs"
if (CheckPallindrome(string)):
    print("String is pallindrome")
else:
    print("String is not Pallindrome")
    
