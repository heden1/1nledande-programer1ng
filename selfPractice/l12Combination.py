def factorial(num):
    factorial = 1
    if num < 0:
        return None
    elif num == 0:
        return 1
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        return factorial
        #print("The factorial of",num,"is",factorial)
        
        
def combinations(n,k):
    return((factorial(n))/(factorial(k)*factorial(n-k)))
print(combinations(10,5))
print(factorial(3))
#252