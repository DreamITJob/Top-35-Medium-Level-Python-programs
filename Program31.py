#PYthon program to search an element in row-wise and column-wise sorted matrix
def Search(matrix,n,element):
    i=0
    j=n-1
    while(i<n and j>=0):
        if (matrix[i][j] == element):
            print("Element Found at ", i+1, ", ", j+1) 
            return 1
        if (matrix[i][j]>element):
            j-=1
        else:  
            i += 1
    
    print("Element not found") 
    return 0
    
matrix = [ [10, 20, 30, 40], 
        [15, 25, 35, 45], 
        [27, 29, 37, 48], 
        [32, 33, 39, 50] ] 
Search(matrix, 4, 39) 
