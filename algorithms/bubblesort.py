def bubblesort(nums):
    n = len(nums)

    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums

print(bubblesort([2,1,49,5,8,7]))
