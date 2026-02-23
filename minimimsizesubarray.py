def minimumsubarrary(nums,target):
    left =0
    total = 0 
    ans =float('inf')

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            ans = min(ans,right-left +1)
            total =-nums[left]
            left +=1
    
    return 0 if ans == float('inf') else ans 

print(minimumsubarrary([4,4,1,2], 4))     

