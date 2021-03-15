x=int(input("chose a posetive int "))
i=2
while i**2<=x:
    h=x//i
    if h*i==x:
        print(str(i)+ "x"+str(h))
    i=i+1
