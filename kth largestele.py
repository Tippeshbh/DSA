"""import heapq

def find_kth_element(nums,k):
    heap =[]

    for num in nums:
        heapq.heappush(heap,num)
        if len(heap)>k:
            heapq.heappop(heap)


    return heap[0]   

print(find_kth_element([2,3,1,5,6,7],3)) """


def findKthLargest( nums, k):
    nums.sort()              # sort array
    return nums[len(nums)-k]          # kth largest
print(findKthLargest([2,3,1,5,6,7],4))

'''def  count_word(sentence:str)-> int:
    word_count = 0
    inside_word = False

    for ch in sentence:
        if ch != " " and ch != '\t' and not inside_word:
            word_count += 1
            inside_word = True
        elif ch == " ":
            inside_word = False 
    

    return word_count

sentence = input("Enter a sentence : ")
result = count_word(sentence)
print("count of  words is" , result)  '''       


'''def armstrong_number(num):
    digits = str(num)
    power = len(digits)
    total = 0

    for d in digits:
        total += int(d)**power
    return total == num

print(armstrong_number(1234))   ''' 