def linsearch(x,ns):
    counter = 0
    for n in ns:
        if n == x:
            return counter
        counter = counter + 1
    return -1

def binsearch(x,ns):
    low = 0
    high = len(ns)-1
    while low <= high:
        mid = (low + high)//2
        item = ns[mid]
        if x == item:
            return mid
        elif x < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1
