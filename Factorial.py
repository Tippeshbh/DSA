def Find_factorial(num):
     product = 1 # product should be 1 because cant multiple by 0 at begging  
     while num!=0: # this loop will itrate till to num ==0
          product = product * num # this multiple by each product so the  throght number product will be incearse 
          num = num - 1 # this one for the each itration that makr num -1 

     return product
num = 4
Find_factorial(num)           