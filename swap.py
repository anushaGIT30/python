a=int(input())
b=int(input())
"""temp=a
a=b
b=temp"""

#without using 3rd vaiable
"""a=a+b
b=a-b
a=a-b"""


#using xor
a=a^b
b=a^b
a=a^b
print(a,'',b)


d=5
f=9
d,f=f,d

print(d,f)