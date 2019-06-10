#Program for printing 1 to 100 numbers without loops...

def PrintCount(num):
    if num!=101:
        print (num)
        PrintCount(num+1)
    else:
        return 0
    
PrintCount(1)
