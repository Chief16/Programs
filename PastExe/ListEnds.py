a = [2,4,6,8,9,7,5,3,1]
def first_last(a):
    first, *middle, last = a
    b = [first,last]
    return b
print (first_last(a))

