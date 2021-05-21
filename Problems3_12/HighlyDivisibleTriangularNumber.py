# Problem Number 12
# Problem Link https://projecteuler.net/problem=12

from functools import reduce

def divisors(x):
    expo_list = []
    count = 0
    divisor = 2
    while divisor <= x:
        while x % divisor == 0:
            x = x / divisor
            count += 1
        if count != 0:
            expo_list.append(count+1)
        divisor += 1
        count = 0
    return reduce(lambda x, y: x * y, expo_list, 1)


def first_tri(n):
    natural = 1
    first_tri_num = 0

    while True:
        first_tri_num += natural
        natural += 1
        if divisors(first_tri_num) > n:
            break
    return first_tri_num
 


#print(first_tri(4))
#print(first_tri(500))