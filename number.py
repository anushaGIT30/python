n = int(input("Enter a number: "))  # Take input from the user
i = 1  # Initialize the counter
while i <= n:  # Loop through numbers 1 to n
    if i % 5 == 0 or i % 3 == 0:  # Skip numbers divisible by either 5 or 3
        i += 1  # Increment the counter and continue
        continue
    print(i, " ", end='')  # Print the number if not skipped
    i += 1  # Increment the counter

a=int(input("enter row "))
b=int(input("enter column"))
i=1
while i<=a:
    j=1
    while j<=b:
        print('#',end="")
        j+=1
    print()
    i+=1       