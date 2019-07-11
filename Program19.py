#Python program  for printing sum of elements in array...

def Sum(array):
    n = len(array)
    sum_of_elements =0
    for i in range(n):
        sum_of_elements+=array[i]
    
    return sum_of_elements 
    
array = [0,-2,1,8,2,-1,9,6,10,3,4,12]
print("Sum of array elements is {}".format(Sum(array)))
