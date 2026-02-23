def seletionSort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[j]<nums[min_index]:
                min_index = j
        nums[i],nums[min_index] =nums[min_index],nums[i] 
    return nums
print(seletionSort([25,43,12,6,29]))          
