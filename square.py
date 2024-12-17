#square of elements in array
arr=[2,3,4,5,6,7,8,9]
for i in range(len(arr)):
    arr[i]=arr[i]*arr[i]
print(arr)   

#sorting 
arr1=[13,67,1,92,2,6]
arr1.sort()
for j in range(len(arr1)):
    print(arr1[j])

#factorial
import math

x=int(input("enter any value"))
fact=1
for i in range(1,x):
    fact=fact*i
    print(fact ,end="")
print()  


import math

arr = [1, 2, 3, 4, 5, 6]

# Iterate through the array and calculate the factorial of each element
for i in range(len(arr)):
    factorial = math.factorial(arr[i])  # Calculate factorial using math.factorial
    print(factorial)

