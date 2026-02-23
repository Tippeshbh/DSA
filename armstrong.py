





def is_Armstrong(number):
    len_num = find_length_of_number(number)
    sum_of_arms_num = 0
    num = number

    while num > 0:
        last_digit = num % 10
        sum_of_arms_num += last_digit ** len_num
        num //= 10
    return sum_of_arms_num ==number
number = int(input("Enter the number:"))
if is_Armstrong(number):
    print(f'yes, {number} is ArmstrongNumber')
else:
    print(f"no , {number} is not Armstrong Number")        

