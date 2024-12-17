"""n = int(input("Enter size: "))
arr = []

# Take input for the array
print("Enter the values:")
for i in range(n):
    value = int(input())
    arr.append(value)

print("Original array:", arr)

# Take the value to be deleted
val = int(input("Enter the value to be deleted: "))

# Create a new array without the value to be deleted
newArr = []
for i in range(n):
    if arr[i] != val:
        newArr.append(arr[i])

print("Updated array:", newArr)"""

# Input the size of the array
n = int(input("Enter the size of the array: "))

# Input the array elements
arr = []
print("Enter the elements of the array:")
for i in range(n):
    value = int(input())
    arr.append(value)

# Input the index to delete
index_to_delete = int(input("Enter the index to delete: "))

# Validate the index
if 0 <= index_to_delete < n:
    # Create a new array excluding the element at the given index
    new_arr = []
    for i in range(n):
        if i != index_to_delete:
            new_arr.append(arr[i])
    print("Updated array:", new_arr)
else:
    print("Invalid index!")

          


        
