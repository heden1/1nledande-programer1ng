#klar
import numpy as np
from numpy import *
import sys
import matplotlib.pyplot as plt




def powers(row,h,k):
    j=0
    n=(len(row))
    leng=(len(range(h,k+1)))
    pMatrix = [[0 for x in range(leng)] for y in range(n)] #creats empty matrix 
    for i in range(n):
        p=h
        for j in range (leng):
            pMatrix[i][j]=row[i]**p
            p=p+1
    return array(pMatrix) 




def poly(a,x):
    Y2=0
    for n in range(len(a)):
        Y2=Y2+a[n,]*x**n   #a[2,]*x**2 + a[1,]*x + a[0,] #or
    return Y2


XY=loadtxt(sys.argv[1]) 

TXY=transpose(XY)

X=TXY[0]
Y=TXY[1]




Xp  = powers(X,0,int(sys.argv[2]))
Yp  = powers(Y,1,1)
Xpt = Xp.transpose()

#calculate the constants
a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]


#creats linspace X2
A=(TXY[0][0])
B=(TXY[0][len(XY)-1])
steps=100 #number of steps bettwen A to B
#step=(((B-A))/steps) 
X2=linspace(A,B,steps).tolist()
#X2=arange(A,B,step).tolist()

#creats Y2
Y2=[]
for i in range (len(X2)):
    Y2.append(poly(a,X2[i])) #calculate Y2 for every X2 Y2(X2)

plt.plot(X,Y,'ro') #plot dots 
plt.plot(X2,Y2) #plot line
plt.show()