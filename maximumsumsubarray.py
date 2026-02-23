def maximum_sub_array(nums):
    maxi = nums[0]
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum > maxi:
            maxi = sum
        if sum < 0:
            sum = 0
    return  maxi 

print(maximum_sub_array( [-2,1,-3,4,-1,2,1,-5,4]))           
