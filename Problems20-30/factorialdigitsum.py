#Project Euler: 20
#Link: https://projecteuler.net/problem=20

import functools
import math
def factorial(num):
        return math.factorial(num)

def get_sum_factorial(num):
    number = factorial(num)
    digits = [int(ele) for ele in str(number)]
    return sum(digits)
        
    
print(get_sum_factorial(10))