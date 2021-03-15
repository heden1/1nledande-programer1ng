def gcd(m,n):
    while True:
        print("gcd("+str(m)+","+str(n)+") == ",end='')
        if n==0:
            print(m)
            return m
        
        n1=m%n
        m=n
        n=n1
        print("gcd("+str(m)+","+str(n)+")")
    
gcd(84,60)
#gcd(317550,97020)

def binarySearch(values, i, j, key):
    while i <= j:
        k = (i + j)//2
        currentItem = values[k]
        if key == currentItem:
            return k
        elif key < currentItem:
            j = k - 1
        else:
            i = k + 1
    return None
    
    
#values=[1,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
#i=0
#j=23
#key=10
#print(binarySearch(values,i,j,key))
#print(binarySearch(values,10,5,key))

import os
def totalFileSize(path):
    firstPath=path
    try:
        total
    except UnboundLocalError:   
        total=0      
    
    print("Files and directories in '", path, "' :")  
    for file1 in os.listdir(path):
            if os.path.isdir(path+file1):
                print(path+file1, "is a directory")
                firstPath=firstPath+file1+"/"
                total=total+totalFileSize(firstPath)
                print("--------")
                print(" ")
                print(" ")
                print("Back to directory: " +path)
                
            else:
                print(file1)
                total=total+os.path.getsize(path+file1)
                print(str(os.path.getsize(path+file1))+ " Bytes")
                
                
    return total

    
#print(totalFileSize('/Users/anton_heden/Downloads/lab3/'))
