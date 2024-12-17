def countNumber(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
a=[]
n=int(input("enter the size of a list:"))
for i in range(n):
    value=int(input("enter the values"))
    a.append(value)
even,odd=countNumber(a)
print (even)
print(odd)