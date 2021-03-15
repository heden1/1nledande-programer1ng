
import sys

def  main(n,s):
    print(n,s)




def hSum(num_terms):
    n=0
    s=0
    main(n,s)
    num_terms=int(num_terms)
    for n in range(1,num_terms):
        s=s+1/n
        main(n,s)
    n=n+1
    s=s+1/n
    #print(n,s)
    return s

hSum(sys.argv[1]) 


#hSum(5)

