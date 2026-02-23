'''def print_all_divisior(num):
   
   divisor = 0
   
   for i in range(1,num):
        if num% i ==0:
           divisor += i
   if divisor != num:
       return False              
print(print_all_divisior(12))'''

def check_perfect_number(num):
    if num <= 1:
        return False

    divisor_sum = 1
    i = 2

    while i * i <= num:
        if num % i == 0:
            divisor_sum += i
            if i != num // i:
                divisor_sum += num // i
        i += 1

    return divisor_sum == num


# ---- Driver code ----
num = 28
print(check_perfect_number(num))
