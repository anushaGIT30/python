def bubblesort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
nums=[2,11,5,6,7,8,13]
bubblesort(nums)
print(nums)