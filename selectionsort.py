def selection_sort(nums):
    for i in range(len(nums) - 1):  # Loop through the list except the last element
        minpos = i  # Assume the current index is the minimum position
        for j in range(i + 1, len(nums)):  # Check for a smaller element in the rest of the list
            if nums[j] < nums[minpos]:
                minpos = j  # Update the minimum position

        # Swap the minimum element found with the first unsorted element
        nums[i], nums[minpos] = nums[minpos], nums[i]

# Example usage
nums = [2, 7, 5, 4, 33, 11]
selection_sort(nums)
print("Sorted List:", nums)
