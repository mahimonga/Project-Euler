#Problem number 5
#Problem link https://projecteuler.net/problem=5

check = [11, 13, 14, 16, 17, 18, 19, 20]

def smallestMultiple(step):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in check):
            return num
    return None

if __name__ == '__main__':
    solution = smallestMultiple(2520)
    if solution is None:
        print("Answer not found")
    else:
        print("Smallest multiple:", solution)