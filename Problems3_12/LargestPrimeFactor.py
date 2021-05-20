# Problem Number 3
# Problem Link https://projecteuler.net/problem=3

def largest_prime_fact(num):
    largest = 2
    while not num % 2:
        num //= 2
    factor = 3
    largest_factor = num ** 0.5
    while factor <= largest_factor:
        if not num % factor:
            largest = factor
            num //= factor
            while not num % factor:
                num //= factor
            if num == 1:
                return largest
            largest_factor = num ** 0.5
        factor += 2

    else:
        return num
