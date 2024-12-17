# First pattern
for i in range(4):
    for j in range(4):
        print("# ", end='')  # Print # with a space
    print()  # Move to the next line after finishing one row

# Separator for clarity (optional)
print()

# Second pattern
for k in range(4):
    for l in range(k + 1):  # Loop to print increasing numbers of #
        print("# ", end='')  # Print # with a space
    print()  # Move to the next line after finishing one row

print()


for a in range(4):
    for b in range(4-a):
        print('#',end='')
    print()       

for c in range(1,5):
    for d in range(5-c):
        print(c,end="")
        c+=1
    print()         