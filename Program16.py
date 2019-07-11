#C program to swap 2 arrays of same size....
#Python does not have built-in support for Arrays, but Python Lists can be used instead

def Swap_Array(arr1,arr2):
    n=len(arr1)
    temp =0 
    for i in range(n):
        temp=arr1[i] 
        arr1[i]=arr2[i]
        arr2[i]=temp
        
    return arr1,arr2
    
arr1 = [1,2,3,4]
arr2 = [5,6,7,8]
print("Before swapping arrays are: ",arr1,arr2)
print("After swapping arrays are: ",Swap_Array(arr1,arr2))
