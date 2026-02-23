#math
'''def missingNumber( nums: list[int]) -> int:
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual
print(missingNumber([1,2,3,4,6,7,8,9]))'''

#set
'''def missingNumber( nums: list[int]) -> int:
    s = set(nums)
    n = len(nums)
   
    for i in range(n + 2):
        if i not in s:
            return i
    return i
        
print(missingNumber([0,1,2,3,4,6,7,8]))  
'''
#sorting
'''def missingNumber(nums: list[int]) -> int:
    nums.sort()

    for i in range(len(nums) +2):
        if nums[i] != i:
            return i

    return len(nums)

print(missingNumber([0,1,2,3,5,6,8]))'''

def missingNumber( nums: list[int]) -> int:
    nums.sort()
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > mid:
            right = mid
        else:
            left = mid + 1

    return left
print(missingNumber([0,1,2,3,4,5,6,7]))


