n=int(input("enter the n value :"))
k=int(input("enter the k value: "))
arr=[]

for i in range(n):
    val=int(input("enter the values "))
    arr.append(val)

for j in range(n):
    if arr[j]==k:
        print("the key is found at the " , j)
        break
else:
    print("the key is not found")
                
    