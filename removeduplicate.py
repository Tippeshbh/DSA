def remove_duplicate(nums):
    k = 1

    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k

print(remove_duplicate([0,1,2,3,4,4,5]))        

