def digitfifthpowers(num : int)-> bool:
    digits = [int(x) for x in str(num)]
    return num == sum([x ** 5 for x in digits])
def getallfifthpowers(start, limit : int) -> list:
    allnums = list([x for x in range(start, limit) if digitfifthpowers(x) == True])
    return sum(allnums)
print(getallfifthpowers(10, 1000000))