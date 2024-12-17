def factorial(n):
    if n==0:
        return 1
    if n==1:
        return 1
    fact=1
    for i in range(1,n+1):
        fact=fact*i

    return fact
  
print(factorial(5))  

#using recursion
def factorialOfnum(m):
    if m==0:
        return 0
    if m==1:
        return 1
    
    return m*factorialOfnum(m-1)
ak=int(input("enter any number:"))
res=factorialOfnum(ak)
print(res)    
