def consective_num(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i]== 1:
            count +=1
        else:
            count = 0
    return count 

result = consective_num([1,1,0,1,1,1,0,1,1,1])   
print(result)    
