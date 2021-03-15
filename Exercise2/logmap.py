#klar
import sys
import matplotlib.pyplot as plt


#functions
def logmap (r):
#0 < r <= 4
    n=0
    x=[0]*2
    x[n]=0.2
    x[n+1]=r*(x[n])*(1-(x[n]))
    n=n+1
    #print(x[n])
    return (x[n])


def experiment(r,x0,n):
#0 < r <= 4
    i=0
    x=[0]*(n+1)
    x[0]=x0
    for i in range (0,n):
        x[i+1]=r*(x[i])*(1-(x[i]))
        print(x[i])
    #return (x[n])

def table(r,x0,y0,n):
    if 0<r<=4 and 0<=x0<=1 and  0<=y0<=1 and 0<=n:
        i=0
        x=[0]*(n+1)
        y=[0]*(n+1)
        x[0]=x0
        y[0]=y0
        for i in range (0,n):
            x[i+1]=r*(x[i])*(1-(x[i]))
            y[i+1]=r*(y[i])*(1-(y[i]))
            print(x[i],y[i])
        #return (x,y)
    else:
        print("fel input")

def attractors(r,x0,n,epsilon):
    if 0<r<=4 and 0<=x0<=1 and 0<=n:
        i=0
        x=[0]*(n+1)
        x[0]=x0
        while i<n and abs(x[i]-x[i-1])>epsilon:
            x[i+1]=r*(x[i])*(1-(x[i]))
            i=i+1
            #print(i,x[i])
        
        
        #check from the end until the pattern repeats istelf and print does number that the pattern reapets itself around
        #x=[1,2,3,4,5]*25
        x2=[x[-1]]
        i=0
        #print (x[i])
        while x[i-2] not in x2 and i>-100: #for maximun -100 loops 
            i=i-1
            x2.append(x[i-1])
        #print (x2)
        return(x2)



    else:
        print("fel input")







def experiment2(r,x0,n,epsilon):
    
    if 0<=r<=4 and 0<=x0<=1 and 0<=n:
        i=0
        x=[0]*(n+1)
        x[0]=x0
        while i<n and abs(x[i]-x[i-1])>epsilon:
            x[i+1]=r*(x[i])*(1-(x[i]))
            i=i+1
            #print(i,x[i])
        return(x[i])
            #print(x[i],y[i])
        #return (x[n])
        #print(x[i],y[i])
    else:
        print("fel input")

def bifurcationDiagram (x0,n,epsilon,step):
    r=0
    i=0
    y=[0]*(int((4.0/step)+1))
    xa=[0]*(int((4.0/step)+1))
    while r<(4):
        y[i]=experiment2(r,x0,n,epsilon)
        #print(y[i])
        xa[i]=r
        i=i+1
        r=r+step


    plt.plot(xa,y,'.',markersize=1)
    plt.ylabel('y')
    plt.xlabel('r')
    plt.show()

    #return(xa,y)






#call functions
#bifurcationDiagram(0.2,100,1e-5,0.003)


#attractors(3.5,0.2,100,1e-5)


#table(3.9,0.2,0.21,20)
#table(1.5,0.2,0.21,20)
#table(3,0.2,0.21,20)
#table(3.5,0.2,0.21,20)
#table(r,x0,y0,n)
#table(float(sys.argv[1]),0.2,0.21,20)
#table(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]))

#experiment(3.9,0.2,20)
#experiment(3.9,0.21,20)

#logmap(3.9)



