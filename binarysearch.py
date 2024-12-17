pos = -1  # Global variable to store the position of the key

def binarySearch(arr, k):
    global pos  # Use the global variable 'pos'
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            pos = mid  # Update position
            return True  # Key found
        elif arr[mid] < k:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half

    return False  # Key not found

# Input list and key
arr = [33, 44, 55, 66, 77]
k = 1  # Key to search

# Function call
if binarySearch(arr, k):
    print("The key is found at position:", pos)
else:
    print("Key not found")
