class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:

        even = 0  # max sum if we add next number
        odd = 0   # max sum if we subtract next number

        for num in nums:

            new_even = max(even, odd + num)  # pick num as +
            new_odd  = max(odd, even - num)  # pick num as -

            even = new_even
            odd = new_odd

        return even
    
nums = [4,2,5,1]
object = Solution() 
result = object.maxAlternatingSum(nums)
print(result)
