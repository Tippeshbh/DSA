'''n = 5
for i in range(n):
    for j in range(n):
        print("&", end=" ")
    print()   
'''
'''n = 5
for i in range(1,n+1):
    for j in range(i):
        print("#",end =" ")
    print() '''    

'''n = 10
for i in range(0,n+1,+2):
    for j in range(i):
         print(i, end = " ")
    print()'''    

'''n = 5
for i in range(1,n+1):
    for j in range(i):
        print("*", end = " ")
    print()    '''  

# left aligned Triangle

'''n = 5
for i in range(1,n+1):
    print("*" * i) '''

# pyramid patteran

'''n = 5
for i in range(1, n + 1):
    for s in range(n-1):
        print(" ",end = " ")
    for j in range(1*i-1):
        print("*", end = " ")
    print() '''

'''n =5
for i in range(n):
    print(" " * (n-i-1) + "*" * (2*i+1))  
for i in range(n,-1,-1):
    print(" " * (n-i) + "*" * (2*i -1))
    

n = 5 
for i in range(n):
    print(" "*(n-i-1) + "*"*(2*i+1))
for i in range(n-1,0,-1):
    print(" "*(n-i) + "*"*(2*i-1))  '''


'''n =4
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end = " ")
    print()
'''

'''n  = 4
for i in range(1, n+1):
    print((str(i)+ " ") * i)'''
'''n = 10
for i in range(1,n+1):
    for j in range(2,3+i):
        print(j,end = " ")
    print()       
'''

'''def countdigit(num):

    count = 0

    for i in num:
        count += 1
    return count
print(countdigit("123")) '''

def countdigit(num):
    count = 0
    while num > 0:
        count += 1
        num // 10
    return count

print(countdigit(123))   # Output: 3'''

'''for i in range(10):
    x = '*'
    x = x*i
    print(f'{x: ^10}')'''

"""n = 5
for i in range(0,n+1):
    print(" " * (n-i) + "*" * (i)) """


'''n = 5
for i in range(0,n):
    for j in range(i):
        print(i,end =" ")
    print()  ''' 