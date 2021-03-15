#klar
def transpose(matrix):
    try:
        m=(len(matrix))
        n=(len(matrix[0]))
        TMatrix = [[0 for x in range(m)] for y in range(n)] #creats empty matrix i the transpose size
        for i in range(m):#for every row
            for j in range(n): #for evere colon
                TMatrix[j][i] =matrix[i][j]
        return TMatrix 
    except IndexError:
        print ("empty matrix")
        return matrix   


def powers(row,h,k):
    j=0
    n=(len(row))
    length=(len(range(h,k+1)))
    pMatrix = [[0 for x in range(length)] for y in range(n)] #creats empty matrix 
    for i in range(n):
        p=h
        for j in range (length):
            pMatrix[i][j]=row[i]**p
            p=p+1
    return pMatrix



def matmul(A,B):
    try:
        m1=(len(A))
        n1=(len(A[0]))
        m2=(len(B))
        n2=(len(B[0]))
        if n1==m2:
            C = [[0 for x in range(n2)] for y in range(m1)] #creats empty matrix 

            for i in range (n2):#i = which colon vi ar on in C 
                for j in range (m1):#% j= which row vi ar on in C 
                    for k in range (n1):#%= which number that is going to get multiplied
                        C[j][i]=C[j][i]+(A[j][k]*B[k][i])   #C(j,i)= C(j,i)+ A(j,k)*B(k,i);

        else:
            print("A and B can't be multiplied. Number of colons in A not equal to number of rows in B")
            print(n1," not equal to ",m2)
            return
    except IndexError:
        print("list index out of range")
        if A==[]:
            return A
        else:
            return B

    return C



def invert(A):
    m=(len(A))
    n=(len(A[0]))
    if m==2 and n==2: 
        det=(A[0][0]*A[1][1])-(A[0][1]*A[1][0]) #calculate the determinate
        AInv=[[A[1][1]/det,-A[0][1]/det],[-A[1][0]/det,A[0][0]/det]] 
        
    else:
        print("Only 2x2 matrix")
        return
    return AInv



def loadtxt(filename):
    file = open(filename,"r")
    List=file.readlines()
    file.close() 
    myList = [[float(val) for val in line.split()] for line in List[0:]]
    return myList



