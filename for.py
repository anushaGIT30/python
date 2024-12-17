# Print odd numbers from 0 to 19
for i in range(20):
    if i % 2 != 0:
        print(i, end=" ")
print()  # Move to the next line

# Print numbers from 21 to 29 with a step of 2
for j in range(21, 30, 2):
    print(j, end=" ")
print()  # Move to the next line

# Print numbers in reverse from 60 to 51
for k in range(60, 50, -1):
    print(k, end=" ")
print()  # Move to the next line

# Print perfect square roots in the range 1 to 50
import math
for l in range(1, 50):
    r = math.sqrt(l)
    if r.is_integer():
        print(int(r), end=" ")
print()  # Move to the next line
