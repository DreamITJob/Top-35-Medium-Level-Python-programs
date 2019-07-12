#Python program for binay search using Recursion.....

def BinarySearch(array,low,high,element):
    c = 0
    if (low<=high):
        mid=(low+high)//2
        if array[mid]==element:
            return mid
        elif array[mid]>element:
            return BinarySearch(array,0,mid-1,element)
        else :
            return BinarySearch(array,mid+1,high,element)
    else:
        return c

array= [5,6,7,4,2,1,9,3,10,8]
array.sort()     #Binary search algo worked on sorted array
print(array)
element=int(input("Enter element to be searched: "))
index = BinarySearch(array,0,len(array)-1,element)
if (index):
    print("element found at index ",index)
else:
    print("element not found")
