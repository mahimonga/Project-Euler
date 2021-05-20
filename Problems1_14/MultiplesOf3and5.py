def is_multiple(num):
    return num % 3 == 0 or num % 5 == 0

def multiples(n):
    return [num for num in range(n) if is_multiple(num)]

def sum_of_multiples(n):
    return sum(multiples(n))

def problem1():
    return sum_of_multiples(1000)    