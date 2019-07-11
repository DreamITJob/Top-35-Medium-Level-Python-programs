#Python program  for reversing of elements in array...

def Reverse(array):
    n = len(array)
    temp=0
    i=0 ; j=n-1
    while(i<=j):
        temp=array[i]
        array[i]=array[j]
        array[j] =temp
        i+=1
        j-=1
    return array 
    
array = [0,-2,1,8,2,-1,9,6,10,3,4,12]
print("Array reversed using slicing: ",array[::-1])
print("Array reversed using our function: ",Reverse(array))
