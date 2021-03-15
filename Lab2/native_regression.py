#klar
from matrix import *
import sys
import matplotlib.pyplot as plt





XY=loadtxt(sys.argv[1])
#XY=loadtxt("chirps.txt")
#XY=loadtxt("chirps-modified.txt")
TXY=transpose(XY)

X=TXY[0]
Y=TXY[1]


Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
#predictChirps=b + m*temprature



predictChirps=[]
for i in range (len(X)):
    predictChirps.append(b+m*X[i])
#print (predictChirps)

plt.plot(X,Y,'ro')
plt.plot(X,predictChirps)
plt.show()