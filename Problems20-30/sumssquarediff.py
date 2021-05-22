def sumofsquares(end):
    return sum([x ** 2 for x in range(1, end + 1)])
def squareofsum(end):
    total = sum([x for x in range(1, end + 1) ])
    return total ** 2
def difference(end):
    sumsquare = sumofsquares(end)
    squaresum = squareofsum(end)
    return squaresum - sumsquare
#print(difference(100))