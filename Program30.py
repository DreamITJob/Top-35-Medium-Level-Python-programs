#Python program for segregate 0,1 in an array...........
# Also see solution : https://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/

def SegregateZeroOne(array):
    a = [i for i in array if i==0]
    x = [i for i in array if i==1]
    a.extend(x)
    return(a)

print(SegregateZeroOne([0,1,1,0,1,0,0]))
