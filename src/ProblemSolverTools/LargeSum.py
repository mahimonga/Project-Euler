def toNumbersArray(filename):
	numbers = open(filename, 'r')
	numbersArray = []
	for number in numbers:
		numbersArray.append(int(number))
	return numbersArray

def largeSum(filename):
	numbersArray = toNumbersArray(filename)
	sumOfNumbers = sum(numbersArray)
	return str(sumOfNumbers)[:10]