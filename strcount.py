'''def stringCount(String):

    count = 0
    for index  in range(len(String)):
        print(str[index]--)
        count += 1
    return count 
print(stringCount("Thippesh"))  ''' 

def stringrevese(String):
    arr = list(String)
    left =   0
    right =  len(String)-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return  "".join(arr)
print(stringrevese("Mahesh Arli sir"))        