with open("S1.in") as file:
	inpu = int(file.read())

def isDistinct(string):
	characters = []

	for i in string:
		if i in characters:
			return False

		characters.append(i)

	return True

def nextDistinctYear(year):
	year += 1
	while not isDistinct(str(year)):
		year += 1
	return year

print(nextDistinctYear(inpu))