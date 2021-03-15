#
def matrix(m,n,k):
    
    rows=[]
    h=1
    for i in range(m):
        row=[]
        for j in range (n):
            row.append(h)
            h=h+1
            if h>k:
                h=1
        rows.append(row)
    return rows

#print(matrix(4,5,3))
 

# another way of solving the problem with modulus
def matrix2(m,n,k):
    
    rows=[]
    h=0
    for i in range(m):
        row=[]
        for j in range (n):
            row.append(h+1)
            h=(h+1)%k
        rows.append(row)
    return rows

#print(matrix2(4,5,3))

#second version of q2

def transliters(s):
    translitTable={}
    f=open("translit.txt",encoding="utf-8")
    for line in f:
        nonLatin,latin=line.split()
        translitTable[nonLatin]=latin
        
    f.close()
    result=""
    for character in s:
        result=result + translitTable.get(character.lower(), character)
    print(result)
transliters("абц")