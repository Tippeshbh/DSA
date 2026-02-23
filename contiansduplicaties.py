# using hashmap
'''def containsDuplicate(nums) -> bool:
    duplicates ={}   #take the hashmap it will contian the key = 0 value =true 
    for i in range(len(nums)): # itratuio for the eaach element
        if nums[i] in duplicates: # chech if that element in the duplicates 
            return True           # return it if is in duplicate
        duplicates[nums[i]] = True     # or elsr store it in the dictonary
    return False            # if thart not contia  that elemnt than retrun the False 
print(containsDuplicate([1,2,3,1]))        
'''
def containsDuplicate(nums) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return seen
        seen.add(num)

    return -1
print(containsDuplicate([1,2,3,4,1,5,7,8,7,5]))
