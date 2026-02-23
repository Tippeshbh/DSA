def maxFrequency(nums, k):
    nums.sort()
    left = 0
    total = 0
    result = 1

    for right in range(len(nums)):
        total += nums[right]

        while nums[right] * (right - left + 1) - total > k:
            total -= nums[left]
            left += 1

        result = max(result, right - left + 1)

    return result
print(maxFrequency([1,2,4],5))