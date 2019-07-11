#Python program for linear search in array....

def Linear_Search(array,element):
    n=len(array)
    for i in range(n):
        if array[i] == element:
            return i
    else:
        return False
        
array = [3,2,1,6,8,9,4,5,10]
element = int(input("Enter element to be searched: "))
x= Linear_Search(array,element)
if (x):
    print("Element found at location {}".format(x))
else:
    print("Element not found ")
