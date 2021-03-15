import time
import wordfreq

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

def fileWords(path):
    f = open(path)
    tokens = list(set(wordfreq.tokenize(f)))
    f.close()
    return tokens

def benchmark(f,x,ns):
    start = time.process_time()
    n = 1000
    for i in range(n):
        f(x,ns)
    end = time.process_time()
    print((end-start)/n)
