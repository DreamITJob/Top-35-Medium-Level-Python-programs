#Python Program for find length of a string without any in-built function....

def Length_String(string):
    str_len =0 
    for i in string:
        str_len+=1
    return str_len

string = "Karan Arora"
print("String length is ", Length_String(string))
