n=int(input("enter any number:"))
t1=0
t2=1
print(t1)
print(t2)
for i in range(2,n):
    
    t3=t1+t2
   

    print(t3)
    t1=t2
    t2=t3
#using function
def fibonacci(m):
    a = 0
    b = 1
    print(a)  # Print the first Fibonacci number
    print(b)  # Print the second Fibonacci number
    for i in range(2, m):
        c = a + b
        print(c)  # Print the next Fibonacci number
        a = b
        b = c
    return   # Explicitly return None to avoid confusion

l = int(input("Enter the Fibonacci series length: "))
ans = fibonacci(l)
print(ans)  # This will print None, as the function doesn't return any meaningful value

       

   