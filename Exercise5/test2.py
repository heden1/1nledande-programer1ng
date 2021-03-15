import counters

def changeValues(n, c1, c2):
    n = n + 1
    c1.count()
    c2 = counters.SimpleCounter()
    c2.count()

k=5
a = counters.SimpleCounter()
b = counters.SimpleCounter()
changeValues(k,a,b)
print("k="+str(k))
print("a="+str(a.getValue()))
print("b="+str(b.getValue()))