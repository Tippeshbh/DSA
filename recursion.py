'''def sum_n_numbers(num):
    sum = 0

    for i in range(num):
        if i < 1:
            print(sum)
            return 
        print(i - 1 , sum + i)
sum_n_numbers(3) ''' 

'''def factorial(num):
    if num == 0:
        return 1
    return num*(num-1)
print(factorial(4))
'''
"""def factorial(n):
    if n == 0:
        return 1
    
    result = factorial(n - 1)   # go deeper
    return n * result           # backtrack step

print(factorial(4))"""


def containsDuplicate( nums) -> bool:
    duplicates ={}
    for i in range(len(nums)):
        if nums[i] in duplicates:
            return True 
        duplicates[nums[i]] = True     
    return False         
print(containsDuplicate([1,2,3,4,1]))        