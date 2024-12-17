
n= int(input())

for i in range(2,n):
    if n%i==0:
        print("notprime")
        break
else:
    print("prime")   

import math
n1=int(input())
cnt=0
for j in range(1,int(math.sqrt(n1))):
    if n1%j==0:
        cnt+=1
        if j*j!=n1:
            cnt+=1
if cnt==2:
    print("primenumber")
else:
    print("not primenumber") 

m=int(input())
isprime=True
for k in range(2,m):
    if m%2==0:
        isprime=False
        break
if m>1 and isprime:
    print("it is a prime number")
else:
    print("not a prime ")        
        
            


        
      