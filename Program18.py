#Python program  for printing smallest and greatest element in array...
#Also check this link : https://www.geeksforgeeks.org/max-min-python/

def Print_Min_Max(array):
    n = len(array)
    mini= maxi = array[0]
    for i in range(n):
        if mini>array[i]:
            mini = array[i]
        elif maxi<array[i]:
            maxi = array[i]
    
    return mini,maxi
    
array = [0,-2,1,8,2,-1,9,6,10,3,4,12]

mini,maxi = Print_Min_Max(array)
print("Minimum element is {} and Maximum element is {}".format(mini,maxi))
