def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, (num//2) + 1):
        if num % i == 0:
            return False
    return True
def nthprime(n):
    index = 0
    number = 0
    while index != n:
        number += 1
        if is_prime(number):
            index += 1
        
    return number
print(nthprime(10001))