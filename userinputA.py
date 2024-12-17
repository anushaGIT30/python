n=int(input("enter size :"))
arr=[]
search=int(input("enter the value to be searched :"))
for i in range(n):
    x=int(input("enter the next value:"))
    arr.append(x)
print(arr)

#searching an element in an array
for j in range (len(arr)):
    if arr[j]==search:
        print(j)
        break
else:
    print("not found")   
#another way
k=0
for l in arr:
    if l==search:
        print(k)
        break
    k+=1

#we can also find by using inbuild functions
print(arr.index(search))         
