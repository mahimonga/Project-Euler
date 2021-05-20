import math


def upper_limit(n):
    return int(math.pow(10, n) - 1)


def lower_limit(n):
    return int(1 + (upper_limit(n) / 10))


def reverse(num):
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    return rev


def isPalindrome(num):
    return num == reverse(num)


def largest_palindrome(n):
    start = lower_limit(n)
    end = upper_limit(n)

    max_product = 0

    for i in range(end, start - 1, -1):
        for j in range(i, start - 1, -1):
            product = i * j
            if product < max_product:
                break
            elif isPalindrome(product) and product > max_product:
                max_product = product
    return max_product


def problem4():
    return largest_palindrome(3)