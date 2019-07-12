#Python program for moving zero at the end of an array.........

def MovingZero(array):
    a = [0 for i in range(array.count(0))]
    x = [ i for i in array if i != 0]
    x.extend(a)
    return(x)

print(MovingZero([0,2,3,4,6,7,10]))
print(MovingZero([10,0,11,12,0,14,17]))
