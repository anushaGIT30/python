#filter is used to filter filter(fun,iter)
def evn(n):
    return  n%2==0
nums=[55,63,12,44,34,66]
even=list(filter(evn,nums))
print(even)
##it can be also write using lamda functions
##even=list(filter(lambda n: n%2==0,nums))
doubles=list(map(lambda n:n*2,nums))
print(doubles)
from functools import reduce

sum=reduce(lambda a,b:a+b,doubles)
print(sum)