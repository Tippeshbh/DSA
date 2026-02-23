def twosum(nums, target):
    dic ={}

    for i,num in enumerate(nums):
        if target - num in dic:
            return [ i, dic[target - num]]
        dic[num] = i

print(twosum([1,2,4,5,6,7],13))  

def twosum(nums, target):
    
    for i in range(len(nums)):
        for j in range(i+1 ,len(nums)):
            if nums[i]+ nums[j] == target:
                return [i, j]
print(twosum([2,3,4,5,6,7],7))